from django.http import JsonResponse, HttpResponseForbidden

class GroupRequiredMixin:
    def __init__(self, group_name):
        self.group_name = group_name

    def __call__(self, view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=self.group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'error': 'Permesso negato a questa pagina, effettua l\'iscrizione per potervi accedere.'}, status=403)
                else:
                    return HttpResponseForbidden("Permesso negato a questa pagina, effettua l'iscrizione per potervi accedere.")

        return _wrapped_view