from django.db import models


class CompanyNews(models.Model):
    title_en = models.CharField(max_length=255)
    title_kh = models.CharField(max_length=255, blank=True)
    title_cn = models.CharField(max_length=255, blank=True)

    short_en = models.TextField(blank=True)
    short_kh = models.TextField(blank=True)
    short_cn = models.TextField(blank=True)

    content_en = models.TextField(blank=True)
    content_kh = models.TextField(blank=True)
    content_cn = models.TextField(blank=True)

    # Thumbnail = show on Home page news card
    image = models.ImageField(upload_to="company_news/thumbnails/", blank=True, null=True)

    # Detail image = show inside news detail page
    detail_image = models.ImageField(upload_to="company_news/detail/", blank=True, null=True)

    video = models.FileField(upload_to="company_news/videos/", blank=True, null=True)

    # Higher number shows first
    sort_order = models.PositiveIntegerField(default=0)

    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-sort_order", "-created_at"]

    def __str__(self):
        return self.title_en


class CompanyNewsPhoto(models.Model):
    news = models.ForeignKey(CompanyNews, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(upload_to="company_news/gallery/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for {self.news.title_en}"