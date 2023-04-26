from django.urls import path
from .views import PhoneListView, NewsListView

urlpatterns = [
    path('', PhoneListView.as_view(), name='home'),
    path('news/', NewsListView.as_view(), name='news')
]