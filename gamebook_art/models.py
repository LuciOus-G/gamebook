from django.db import models
import datetime
from django.utils.text import slugify
from django.db.models import Q
from django_random_queryset import RandomManager
# Create your models here.

class PostQuerySet(models.QuerySet):
	def search(self, query=None):
		qs = self
		if quersy is not None:
			or_lookup = (Q(title__icontains=query) | Q(body__icontains=query) | Q(slug__icontains=query))
			qs = qs.filter(or_lookup).distinct()
		return qs

class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                         Q(description__icontains=query)|
                         Q(slug__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


class Gamebook_art(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(blank=True, editable=False)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	thumbnail = models.ImageField(upload_to='content_thumbnails', default='')
	image1 = models.ImageField(default='', upload_to="Screenshoot")
	image2 = models.ImageField(default='', upload_to="Screenshoot")
	min_req = models.TextField(default='')
	rec_req = models.TextField(default='')
	Video_url = models.	URLField(default='', blank=True)
	Gdrive1 = models.URLField(default='', blank=True)
	Gdrive2 = models.URLField(default='', blank=True)

	objects = RandomManager()

	def save(self):
		self.slug = slugify(self.title)
		super(Gamebook_art, self).save()
		print(Gamebook_art.slug)

	def __str__(self):
		return '{}, {}'.format(self.id, self.title)

	def snippet(self):
		return self.body [:275] + ' [...]'

class carousel (models.Model):
	title = models.CharField(max_length=100, default='')
	slug = models.SlugField(default='')
	banners = models.ImageField(upload_to='image', default='')

	def __str__(self):
		return self.title
