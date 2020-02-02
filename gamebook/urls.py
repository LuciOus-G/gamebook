from django.conf.urls import url
from django.contrib import admin
from gamebook_art import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^login/admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^archive/(?P<slug>[\w-]+)/$', views.articles, name='article'),
    url(r'^archive/$', views.game, name='game'),
    url(r'^search/$', views.search, name='search'),
    url(r'^support/$', views.faq, name='support'),
    url(r'^support/req/$', views.reqGameForm, name='reqGame'),
    url(r'^support/req/send$', views.reqGame, name='send'),
    url(r'^support/req/send/message$', views.message, name='msg'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
