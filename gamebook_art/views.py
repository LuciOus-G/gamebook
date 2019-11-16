from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Gamebook_art
from .models import carousel
from django.http import HttpResponse
from itertools import chain
from django.views.generic import ListView
from django.db.models import Q
from operator import attrgetter
from .pagination import pagination

def home(request):
    art = Gamebook_art.objects.all().order_by('date')
    crl = Gamebook_art.objects.all().order_by('title')

    # crl.random(10)
    context = {
        'art':art,
        'crl':crl
    }
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    return render(request, 'home.html', context)

def search(request):
    # search system
    query = request.GET.get('search', None)
    results  = Gamebook_art.objects.filter(Q(title__icontains=query))
    # end search system


    paginator = Paginator(results, 5)
    page = request.GET.get('page', 10)
    try:
        art = paginator.page(page)
    except PageNotAnInteger:
        art = paginator.page(1)
    except EmptyPage:
        art = paginator.page(paginator.num_pages)


    # render
    context = {
        'art1':results,
        'art':art
    }

    return render(request, 'search.html', context)
    # end render

def articles(request, slug):
	art = Gamebook_art.objects.all().order_by('date')
	crl = carousel.objects.all()
	article = Gamebook_art.objects.get(slug=slug)
	return render (request, 'article.html', {'article':article, 'art':art, 'crl':crl, })

def game (request):
	art = Gamebook_art.objects.all().order_by('date')
	paginator = Paginator(art, 10)
	page = request.GET.get('page', 1)

	try:
		art = paginator.page(page)
	except PageNotAnInteger:
		art = paginator.page(1)
	except EmptyPage:
		art = paginator.page(paginator.num_pages)

	return render(request, 'games.html', {'art':art})
