from django.db import models
from django.contrib.auth.models import User
#from PIL import Image
from .utils import validate_phone_number


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
        verbose_name="Пользователь")
    image = models.ImageField(upload_to='profile/',
        verbose_name="Фото профиля",
        help_text="Фотография должно быть Х на Х",
        blank=True, null=True)
    description = models.TextField(max_length=200,
        verbose_name="Информация", blank=True, null=True)
    birth_data = models.DateField(verbose_name="Дата рождения",
        blank=True, null=True)
    phone = models.CharField(max_length=20,
        verbose_name="Номер телефона",
        validators=[validate_phone_number],
        blank=True, null=True)

class Author(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.user.username


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
