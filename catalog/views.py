from django.shortcuts import render, redirect
from django.contrib import messages
from .models import HonorCapsInqueries


def handleCatalogRoute(request):
    """
    Display the catalog
    """
    context = {"activelink": "catalog"}
    return render(request, "catalog.html", context)


def handleCapsRoute(request):
    if request.method == "POST":
        # Get form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        # create the wrs catalog inquery
        hci = HonorCapsInqueries(name=name, email=email, phone=phone)
        hci.save()

        # Send email to this user and to admins
        # .... coming soon .... 5v.0.1

        # Redirect to success page
        return redirect("success")
    context = {"activelink": "catalog"}
    return render(request, "caps.html", context)

def handleAuctionRoute(request):
    context = {"activelink": "catalog"}
    return render(request, "auction.html", context)