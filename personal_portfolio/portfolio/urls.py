from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.index_page_view, name='index_page'),
]
