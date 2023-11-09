from django.shortcuts import redirect, render
from django.core.mail import send_mail
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

        # Send a confirmation email
        subject = 'Caps inquiry confirmation'
        message = f"""Hey there {caps_inquiry.team_name},

      Your caps order was submitted successfully. A representative will be reaching out shortly.

      Have a great day, and thank you for your interest in team caps.
      
      First Five Rugby
      www.firstfiverugby.com
      letusknow@firstfiverugby.com
        """
        from_email = 'firstfiverugby@gmail.com'  # Replace with your email
        recipient_list = [caps_inquiry.email]
        send_mail(
          subject,
          message,
          from_email,
          recipient_list,
          fail_silently=False,
        )
        
        # Add any additional logic or redirection here
        return redirect('success_caps')  # Redirect to a success page or another appropriate URL
    else:
      form = CapsInquiryForm()

    return render(request, 'capsform.html', {'form': form})

def handleCapsSuccess(request):
  return render(request, 'success.html', {})
