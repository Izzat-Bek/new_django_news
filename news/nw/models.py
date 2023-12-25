from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .bot import send_news
from django.db.models.signals import post_save
from django.dispatch import receiver


class CategoryModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class PostModel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    image1 = models.ImageField(upload_to="news/", blank=True, null=True, verbose_name="Image 1")
    content1 = RichTextField(blank=True, null=True, verbose_name="Content")
    image2 = models.ImageField(upload_to="news/", blank=True, null=True, verbose_name="Image 2")
    content2 = RichTextField(blank=True, null=True, verbose_name="Content")
    image3 = models.ImageField(upload_to="news/", blank=True, null=True, verbose_name="Image 3")
    content3 = RichTextField(blank=True, null=True, verbose_name="Content")
    image4 = models.ImageField(upload_to="news/", blank=True, null=True, verbose_name="Image 4")
    content4 = RichTextField(blank=True, null=True, verbose_name="Content")
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name="Category")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


@receiver(post_save, sender=PostModel)
async def send_news_to_telegram(sender, instance, created, **kwargs):
    await send_news(instance)



class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Post")
    username = models.CharField(max_length=255, blank=True, null=True, verbose_name="Username")
    content = RichTextField(blank=True, null=True, verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class StarModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Post")
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Username")
    num_star = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Num Star",
                                                validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.num_star)

    class Meta:
        verbose_name = "Star"
        verbose_name_plural = "Stars"
