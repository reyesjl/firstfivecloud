from django.shortcuts import render

# Create your views here.

def handleStoreRoute(request):
  """
  Returns the store page.
  """
  context = {
    "activelink": 4,
  }
  return render(request, "store.html", context)
