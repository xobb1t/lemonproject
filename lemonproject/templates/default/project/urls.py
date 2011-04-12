from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from lemon import extradmin
from lemon import metatags
from lemon import sitemaps


extradmin.autodiscover()
metatags.autodiscover()
sitemaps.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(extradmin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^404$', TemplateView.as_view(template_name='404.html')),
        url(r'^500$', TemplateView.as_view(template_name='500.html')),
    )
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
