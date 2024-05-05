from rest_framework import serializers
from music_app.models import Artis,Album,Lagu,Playlist


class PlaylistSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class LaguSerilizer(serializers.ModelSerializer):
    playlist = PlaylistSerilizer(many=True,read_only=True)
    class Meta:
        model = Lagu
        fields = '__all__'

class AlbumSerilizer(serializers.ModelSerializer):
    lagu = LaguSerilizer(many=True,read_only=True)
    class Meta:
        model = Album
        fields = '__all__'


class ArtisSerilizer(serializers.ModelSerializer):
    album = AlbumSerilizer(many=True,read_only=True)
    class Meta:
        model = Artis
        fields = '__all__'
