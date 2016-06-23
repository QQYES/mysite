from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic import TemplateView
import datetime


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def about_pages(request, page):
    try:
        return TemplateView.as_view(request, template='about/%s.html' % page)
    except TemplateDoesNotExist:
        raise Http404()
