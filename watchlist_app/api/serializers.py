from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = "__all__" #individual fields can be included as well- ['id','name'....]
        # fields = ['id','name','description',]
        # exclude = ['active'] it includes all other fields except exclude field
        
    def get_len_name(self, object):
        length = len(object.name)
        return length
    
    #object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and description must not be same.")
        return value
    
    #field level validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value
        