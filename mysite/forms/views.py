from django.shortcuts import render,redirect
from .forms import RegistrarUsuario
from .models import Usuarios
# Create your views here.
def index(request):
    mis_usuarios = Usuarios.objects.all()

    if request.method == 'POST':
        register_form = RegistrarUsuario(request.POST)
        if register_form.is_valid():
            success = register_form.registrar_usuario()
            return redirect('./')
    else:
        register_form = RegistrarUsuario()
        return render(request, 'forms/mi_form.html', {'register_form': register_form,'usuarios': mis_usuarios})