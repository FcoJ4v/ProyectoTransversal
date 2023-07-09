from django.contrib.auth.backends import ModelBackend
from .models import Usuario

class CustomBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        try:
            usuario = Usuario.objects.get(username=username)
            if usuario.contraseña == password:
                return usuario
        except Usuario.DoesNotExist:
            pass



    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
