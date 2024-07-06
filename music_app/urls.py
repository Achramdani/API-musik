from django.urls import path
from music_app.views import ArtistList, ArtistDetail, AlbumList,AlbumDetail, LaguList,LaguDetail, PlayList, PlaylistDetail

urlpatterns = [
    path('artis/', ArtistList.as_view()),
    path('artis/<int:pk>/', ArtistDetail.as_view()),
    path('album/', AlbumList.as_view()),
    path('album/<int:pk>/', AlbumDetail.as_view()),
    path('lagu/', LaguList.as_view()),
    path('lagu/<int:pk>/', LaguDetail.as_view()),
    path('playlist/', PlayList.as_view()),
    path('playlist/<int:pk>/', PlaylistDetail.as_view()), 
]