from django.urls import path, include
from music_app.views import ArtistList, ArtistDetail, AlbumList,AlbumDetail, LaguList,LaguDetail, PlayList, PlaylistDetail,UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('user', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('artis/', ArtistList.as_view()),
    path('artis/<int:pk>/', ArtistDetail.as_view()),
    path('album/', AlbumList.as_view()),
    path('album/<int:pk>/', AlbumDetail.as_view()),
    path('lagu/', LaguList.as_view()),
    path('lagu/<int:pk>/', LaguDetail.as_view()),
    path('playlist/', PlayList.as_view()),
    path('playlist/<int:pk>/', PlaylistDetail.as_view()), 
]