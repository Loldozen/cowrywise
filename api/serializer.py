from rest_framework import serializers

class APISerializer(serializers.Serializer):
    
    id = serializers.UUIDField()
    created_datetime = serializers.CharField(max_length=200)