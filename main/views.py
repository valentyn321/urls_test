from main.models import Url
from django.http import JsonResponse
from django.views.generic import ListView
import urllib3



class UrlListView(ListView):
    model = Url
    template_name = 'main/main.html'


def CheckUrls(request):
    http = urllib3.PoolManager()
    queryset =  Url.objects.all()
    for obj in queryset:        
        if http.request('GET', obj.reference).status == 200:
            obj.up = True
            obj.save()

    return JsonResponse({})