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
from django.views.decorators.csrf import csrf_protect
from django.core.mail import EmailMultiAlternatives
from django_user_agents.utils import get_user_agent

def home(request):
    art = Gamebook_art.objects.all().order_by('-date')
    crl = Gamebook_art.objects.all().order_by('?')

    crl.random()

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

def support(request):
    return render(request, 'support.html')

def search(request):
    # search system
    query = request.GET.get('search', None)
    results  = Gamebook_art.objects.filter(Q(title__icontains=query)).order_by('-date')
    # end search system


    paginator = Paginator(results, 10)
    page = request.GET.get('page')
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

    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        Gamebook_art.snp = 170
    elif user_agent.is_pc:
        Gamebook_art.snp = 250

    return render(request, 'search.html', context)
    # end render

@csrf_protect
def reqGame(request):
    # get data from POST method
    name = request.POST.get('name')
    email = request.POST.get('email')
    game = request.POST.get('game')
    # end get data from POST

    # send to developer/admin
    subject1 = 'Request Game'
    fromEmail1 = 'gamebook.powered@gmail.com'
    to1 = ['gamebook.powered@gmail.com']
    body1 = 'Name : ' + name + '\nEmail : ' + email + '\nGame : ' + game
    msg1 = EmailMultiAlternatives(subject1, body1, fromEmail1, to1)
    msg1.send()
    # end send to developer/admin

    # send into client
    to2 = [email]
    with open('/var/www/gamebook/gamebook_art/email.html', encoding='utf8') as t:
        text = t.read()
    msg2 = EmailMultiAlternatives('Thank You', '', fromEmail1, to2)
    msg2.attach_alternative(text, 'text/html')
    msg2.send()
    # end of send to client
    return render(request, 'send.html')

def reqGameForm(request):
    return render(request, 'reqGame.html')

def articles(request, slug):
	art = Gamebook_art.objects.all().order_by('-date')
	article = Gamebook_art.objects.get(slug=slug)
	return render (request, 'article.html', {'article':article, 'art':art, })

def game(request):
    art = Gamebook_art.objects.all().order_by('-date')
    paginator = Paginator(art, 10)
    page = request.GET.get('page', 1)
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        Gamebook_art.snp = 170
    elif user_agent.is_pc:
        Gamebook_art.snp = 250

    try:
        art = paginator.page(page)
    except PageNotAnInteger:
        art = paginator.page(1)
    except EmptyPage:
        art = paginator.page(paginator.num_pages)

    return render (request, 'games.html', {'art':art})

# faq
def faq(request):
    faqs = carousel.objects.all().order_by('faq')

    context = {
        'faq':faqs
    }

    return render(request, 'faq.html', context)

@csrf_protect
def message(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    body = request.POST.get('body')
    fromEmail1 = 'gamebook.powered@gmail.com'
    to = ['gamebook.powered@gmail.com']

    bodyMsg = 'Message From Visitors\n' + 'Name : ' + name + '\nEmail : ' + email + '\nMessage : ' + body

    msgSend = EmailMultiAlternatives(subject, bodyMsg, fromEmail1, to)
    msgSend.send()

    to2 = [email]
    with open('/var/www/gamebook/gamebook_art/email.html', encoding='utf8') as t:
        text = t.read()
    msg2 = EmailMultiAlternatives('Thank You', '', fromEmail1, to2)
    msg2.attach_alternative(text, 'text/html')
    msg2.send()
    # end of send to client
    return render(request, 'send.html')

    # toclient
