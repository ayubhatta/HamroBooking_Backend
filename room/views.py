from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .models import Room, RoomMaintenance
from .serializers import RoomSerializer, RoomMaintenanceSerializer

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def create_list_view(request):
    if request.method == 'GET':
        room = Room.objects.all()
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data': serializer.data,
                'message': 'Room created successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def detail_update_delete_view(request, pk):
    try:
        room = get_object_or_404(Room.objects.all(), pk=pk)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RoomSerializer(room, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def create_list_maintenance_view(request):
    if request.method == 'GET':
        maintenance_records = RoomMaintenance.objects.all()
        serializer = RoomMaintenanceSerializer(maintenance_records, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RoomMaintenanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data': serializer.data,
                'message': 'Room maintenance created successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def detail_update_delete_maintenance_view(request, pk):
    try:
        maintenance_record = get_object_or_404(RoomMaintenance.objects.all(), pk=pk)
    except RoomMaintenance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RoomMaintenanceSerializer(maintenance_record)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RoomMaintenanceSerializer(maintenance_record, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        maintenance_record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)