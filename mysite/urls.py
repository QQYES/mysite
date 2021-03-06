"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, patterns
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic import list
from books.models import Publisher
from mysite.views import about_pages

# from mysite.views import hello, current_datetime, hours_ahead, display_meta
# from books.views import search
# from contact.views import contact
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^time/$', current_datetime),
#     url(r'^hello/$', hello),
#     url(r'^time/plus/(\d{1,2})/$', hours_ahead),
#     url(r'^meta/$', display_meta),
#     # url(r'^search-form/$', search_form),
#     url(r'^search/$', search),
#     url(r'^contact/$', contact),
#     # url(r'^$', my_homepage_view),
# ]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

publisher_info = {
    'queryset': Publisher.objects.all(),
    'template_name': 'publisher_list_page.html',
}

urlpatterns += patterns('',
                        (r'^publishers/$',
                         list.ListView.as_view(model=Publisher, template_name='publisher_list_page.html')), )

urlpatterns += patterns('', (r'^about/$', TemplateView.as_view(template_name="about.html")),
                        (r'^about/(\w+)/$', about_pages), )

urlpatterns += patterns('mysite.views',
                        url(r'^hello/$', 'hello'),
                        url(r'^time/$', 'current_datetime'),
                        url(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
                        )

urlpatterns += patterns('books.views',
                        url(r'^search/$', 'search'),
                        )

urlpatterns += patterns('contact.views',
                        url(r'^contact/$', 'contact'),
                        )

urlpatterns += patterns('contact.views',
                        url(r'^contact/$', 'contact'),
                        )
