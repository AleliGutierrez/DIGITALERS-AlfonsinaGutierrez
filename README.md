# DIGITALERS-AlfonsinaGutierrez

El sitio web está destinado a la venta de terrarios a modo decorativo o con el fin de hacer de hogar para una mascota, como peces o animales pequeños.

Usuario Administrador: 
Nombre: admin
Contraseña: admin
Nota: Para probar la opción "Eliminar perfil" crear un nuevo usuario en plataforma con el que hacer la prueba, admin no puede ser eliminado.

Recursos empleados:
- Python 3.7.9
- Django 3.2.22
- Bootstrap 5.3 (se incluyeron componentes extraídos, como el footer y el perfil, desde mdbootstrap.com)
- ​SQLite


Librerías iincluidas
- Django (junto a sus librerías asociadas)
- ​Pillow (junto a sus librerías asociadas)




Objetivo funcional: 

Ofrecerle al usuario registrado la posibilidad de realizar operaciones CRUD en el panel de administración, como así también la posibilidad de recorrer la página a los visitantes de la página.


Funcionalidades: 

- ​Operaciones CRUD: Aplicables a los modelos Product, Tag, Cliente, Domicilio y Perfil. Estas pueden ser realizadas tanto por usuarios registrados en plataforma como los registrados en el panel de administración de Django.
- ​Visualización general de productos o filtrada por categoría y búsqueda.
- Sign up / Log in / Log out.


Modelos: 
- ​Product: Representa al producto. Cuenta con los siguientes atributos: name, price, inventory, description, cover, created, updated.
  
- ​Tag: Representa las categorías y etiquetas relacionadas a los productos. Cuenta con los siguientes atributos: name, product_list(Product/ManyToMany).
  
- Address: Representa el domicilio del cliente. Cuenta con los siguientes atributos: country, state, city, neighborhood, street, postal_code,  created, updated.

- ​Customer: Representa al cliente. Cuenta con los siguientes atributos: first_name, last_name, id_number, phone, address(Address/OneToOne), created, updated.
Nota: Se eliminarán tanto cliente como domicilio, aunque es posible eliminar domicilio sin que afecte al cliente.

- Profile: Representa el perfil del usuario. Cuenta con los siguientes atributos: user(User/OnetoOne), avatar, created, updated.
Nota: De eliminarse el perfil, se eliminara también el usuario asociado (no aplica a admin).

