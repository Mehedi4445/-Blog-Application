from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ("Technology", "Technology"),
        ("Education", "Education"),
        ("Travel", "Travel"),
        ("Lifestyle", "Lifestyle"),
        ("Programming", "Programming"),
        ("Other", "Other"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Other"
    )
    image = models.URLField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def excerpt(self):
        if len(self.content) <= 180:
            return self.content
        return self.content[:180] + "..."
