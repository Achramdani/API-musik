from music_app.models import Artis,Album,Lagu,Playlist
from music_app.serializers import ArtisSerilizer,AlbumSerilizer,LaguSerilizer,PlaylistSerilizer
from rest_framework import generics


class ArtistList(generics.ListCreateAPIView):
    queryset = Artis.objects.all()
    serializer_class = ArtisSerilizer

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerilizer

class LaguList(generics.ListCreateAPIView):
    queryset = Lagu.objects.all()
    serializer_class = LaguSerilizer

class PlayList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerilizer