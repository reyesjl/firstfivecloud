from django.shortcuts import render, redirect
from .models import Event, EventRegistration


def handleCampsRoute(request):
    """
    Displays camps landing page
    """
    context = {"activelink": "camps"}
    return render(request, "camps.html", context)
