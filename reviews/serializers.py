from rest_framework import serializers
from .models import Review
from likes.models import Like

#Credit to Code Institute Walkthrough
class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    like_id = serializers.SerializerMethodField()


    def validate_image(self, value):
        if value is None:
            return value

        if value.size > 1024 * 1024 * 2: 
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            likes = Like.objects.filter(
                owner=user, review=obj
            ).first()
            return likes.id if likes else None
        return None

    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'is_owner', 'created_at', 'content', 'image',
            'rating', 'game', 'profile_image', 'profile_id', 'title',
            'comments_count', 'likes_count', 'like_id',
        ]