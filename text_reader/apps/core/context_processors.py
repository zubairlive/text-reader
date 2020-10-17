from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site


def site_processor(request):
    """
    Provide basic settings across all project.
    """
    return {
        'site': get_current_site(request),
        'settings': settings,
    }
