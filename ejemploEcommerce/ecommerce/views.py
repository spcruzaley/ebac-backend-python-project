from django.http import JsonResponse

def vista_hola_mundo(request):
    data = {
        "message": "Hola, Mundo !!!"
    }
    return JsonResponse(data)
