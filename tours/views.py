from django.shortcuts import render, redirect
from .models import Event, EventInqueries


def handleToursRoute(request):
    """
    Displays tours landing page and handles registration for camp event.
    """
    if request.method == "POST":
        ''' inquery request
        # Get form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        event_id = request.POST.get("event_id")

        # Retrieve the event based on the event_id
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            # If the event does not exist, redirect to error page
            # (or handle this case however you want)
            return redirect("error_page")

        # Create the EventInqueries
        event_inqueries = EventInqueries(name=name, email=email, phone=phone)
        event_inqueries.save()
        event_inqueries.events.add(event)
        '''

        # Redirect to success page
        return redirect("home")
    context = {"activelink": "tours"}
    return render(request, "tours.html", context)
