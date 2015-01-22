import os
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse



# Default Landing Page loader for Jiffy
def home(request):
    templ = get_template('index.html')
    html = templ.render(Context())
    return HttpResponse(html)
