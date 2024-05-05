from django.db import models

class Artis(models.Model):
    nama = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    
    def _str_(self):
        return self.nama
    
class Album(models.Model):
    judul = models.CharField(max_length=100)
    artis = models.ForeignKey(Artis, on_delete=models.CASCADE,related_name='album')
    tahun_rilis = models.IntegerField()
    
    def _str_(self):
        return self.artis.nama
    
class Lagu(models.Model):
    judul = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE,related_name='lagu')
    durasi = models.DurationField()
    
    def _str_(self):
        return self.judul
    
class Playlist(models.Model):
    nama = models.CharField(max_length=100)
    lagu = models.ManyToManyField(Lagu,related_name='playlist')
    
    def _str_(self):
        return self.nama
