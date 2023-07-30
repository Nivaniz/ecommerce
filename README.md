# Ecommerce  
<p align="center">
  <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Logo.png" alt="Logo" style="width: 30%; max-width: 200px;">
</p>
<h5 align="center">ByteShop: Tu destino para compras online</h5>

ByteShop es un proyecto de e-commerce desarrollado en Django, que ofrece una experiencia de compra en línea dinámica y completa. Descubre una amplia variedad de productos, gestiona tus compras y maneja tu cuenta a tu gusto, todo en un sitio web intuitivo y fácil de usar.

## ¿En qué consiste?

Este proyecto es un e-commerce desarrollado en Django, un potente Framework de Python. El entorno virtual se ha configurado cuidadosamente para asegurar una experiencia de desarrollo óptima y segura. La tecnología utilizada incluye Python, JavaScript, HTML, Bootstrap/CSS, jQuery y MySQL. Todas las páginas del sitio web son dinámicas y ofrecen una experiencia interactiva a los usuarios.

## Características destacadas

- Administrador
  * Agregar nuevos productos con información detallada, incluyendo nombre, categoría, imagen, precio, stock y disponibilidad.
  * Gestionar las reviews de compradores previamente verificados, permitiendo visualizar el usuario que realizó la compra, su calificación, su reseña y el producto     evaluado.
  * Ver las órdenes de productos, mostrando el número de orden, nombre del cliente, teléfono, email, ciudad, costo total, impuestos, estado y fecha de la orden.
  * Acceder a información sobre los pagos de compras, incluyendo el usuario, PaymentID, método de pago, cantidad y estado de la transacción.
  * Visualizar los productos solicitados por los clientes, junto con detalles como el pago, costo, usuario y variaciones del producto.

- Categorías
  * Agregar nuevas categorías para clasificar los productos y facilitar la navegación y búsqueda de los usuarios.

- Carritos de compra
  * Los usuarios pueden acceder a su carrito de compra, identificado por un cartID único.
  * La sección "CartItems" muestra los elementos presentes en el carrito, incluyendo los productos seleccionados, el ID del carrito, la cantidad de cada producto y 
    su disponibilidad.

- Gestión de cuentas
  * Utiliza el sistema de grupos proporcionado por Django para asignar roles con características específicas para el manejo del sistema.

- Usuarios
  * Los perfiles de usuarios contienen información relevante, como la imagen de perfil, nombre de usuario, país, ciudad y código postal.

- Cuentas
  * Sección que muestra información sobre las cuentas de los usuarios, incluyendo email, primer nombre, último nombre, nombre de usuario, última vez que se      conectó, fecha de registro y estado de la cuenta (activa o pendiente de confirmación por correo).
 
<p align="center">
  <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Main_Page.png" alt="Main Page" style="width: 50%; max-width: 200px;">
</p>

## Ejecución 

Es necesario tener instalado los requerimientos necesarios para ejecutarlo posteriormente con `python manage.py runserver` desde la terminal en el directorio de la carpeta clonada. Una vez realizado es necesario abrir localhost:8000 para visualizar el sistema.

### Instalación

Para poder utilizar el proyecto o modificarlo puedes:

1.- **Clonar el repositorio en tu máquina local:**
`git clone https://github.com/Nivaniz/ecommerce.git`
*(Hay que tener todos los requerimientos previamente instalados)*

2.- **Crea un entorno virtual e instala las dependencias necesarias.**

3.- **Configura la base de datos y realiza las migraciones.**

4.- **Ejecuta el servidor de desarrollo de Django.**

5.- **Navegar en el directorio del proyecto:**
`cd ecommerce`

6.- **Instalar las dependencias necesarias:**
`pip install -r requirements.txt`

~~~
git clone https://github.com/tu-usuario/ecomerce.git
cd ecommerce
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
~~~

## Uso y cómo acceder al administrador

Para acceder al área de administración, sigue los siguientes pasos:

El sistema mediante el cual se maneja con localhost:8000/securelogin, para poder acceder a la ventana de administrador necesitas crear una cuenta desde la CMD o BASH utilizando `winpty python manage.py createsuperuser` para crear super usuario.

<p align="center">
  <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Django-Main.png" alt="Main Django" style="width: 50%; max-width: 200px;">
</p>

### Ventanas del E-commerce

La mayoría de las ventanas se pueden acceder sin tener una cuenta, pero para comprar y ver pedidos es necesario crear una.
  
- Registro e Inicio de Sesión:
El sistema ofrece a los usuarios la posibilidad de registrarse y crear una cuenta utilizando su correo electrónico de Gmail. La cuenta se verifica mediante un proceso de codificación en Base64 para mayor seguridad. Además, los usuarios registrados pueden iniciar sesión fácilmente para acceder a todas las funcionalidades del sitio.

<p align="center">
   <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Inicio_Sesión.png" alt="Inicio de Sesión" style="width: 40%;">
    <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Registrarme.png" alt="Registrarme" style="width: 40%;">
 <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Correo.png" alt="Activar Cuenta" style="width: 40%;">
</p>

- Sección de Olvidé mi Contraseña:
En caso de que los usuarios olviden su contraseña, el e-commerce cuenta con una sección dedicada para restablecerla de forma segura. Los usuarios recibirán un correo electrónico con instrucciones para recuperar su contraseña y volver a acceder a su cuenta.

<p align="center">
   <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Olvide_Contraseña.png" alt="Olvidé Contraseña" style="width: 40%;">
   <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Recuperar.png" alt="Recuperar Cuenta" style="width: 40%;">
</p>

- Sección de Categorías:
La navegación y búsqueda de productos se simplifica gracias a la sección de categorías. Los usuarios pueden explorar y filtrar productos por categorías específicas, lo que facilita la búsqueda de artículos de su interés.

<p align="center">
  <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Tienda_Main.png" alt="Tienda" style="width: 50%; max-width: 200px;">
</p>

- Apartado de Búsqueda de Productos:
Para una experiencia de compra más ágil, el e-commerce proporciona un apartado de búsqueda de productos. Los usuarios pueden ingresar palabras clave y encontrar rápidamente los productos que desean comprar.

- Apartado de Mi Cuenta:
Los usuarios tienen acceso a su área personal a través del apartado "Mi Cuenta". Aquí, pueden ver el historial de sus pedidos, revisar sus ordenes de compra anteriores, cambiar su contraseña para garantizar la seguridad y editar su perfil para mantener su información actualizada.

<p align="center">
   <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Mi_Panel.png" alt="Mi panel" style="width: 40%;">
   <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Orden_De_Compra.png" alt="Mis pedidos" style="width: 40%;">
</p>

<p align="center">
   <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Editar_Perfil.png" alt="Editar Cuenta" style="width: 40%;">
   <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Cambiar_Contraseña.png" alt="Editar constraseña" style="width: 40%;">
</p>

- Carrito:
El carrito de compra es una funcionalidad esencial en el e-commerce. Los usuarios pueden agregar productos seleccionados a su carrito, ver el resumen de sus compras y ajustar las cantidades antes de proceder al pago.

<p align="center">
   <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Carrito.png" alt="Carrito" style="width: 40%;">
</p>

- Dirección de Envío:
Antes de finalizar la compra, los usuarios pueden proporcionar y verificar su dirección de envío para garantizar que los productos sean entregados correctamente.

<p align="center">
   <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Dirección_Envio.png" alt="Dirección de Envio" style="width: 40%;">
</p>

- Pagar:
El proceso de pago se lleva a cabo en una ventana dedicada, donde los usuarios pueden seleccionar el método de pago preferido y completar la transacción de forma segura.

<p align="center">
   <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Pagar.png" alt="Pago" style="width: 40%;">
</p>

- Ventana de Venta Exitosa
Una vez completada la transacción, los usuarios recibirán una ventana de venta exitosa que confirmará su compra y proporcionará detalles importantes, como el número de orden y la fecha estimada de entrega.

<p align="center">
   <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Completed.png" alt="Compra exitosa" style="width: 40%;">
   <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Cuenta_Pagado.png" alt="Cuenta Pagado" style="width: 40%;">
</p>

<p align="center">
   <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Cuenta_Recibido.png" alt="Cuenta Recibido" style="width: 40%;">
   <img src="https://github.com/Nivaniz/ecommerce/blob/main/img-git/Compra_Correo.png" alt="Correo de Compra" style="width: 40%;">
</p>

## Notas

Por cuestiones de seguridad la funcionalidad de SECRET_KEY, y contraseñas especificas de correo como EMAIL_HOST_USER / PASSWORD están privadas en un archivo local .env. Es necesario que si quieres utilizarlo insertes tus credenciales necesarias para el correcto funcionamiento de la página accediendo a settings con contraseñas de acceso de los servicios de google gmail.

Para ver y realizar los págos por Paypal o tarjetas de crédito/débito (VISA) es necesario utilizar un Sandbox desde Paypal y tener una cuenta como desarrollador.

## Autoría

¡Tus contribuciones son bienvenidas! Si encuentras errores o mejoras para el proyecto, no dudes en enviar tus pull requests. Si tienes alguna pregunta o comentario, puedes encontrarme y visitar mi sitio web https://codingwithnirvana.pythonanywhere.com.

Espero que esta versión del README sea útil.
Creado por **Nirvana Belen González López** 
