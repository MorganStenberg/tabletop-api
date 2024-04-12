from rest_framework import serializers
from .models import Game
from reviews.models import Review


class GameSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    saved_review_connect = serializers.SerializerMethodField(read_only=True)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_saved_review_connect(self, obj):
        review_title = []
        for review in obj.review_connect.all():
            review_title.append({
                "review": review.review.title,
                "id": review.review.pk})
        return review_title

    class Meta:
        model = Game
        fields = [
            'id', 'owner', 'is_owner', 'genre', 'review_connect',
            'description', 'saved_review_connect', 'profile_id',
            'title', 'created_at',
        ]
