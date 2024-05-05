from django.urls import path
from music_app.views import ArtistList,AlbumList,LaguList,PlayList

urlpatterns = [
    path('artis/', ArtistList.as_view()),
    path('album/', AlbumList.as_view()),
    path('lagu/', LaguList.as_view()),
    path('playlist/', PlayList.as_view()), 
]