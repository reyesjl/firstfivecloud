from django.shortcuts import render, redirect
from .models import ToursInqueries


def handleToursRoute(request):
    """
    Displays tours landing page and handles registration for camp event.
    """
    if request.method == "POST":
        # Get form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        # create the wrs catalog inquery
        ti = ToursInqueries(name=name, email=email, phone=phone)
        ti.save()

        # Send email to this user and to admins
        # .... coming soon .... 5v.0.1

        # Redirect to success page
        return redirect("success")

    context = {"activelink": "tours"}
    return render(request, "tours.html", context)

def handleInsuranceRoute(request):
    """
    Display insurance page. Globetrotter insurance.
    """
    context = {"activelink": "tours"}
    return render(request, "globetrotter.html", context)
