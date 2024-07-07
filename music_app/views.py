from music_app.models import Artis,Album,Lagu,Playlist
from music_app.serializers import ArtisSerilizer,AlbumSerilizer,LaguSerilizer,PlaylistSerilizer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

class ArtistList(generics.ListCreateAPIView):
    queryset = Artis.objects.all()
    serializer_class = ArtisSerilizer

class ArtistDetail(APIView):
    def get_object(self, pk):
        try:
            return Artis.objects.get(pk=pk)
        except Artis.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Artis = self.get_object(pk)
        serializer = ArtisSerilizer(Artis)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Artis = self.get_object(pk)
        serializer = ArtisSerilizer(Artis, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Artis = self.get_object(pk)
        Artis.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerilizer

class AlbumDetail(APIView):
    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Album = self.get_object(pk)
        serializer = AlbumSerilizer(Album)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Album = self.get_object(pk)
        serializer = AlbumSerilizer(Album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Album = self.get_object(pk)
        Album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LaguList(generics.ListCreateAPIView):
    queryset = Lagu.objects.all()
    serializer_class = LaguSerilizer

class LaguDetail(APIView):
    def get_object(self, pk):
        try:
            return Lagu.objects.get(pk=pk)
        except Lagu.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Lagu = self.get_object(pk)
        serializer = LaguSerilizer(Lagu)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Lagu = self.get_object(pk)
        serializer = LaguSerilizer(Lagu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Lagu = self.get_object(pk)
        Lagu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

class PlayList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerilizer

class PlaylistDetail(APIView):
    def get_object(self, pk):
        try:
            return Playlist.objects.get(pk=pk)
        except Playlist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        PlayList = self.get_object(pk)
        serializer = PlaylistSerilizer(PlayList)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        PlayList = self.get_object(pk)
        serializer = PlaylistSerilizer(Playlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Playlist = self.get_object(pk)
        Playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)