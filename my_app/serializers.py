from rest_framework import serializers
from .models import Position, Comments

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['lat', 'lng']

class CommentsSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = Comments
        fields = ['id', 'cityName', 'country', 'emoji', 'date', 'notes', 'position']
        read_only_fields = ['id', 'date']

    def create(self, validated_data):
        position_data = validated_data.pop('position')
        position = Position.objects.create(**position_data)
        comment = Comments.objects.create(position=position, **validated_data)
        return comment
    
    def update(self, instance, validated_data):
        position_data = validated_data.pop('position', None)
        if position_data:
            Position.objects.filter(pk=instance.position.pk).update(**position_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
