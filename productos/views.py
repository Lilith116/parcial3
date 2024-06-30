from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Genero, Producto, ProductoCarro

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

def Productos(request):
    context={}
    return render(request,'productos/Productos.html', context)

def ShoppingCart(request):
    context={}
    return render(request,'productos/ShoppingCart.html', context)

def crud(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'productos/Clientes_list.html', context)

def clientesadd(request):
    if request.method is not "POST":
        
        generos=Genero.objects.all()
        context={'generos':generos}
        return render (request, 'productos/clientes_add.html', context)
    
    else:
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"] 
        genero=request.POST["genero"]
        telefono = request.POST["telefono"] 
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"
        
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
                                    activo=1 )
        obj.save()
        context={'mensaje': "Ok, datos grabados..."}
        return render(request,'productos/Clientes_add.html',context)
        

def clientes_del(request, pk):
    context={}
    try:
        cliente=Cliente.objects.get(rut=pk)
        
        cliente.delete()
        mensaje="Bien, datos eliminados..."
        clientes = Cliente.objects.all()
        context = { 'clientes': clientes, 'mensaje': mensaje}
        return render(request, 'alumnos/alumnos_list.html', context) 
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
        
def clientesUpdate(request):
    
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
    

def agregar_al_carro(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    item_producto, created = ProductoCarro.objects.get_or_create(producto=producto)
    if not created:
        item_producto.cantidad += 1
    item_producto.save()
    return redirect('vista_carro')
    
    
def vista_carro(request):
    item_producto = ProductoCarro.objects.all()
    total= sum(item.precio_total() for item in item_producto)
    return render(request, 'productos/ShoppingCart.html', {'item_producto': item_producto, 'total': total })

def quitar_del_carro(request, item_producto_id):
    item_producto = get_object_or_404(ProductoCarro, id=item_producto_id )
    item_producto.delete()
    return(vista_carro)
    
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html',{'productos': productos}) 

        
        