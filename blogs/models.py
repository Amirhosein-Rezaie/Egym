from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    content = models.TextField()
    uploaded_at = models.DateField(auto_now_add=True)

    class Meta:
        db_name = 'blog'

    def __str__(self):
        return self.title
