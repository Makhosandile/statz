from django.urls import path
from covid import views

urlpatterns = [
    path('', views.index, name='home'),
    path('confirmed_count', views.confirmed_count, name="confirmed_count"),
    path('active_count', views.active_count, name="active_count"),
    path('death_count', views.death_count, name="death_count"),
    path('recovered_count', views.recovered_count, name="recovered_count"),
    path('recovery_rate', views.recovery_rate, name="recovery_rate"),
    path('death_rate', views.death_rate, name="death_rate"),
    path('active_percentage', views.active_percentage, name="active_percentage"),
    path('daily_confirmed', views.daily_confirmed, name="daily_confirmed"),
    path('daily_deaths', views.daily_deaths, name="daily_deaths"),
    path('daily_recovered', views.daily_recovered, name="daily_recovered"),
    path('daily_active', views.daily_active, name="daily_active"),
]
