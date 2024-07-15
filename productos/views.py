from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Cliente, Genero, Producto
from productos.Carrito import Carrito
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.

def index(request):
    context={}
    return render(request,'productos/index.html', context)

def About(request):
    context={}
    return render(request,'productos/About.html', context)

def Adopciones(request):
    context={}
    return render(request,'productos/Adopciones.html', context)


def ShoppingCart(request):
    context={}
    return render(request,'productos/ShoppingCart.html', context)

def crud(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'productos/Clientes_list.html', context)

def clientes_add(request):
    if request.method is not "POST":
        
        generos=Genero.objects.all()
        context={'generos':generos}
        return render (request, 'productos/clientes_add.html', context)
    
    else:
        rut=request.POST.get["rut"]
        nombre=request.POST.get["nombre"]
        aPaterno=request.POST.get["paterno"]
        aMaterno=request.POST.get["materno"]
        fechaNac=request.POST.get["fechaNac"] 
        genero=request.POST.get["genero"]
        telefono = request.POST.get["telefono"] 
        email=request.POST.get["email"]
        direccion=request.POST.get["direccion"]
        activo= 1
        
        
        objGenero=Genero.objects.get(id_genero = genero) 
        obj=Cliente.objects.create( rut=rut,
                                    nombre=nombre,
                                    apellido_paterno=aPaterno,
                                    apellido_materno=aMaterno,
                                    fecha_nacimiento=fechaNac,
                                    id_genero=objGenero,
                                    telefono=telefono,
                                    email=email,
                                    direccion=direccion,
                                    activo=activo )
        obj.save()
        context={'mensaje': "Ok, datos grabados..."}
        return render(request,'productos/clientes_add.html',context)
        

def clientes_del(request, pk):
    context={}
    try:
        cliente=Cliente.objects.get(rut=pk)
        
        cliente.delete()
        mensaje="Bien, datos eliminados..."
        clientes = Cliente.objects.all()
        context = { 'clientes': clientes, 'mensaje': mensaje}
        return render(request, 'productos/Clientes_list.html', context) 
    except:
        mensaje="Error, rut no existe..."
        clientes = Cliente.objects.all()
        context = {'clientes': clientes, 'mensaje': mensaje}
        return render(request, 'productos/Clientes_list.html', context)
    


def clientes_findEdit(request, pk):
    if pk != "":
        cliente=Cliente.objects.get(rut=pk) 
        generos=Genero.objects.all()
        
        print(type (cliente.id_genero.genero))
        
        context={'cliente': cliente, 'generos': generos}
        if cliente:
            return render(request, 'productos/Clientes_edit.html', context)
        else:
            context={ 'mensaje': "Error, rut no existe..."}
            return render (request, 'productos/Cliente_list.html', context)
        
def clientes_Update(request):
    
    if request.method is not "POST":
        
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request. POST["genero"]
        telefono = request.POST["telefono"] 
        email=request.POST["email"]
        direccion=request.POST["direccion"] 
        activo="1"
        
        objGenero=Genero.objects.get(id_genero = genero)
        
        cliente = Cliente()
        cliente.rut=rut
        cliente.nombre=nombre
        cliente.apellido_paterno=aPaterno
        cliente.apellido_materno=aMaterno
        cliente.fecha_nacimiento=fechaNac
        cliente.id_genero=objGenero
        cliente.telefono-telefono
        cliente.email=email
        cliente.direccion-direccion
        cliente.activo=1
        cliente.save()
        
        generos=Genero.objects.all()
        context={'mensaje':"Ok, datos actualizados..",'generos':generos,'cliente':cliente}
        return render(request, 'productos/Clientes_edit.html', context)
    else:
        clientes = Cliente.objects.all()
        context={'clientes',clientes}
        return render(request,'productos/Clientes_list.html',context)
    

def tienda(request):
    productos = Producto.objects.all()
    agregado = request.GET.get('agregado', False)
    return render(request, "productos/tienda.html",{'productos':productos,'agregado': agregado})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect(reverse('productos')+ '?agregado=true')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id= producto_id)
    carrito.eliminar(producto)
    return redirect(reverse('shopping_cart')+ '?accion=eliminado')
    
def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id= producto_id)
    carrito.restar(producto)
    return redirect(reverse('shopping_cart')+'?accion=restado')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect(reverse('shopping_cart')+ '?accion=limpiado')



def shopping_cart(request):
    carrito = Carrito(request)
    productos = carrito.obtener_productos()
    accion = request.GET.get('accion', None)
    return render(request, 'productos/ShoppingCart.html', {'productos': productos, 'accion': accion})

    
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"] )
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="productos")
        data["form"] = formulario
    
    return render(request, 'registration/registro.html', data)


