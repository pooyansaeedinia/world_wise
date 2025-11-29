from rest_framework import serializers

from my_app.models import Position, Comments


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()
    class Meta:
        model = Comments
        fields = '__all__'

    @staticmethod
    def get_position(obj):
        return {"lat":obj.position.lat, "lng":obj.position.lng}