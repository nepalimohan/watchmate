from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField(default=True)
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data) 
        #the data passed to in def movies_list post method is because of this return
        
    def update(self, instance, validated_data):
        # old value = new name.....the process of validating the data
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance