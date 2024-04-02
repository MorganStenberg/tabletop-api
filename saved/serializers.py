from django.db import IntegrityError
from rest_framework import serializers
from .models import Save


class SaveSerializer(serializers.ModelSerializer):
    """
    Serializer for the Save model.
    Overriding create method, credit to Stackoverflow.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    review_title = serializers.ReadOnlyField(source='review.title')
    review_game = serializers.ReadOnlyField(source='review.game')

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'duplicate save not possible'
            })

    class Meta:
        model = Save
        fields = [
            'id', 'owner', 'review', 'review_title', 'review_game',
            'created_at',
        ]
