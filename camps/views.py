from django.shortcuts import render


def handleWelcome(request):
    """
    Displays camps landing page
    """
    context = {"activelink": "camps"}
    return render(request, "events/welcome.html", context)
