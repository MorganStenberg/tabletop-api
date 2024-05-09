from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    review_count = serializers.ReadOnlyField()
    saved_count = serializers.ReadOnlyField()

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

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'content', 'name',
            'favorite_game', 'image', 'is_owner', 'review_count',
            'saved_count',
        ]
