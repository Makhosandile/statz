from django.urls import path
from covid import views


urlpatterns = [
    path('', views.index, name='home'),
]
