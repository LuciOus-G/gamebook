from django.conf.urls import url
from django.contrib import admin
from gamebook_art import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^login/admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^archive/(?P<slug>[\w-]+)/$', views.articles, name='article'),
    url(r'^archive/$', views.game, name='game'),
    url(r'^search/$', views.search, name='search')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
