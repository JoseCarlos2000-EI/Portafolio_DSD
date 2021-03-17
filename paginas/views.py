from django.shortcuts import render,redirect
from .models import usuario
# Create your views here.
def lisusuario(request):
    arrayu=usuario.objects.all()
    return render(request,'usuario.html',{'usuarios':arrayu})

def agregarusuario(request):
    nombre=request.POST['nombreu']
    correou=request.POST['correo']
    telefonou=request.POST['telefono']
    usuario(usuario=nombre,correo=correou,telefono=telefonou).save()
    return redirect(request.META['HTTP_REFERER'])

def eliminarusuario(request,ide):
    usuario.objects.filter(id=ide).delete()
    return redirect(request.META['HTTP_REFERER'])

def pagina_editar(request,id):
    return render(request,'actualizar_usuario.html',{'id':id})

def actualizar_usu(request,ide):
    arrayu=usuario.objects.all()
   
    nom=request.POST['nombreu']
    corr=request.POST['correous']
    tel=request.POST['telefonou']
    obj=usuario.objects.filter(id=ide)[0]
    obj.usuario=nom
    obj.correo=corr
    obj.telefono=tel
    obj.save()
    return render(request,"usuario.html",{'usuarios':arrayu})