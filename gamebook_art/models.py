from django.db import models
from tinymce_4.fields import TinyMCEModelField
import datetime
from django.utils.text import slugify
from django.db.models import Q
from django_random_queryset import RandomManager
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
# Create your models here.
# variable fields
# end variable fields

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
	objects = RandomManager()
	title = models.CharField(max_length=255, default='')
	slug = models.SlugField(blank=True, editable=False, max_length=255)
	body = models.TextField(default='')
	date = models.DateTimeField(auto_now_add=True)
	thumbnail = models.ImageField(upload_to='content_thumbnails', default='')
	image1 = models.ImageField(default='', upload_to="Screenshoot")
	image2 = models.ImageField(default='', upload_to="Screenshoot")
	min_req = models.TextField(default='')
	rec_req = models.TextField(default='')
	Video_url = models.	URLField(default='', blank=True, max_length=1000)
	Gdrive1 = models.URLField(default='', blank=True, max_length=1000)
	Gdrive2 = models.URLField(default='', blank=True, max_length=1000)

	def save(self):
		self.slug = slugify(self.title)
		super(Gamebook_art, self).save()
		print(Gamebook_art.slug)

	def __str__(self):
		return '{}, {}'.format(self.id, self.title)
	snp = 250

	def snippet(self):
		return self.body [:self.snp] + ' [...]'

class carousel (models.Model):
	faq = models.CharField(max_length=255, default='')
	ans = HTMLField()
	num = models.CharField(max_length=255, default='')

	def __str__(self):
		return '{}, {}'.format(self.id, seld.faq)
