from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        pass
        
    return HttpResponse()
