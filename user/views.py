import logging

from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import RegisterSerializer

logger = logging.getLogger('user.views')

def send_activation_email(request, user):
    current_site = get_current_site(request)
    mail_subject = 'Activate your account'
    mail_subject = 'Activate your account'
    activation_link = f"http://{current_site.domain}/api/user/activate/{urlsafe_base64_encode(force_bytes(user.pk))}/{default_token_generator.make_token(user)}/"
    message = f"Hi {user.username},\n\nClick the following link to activate your account:\n\n{activation_link}"
    send_mail(mail_subject, message, 'your-email@example.com', [user.email])

@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
    serializer = RegisterSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        user = serializer.save()
        send_activation_email(request, user)
        return Response({'message': 'User Registered'}, status = status.HTTP_201_CREATED)

    else:
        data = serializer.errors
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Account has been activated', status=status.HTTP_200_OK)  # Replace 'activation_success' with the URL name of your activation success page
    else:
        return HttpResponse('Account cannot be activated', status=status.HTTP_400_BAD_REQUEST)  # Replace 'activation_failure' with the URL name of your activation failure page

@api_view(['DELETE',])
@permission_classes([AllowAny])
def users_view(request,id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({'message': 'The user does not exist'}, status = status.HTTP_204_NO_CONTENT)

    
    operation = user.delete()
    data={}
    if operation:
        data["success"] = "delete success"
    else:
        data["failure"] = "delete failed "
    return Response(data=data)

@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def user_login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    login(request, user)
    refresh = RefreshToken.for_user(user)
    return Response({"message":"user logged-in",
                      "access_token":str(refresh.access_token),
                      "refresh_token":str(refresh)
                      })