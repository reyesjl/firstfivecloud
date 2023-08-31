from django.shortcuts import render

def handleHomeRoute(request):
    """
    Displays firstfiverugby homepage with navigation to our services.
    """
    context = {
        "activelink": "home",
    }
    return render(request, "home.html", context)

def handlePreviewRoute(request, param):
    """
    Displays a preview route for devs to see new content. 
    """
    context = {
        "activelink": param,
    }
    return render(request, "preview.html", context)

def handleAboutRoute(request):
    """
    Displays firtfiverugby about us page.
    """
    context = {
        "activelink": "about",
    }
    return render(request, "about.html", context)

def handleSuccessRoute(request):
    """
    Show success message for the user.
    """
    context = {
        "activelink": "success",
    }
    return render(request, "success.html", context)