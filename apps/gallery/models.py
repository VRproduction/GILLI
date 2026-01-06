from django.db import models
from django.forms import ValidationError

class ImageGallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    caption = models.CharField(max_length=200, null=True, blank = True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption if self.caption is not None else f'Image {self.pk}'
    
    
class VideoGallery(models.Model):
    caption = models.CharField(max_length=200, null=True, blank = True)
    video = models.FileField(upload_to='videos', null= True, blank = True)
    youtube_iframe = models.TextField(null=True, blank = True)
    thumbnail = models.ImageField(upload_to='thumbnails', null=True, blank = True)
    
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption if self.caption is not None else f'Video {self.pk}'
    
    
    def clean(self):
        if not self.video and not self.youtube_iframe:
            raise ValidationError('You must provide either a video or a youtube_iframe.')
        if self.video and self.youtube_iframe:
            raise ValidationError('Only one of video or youtube_iframe can be provided.')
        return super().clean()
