from rest_framework import serializers
from music_app.models import Artis,Album,Lagu,Playlist


class ArtisSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Artis
        fields = '__all__'

class AlbumSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class LaguSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Lagu
        fields = '__all__'

class PlaylistSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'