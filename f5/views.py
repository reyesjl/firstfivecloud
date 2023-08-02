from django.shortcuts import render

def handleLandingPage(request):
    """
    Displays firstfiverugby landing page. Countdown.
    """
    context = {"activelink": "home"}
    return render(request, "landing.html", context)


def handleHomeRoute(request):
    """
    Displays firstfiverugby homepage with navigation to our services.
    """
    context = {
        "activelink": "home",
    }
    return render(request, "index.html", context)


def handleAboutRoute(request):
    """
    Displays firtfiverugby about us page.
    """
    context = {
        "activelink": "about",
    }
    return render(request, "about.html", context)

def handleDownRoute(request):
    """
    Displays down page for the platform.
    """
    context = {
        "banner": "Exclusive direct team deals on all WRS catalog items for games, traning, events, and even travel gear."
    }
    return render(request, "down.html", context)

def handleHelpRoute(request):
    """
    Displays our help page.
    """
    context = {
        "activelink": "catalog"
    }