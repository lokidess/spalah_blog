from django.conf import settings


def lazy_context_processor(request):
    return {
        'some_name': settings
    }
