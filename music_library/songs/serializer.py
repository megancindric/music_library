from rest_framework import serializers
from songs.models import Song


class SongSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, allow_blank = False)
    artist = serializers.CharField(required=True, allow_blank = False)
    album = serializers.CharField(required=True,allow_blank=False)
    release_date = serializers.DateField()
    genre = serializers.CharField(required=True,allow_blank=False)


    def create(self, validated_data):
        return Song.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.artist = validated_data.get('artist', instance.artist)
        instance.album = validated_data.get('album', instance.album)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.save()
        return instance

