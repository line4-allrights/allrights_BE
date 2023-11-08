from django.db import models
from django.utils import timezone
from account.models import User

class Music(models.Model):
    MUSIC_TYPES = (
        ('effect', '효과음'),
        ('background', '배경음악'),
    )

    GENRE_TYPES = (
        ('hiphop', '힙합'),
        ('rock', '락'),
        ('pop', '팝'),
        ('jazz', '재즈'),
        ('classic', '클래식'),
        ('blues', '블루스'),
        ('fork', '포크'),
        ('indie', '인디'),
        ('rnb', 'R&B'),
    )

    MOOD_TYPES = (
        ('depressed', '우울한'),
        ('excited', '신나는'),
        ('happy', '쾌활한'),
        ('peaceful', '평화로운'),
        ('serious', '심각한'),
        ('urgent', '급박한'),
        ('horrifying', '소름 끼치는'),
    )

    INSTRUMENTS_TYPES = (
        ('piano', '피아노'),
        ('acoustic guitar', '어쿠스틱 기타'),
        ('bass', '베이스'),
        ('drum', '드럼'),
        ('violin', '바이올린'),
    )

    title = models.CharField(max_length=100)
    music_file = models.FileField(upload_to='music/')
    music_type = models.CharField(max_length=100, choices=MUSIC_TYPES)
    genre = models.CharField(max_length=100, choices=GENRE_TYPES)
    instruments = models.CharField(max_length=100, choices=INSTRUMENTS_TYPES)
    mood = models.CharField(max_length=100, choices=MOOD_TYPES)
    length = models.PositiveIntegerField(default=0)
    description = models.TextField()
    upload_date = models.DateTimeField(default=timezone.now)  # 업로드 날짜 및 시간
    downloads = models.PositiveIntegerField(default=0)  # 다운로드 횟수
    author=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    liker=models.ManyToManyField(User,related_name='like_music',default=[],blank=True)