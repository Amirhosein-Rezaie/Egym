from django.db import models


class Image(models.Model):
    photo = models.ImageField(upload_to='gallery/')

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.photo} -> {self.uploaded_at}"
    
    class Meta:
        db_table = 'gallery'
        
