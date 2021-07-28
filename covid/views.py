from django.shortcuts import render
from django.http import JsonResponse

from covid.utils.covid import GlobalCases, Countries


def index(request):
    return render(request, template_name='pages/index.html')


def confirmed_count(self):
    data = GlobalCases.confirmed(self)
    return JsonResponse(data)


def death_count(self):
    data = GlobalCases.deaths(self)
    return JsonResponse(data)


def recovered_count(self):
    data = GlobalCases.recovered(self)
    return JsonResponse(data)


def active_count(self):
    data = GlobalCases.active(self)
    return JsonResponse(data)


def death_rate(self):
    data = GlobalCases.death_rate(self)
    return JsonResponse(data)


def recovery_rate(self):
    data = GlobalCases.recovery_rate(self)
    return JsonResponse(data)


def active_percentage(self):
    data = GlobalCases.active_perc(self)
    return JsonResponse(data)


def daily_confirmed(self):
    data = GlobalCases.daily_confirmed(self)
    return JsonResponse(data, safe=False)


def daily_deaths(self):
    data = GlobalCases.daily_deaths(self)
    return JsonResponse(data, safe=False)


def daily_recovered(self):
    data = GlobalCases.daily_recovered(self)
    return JsonResponse(data, safe=False)


def daily_active(self):
    data = GlobalCases.daily_active(self)
    return JsonResponse(data, safe=False)
