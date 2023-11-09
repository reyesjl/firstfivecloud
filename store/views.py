from django.shortcuts import redirect, render
from .forms import CapsInquiryForm

# Create your views here.

def handleStoreRoute(request):
  """
  Returns the store page.
  """
  context = {
    "activelink": 4,
  }
  return render(request, "store.html", context)

def handleCapsInquiry(request):
    if request.method == 'POST':
        form = CapsInquiryForm(request.POST)
        if form.is_valid():
            caps_inquiry = form.save()
            # Add any additional logic or redirection here
            return redirect('success_page')  # Redirect to a success page or another appropriate URL
    else:
        form = CapsInquiryForm()

    return render(request, 'capsform.html', {'form': form})
