from rest_framework import serializers
from watchlist_app.models import Watchlists, StreamPlatforms


class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model= StreamPlatforms
        fields = "__all__"
class WatchlistSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    class Meta:
        model= Watchlists
        fields = "__all__"
        # fields = ["id", "name", "description"]
        # exclude = ["name"]
        
    def get_len_name(self, object):
        return len(object.name)

# def name_length(value):
#     if len(value)<2:
#             raise serializers.ValidationError('Name is too short')

# class MovieSerializer(serializers.Serializer):
#     id= serializers.IntegerField(read_only=True)
#     name= serializers.CharField(validators=[name_length])
#     description= serializers.CharField()
#     active= serializers.BooleanField()

#     def create(self, validated_data):
#         return Watchlists.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description= validated_data.get('description', instance.description)
#         instance.active= validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and Description should be different!')
#         else:
#             return data
        
#     def validate_name(self, value):
#         if len(value)<2:
#             raise serializers.ValidationError('Name is too short')
#         else:
#             return value