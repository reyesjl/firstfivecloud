from django.shortcuts import render

# Create your views here.

def handleSchedulesRoute(request):
  context = {"activelink":"scheudles"}
  return render(request, "schedules.html", context)
