from django.http import HttpResponse
from django.template import loader
from .models import hosi


def index(request):
    myhosi = hosi.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'hosi': myhosi,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('admin.html')
    return HttpResponse(template.render({}, request))
def dash(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render({}, request))
