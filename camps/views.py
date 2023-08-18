from django.shortcuts import render, redirect
from .models import Event, EventRegistration
from datetime import datetime


def handleCampsRoute(request):
    """
    Displays camps landing page
    """
    upcoming_camps = Event.objects.filter(start_date__gte=datetime.now()).order_by('start_date')
    expired_camps = Event.objects.filter(start_date__lt=datetime.now()).order_by('-start_date')

    return render(request, "camps.html", {'activelink': 'camps', 'upcoming_camps': upcoming_camps, 'expired_camps': expired_camps})
