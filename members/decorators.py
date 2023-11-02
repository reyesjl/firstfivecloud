from functools import wraps
from django.http import HttpResponseForbidden

def coach_required(view_func):
  @wraps(view_func)
  def _wrapped_view(request, *args, **kwargs):
    if request.user.groups.filter(name='coach').exists():
      return view_func(request, *args, **kwargs)
    else:
      return HttpResponseForbidden("Access denied. You must be a coach to access this page.")
  return _wrapped_view
  
      