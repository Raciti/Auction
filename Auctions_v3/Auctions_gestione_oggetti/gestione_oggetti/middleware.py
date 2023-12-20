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


import jwt
from django.conf import settings

class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        authorization_header = request.headers.get('Authorization')

        if authorization_header and authorization_header.startswith('Bearer '):
            token = authorization_header.split(' ')[1]

            try:
                decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                request.user = {'id': decoded_token['user_id']}
            except jwt.ExpiredSignatureError:
                return JsonResponse({'error': 'Token has expired'}, status=403)
            except jwt.InvalidTokenError:
                return JsonResponse({'error': 'Invalid token'}, status=403)

        response = self.get_response(request)
        return response
