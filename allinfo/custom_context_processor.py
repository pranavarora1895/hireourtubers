from .models import Allinfo

def info_renderer(request):
    return {
        'all_info': Allinfo.objects.all(),
    }
