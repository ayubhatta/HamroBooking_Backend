from rest_framework import serializers
from .models import Review
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        
    def save(self, **kwargs):
        user = self.context['request'].user
        review = Review(
            user_id = user,
            star_count = self.validated_data['star_count'],
            comment = self.validated_data['comment'],
        )
        hotel_id = self.validated_data['hotel_id']
        
        review.save()
        return review
     



