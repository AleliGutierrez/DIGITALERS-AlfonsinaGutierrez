from django.db import models

# MODELOS #


# PRODUCTO
class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    inventory = models.PositiveIntegerField(verbose_name='Inventario')
    description = models.TextField(null=True, verbose_name='Descripción')
    cover = models.ImageField(upload_to= 'products', verbose_name='Imagen del producto')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
        
    def __str__(self):
        return self.name
    

# CATEGORIAS/ETIQUETAS
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    product_list = models.ManyToManyField(Product, default=None, blank=True, null=True)
    """created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)"""
    
    class Meta:
        verbose_name='Categorías'
        verbose_name_plural='Categorías'
        
    def __str__(self):
        return self.name


# DOMICILIO-CLIENTE
class Address(models.Model):
    country = models.CharField(max_length=100, verbose_name='País')
    state = models.CharField(max_length=255, verbose_name='Provincia')
    city = models.CharField(max_length=255, verbose_name='Ciudad')
    neighborhood = models.CharField(max_length=255, verbose_name='Barrio')
    street = models.CharField(max_length=255, verbose_name='Calle')
    postal_code = models.CharField(max_length=10, verbose_name='Código postal')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Domicilio'
        verbose_name_plural='Domicilios' 
        
    def __str__(self):
        return f"{self.street}, {self.neighborhood}, {self.city}, {self.state}, {self.country} {self.postal_code}"


# CLIENTE
class Customer(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Nombre')
    last_name = models.CharField(max_length=255, verbose_name='Apellido')
    id_number = models.CharField(max_length=20, verbose_name='DNI', unique=True)
    phone = models.CharField(max_length=20, verbose_name='Teléfono')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, verbose_name='Domicilio', default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"