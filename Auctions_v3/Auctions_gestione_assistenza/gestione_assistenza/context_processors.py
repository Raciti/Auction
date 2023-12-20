from .models import Quest

def ultimo_elemento(request):
    ultimo_elemento = Quest.objects.last()
    return {'ultimo_elemento': ultimo_elemento}
