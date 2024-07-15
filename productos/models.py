from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut                      = models.CharField(primary_key=True, max_length=10)
    nombre                   = models.CharField(max_length=20)
    apellido_paterno         = models.CharField(max_length=20)
    apellido_materno         = models.CharField(max_length=20)
    fecha_nacimiento         = models.DateField(blank=False, null=False)
    id_genero                = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero')
    telefono                 = models.CharField(max_length=45)
    email                    = models.EmailField(unique=True, max_length=100, blank=True, null=False)
    direccion                = models.CharField(max_length=50, blank=True, null=False)
    activo                   = models.IntegerField()
    
    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)   

    
class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)
    
class Producto(models.Model):
    nombre = models.CharField(max_length=64)       
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    image = models.ImageField(default='fallback.png', blank=True)
    
    
    
    
    def __str__(self):
        return f'{self.nombre} -> {self.precio}'



