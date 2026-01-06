from .models import *
import datetime

def extras(request):
    context={
        'current_year': datetime.datetime.now().year,
        'setting': GeneralSettings.objects.first(),
    }
    return context