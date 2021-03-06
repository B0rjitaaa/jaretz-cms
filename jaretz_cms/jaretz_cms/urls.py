from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jaretz_cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'shop.views.index', name='index'),
    url(r'^items/$', 'shop.views.items', name='items'),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
