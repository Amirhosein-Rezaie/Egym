from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=255, db_index=True, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    uploaded_at = models.DateField(auto_now_add=True, blank=False, null=False)

    class Meta:
        db_table = 'blog'

    def __str__(self):
        return self.title
