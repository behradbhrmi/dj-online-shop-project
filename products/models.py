from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class DemonstrableCommentsManager(models.Manager):
    def get_queryset(self):
        return super(DemonstrableCommentsManager, self).get_queryset().filter(demonstrable=True)


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    availability = models.BooleanField(default=True)
    # cover = models.ImageField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


class Comment(models.Model):
    STARS = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Perfect'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    satisfaction = models.CharField(max_length=8, choices=STARS)
    demonstrable = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    # Manager
    objects = models.Manager()
    demonstrable_comments_manager = DemonstrableCommentsManager()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])
