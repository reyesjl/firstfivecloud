from django.shortcuts import render


def handleToursLanding(request):
    """
    Displays tours landing page
    """
    context = {"activelink": "tours"}
    return render(request, "tours_welcome.html", context)
