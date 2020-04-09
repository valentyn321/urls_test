from main.models import Url
from django.views.generic import ListView


class UrlListView(ListView):
    model = Url
    template_name = 'main/main.html'
