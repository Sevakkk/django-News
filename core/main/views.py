from django.shortcuts import render
from .models import Phone, News
from django.views.generic import ListView
# Create your views here.

class PhoneListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        phones = Phone.objects.all()
        return render(request, self.template_name, {'phones':phones})

class NewsListView(ListView):
    template_name = 'news.html'

    def get(self, request):
        news = News.objects.all()
        return render(request, self.template_name, {'news':news})