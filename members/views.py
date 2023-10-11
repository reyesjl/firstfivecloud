from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def handleSignupUser(request):
  """
  Sign up user to platform.
  """
  context = {
    'activelink': 2,
  }
  return render(request, 'members/signup.html', context)

def handleLoginUser(request):
  """
  Log a user into the system.
  """
  context = {
    "activelink": 2,
  }

  if request.method == "POST":
    username = request.POST['username']  
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, ('User is authenticated.'))
      return redirect('home')
    else:
      messages.success(request, ('User is NOT authenticated.'))
      return redirect('login')
  else:
    return render(request, 'members/login.html', context)
  
def handleLogoutUser(request):
  """
  Log a user out of the system.
  """
  logout(request)
  messages.success(request, ('User has been authenticated.'))
  return redirect('members/logout.html')