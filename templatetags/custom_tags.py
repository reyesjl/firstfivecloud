from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def banner_component(title, image_url, link_display_text, url_name, *args, **kwargs):
  # If the url has parameters, they will be passed in above.
  # This reverse function will build the {% url 'url_name' %} 
  # string for the href attribute.

  link = reverse(url_name, args=args, kwargs=kwargs)
  return f'''
    <div class="banner" style="background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('{image_url}')">
      <h2 class="banner_title">{title}</h2>
      <div class="pair_links">
        <a class="button-link light" href="{link}"><span id="link_text">{link_display_text}</span></a>
      </div>
    </div>
  '''

