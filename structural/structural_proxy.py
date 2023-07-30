"""
Structural pattern Proxy

El patrón Proxy es un patrón de diseño estructural que actúa como intermediario o sustituto de otro objeto. El objetivo 
del patrón Proxy es controlar el acceso a un objeto y proporcionar una representación o funcionalidad adicional, como el 
almacenamiento en caché, la verificación de permisos o la carga diferida. En resumen, el Proxy se utiliza para agregar 
una capa de control entre el cliente y el objeto real.

Imagina que tienes una clase ObjetoReal que es costosa de crear o inicializar. En lugar de crear directamente una 
instancia de ObjetoReal, puedes utilizar un objeto Proxy que maneje la creación y la interacción con ObjetoReal. De esta 
manera, puedes retrasar la creación del objeto real hasta que sea realmente necesario o realizar alguna operación 
adicional antes o después de acceder al objeto real.

Ejemplo en Python:

Supongamos que tenemos una clase Imagen que representa una imagen que se carga desde el disco. Queremos utilizar un 
proxy para cargar la imagen desde el disco solo cuando se solicite y no antes.

"""
# Clase base: Interfaz de la imagen
class Imagen:
    def mostrar(self):
        pass

# Clase concreta: ObjetoReal (Imagen real)
class ImagenReal(Imagen):
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.cargar_desde_disco()

    def cargar_desde_disco(self):
        print(f"Cargando imagen desde el disco: {self.ruta_archivo}")

    def mostrar(self):
        print(f"Mostrando imagen: {self.ruta_archivo}")

# Clase Proxy: ProxyImagen
class ProxyImagen(Imagen):
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.imagen_real = None

    def cargar_desde_disco(self):
        if self.imagen_real is None:
            self.imagen_real = ImagenReal(self.ruta_archivo)

    def mostrar(self):
        self.cargar_desde_disco()
        self.imagen_real.mostrar()

"""
En este ejemplo, tenemos una clase ImagenReal que representa la imagen real que se carga desde el disco. El proxy, 
ProxyImagen, es una clase que actúa como intermediario entre el cliente y la imagen real.

El proxy ProxyImagen contiene una referencia a ImagenReal y carga la imagen real desde el disco solo cuando es 
necesario, es decir, cuando se invoca el método mostrar(). Esto se realiza en el método cargar_desde_disco() del proxy. 
De esta manera, el cliente interactúa con el proxy, que a su vez maneja la interacción con el objeto real.

Ahora podemos utilizar el proxy para mostrar la imagen:
"""

# Crear el proxy con la ruta de archivo de la imagen
proxy_imagen = ProxyImagen("imagen.png")

# La imagen real aún no se ha cargado desde el disco
# La carga real se produce solo cuando se llama a 'mostrar()'
proxy_imagen.mostrar()
# Output: Cargando imagen desde el disco: imagen.png
#         Mostrando imagen: imagen.png

# La imagen real ya se ha cargado, la carga no se produce nuevamente
proxy_imagen.mostrar()
# Output: Mostrando imagen: imagen.png

"""
En este ejemplo, hemos utilizado el proxy ProxyImagen para cargar la imagen real desde el disco solo cuando se llama al 
método mostrar(). Si el cliente no utiliza la imagen, no se carga desde el disco, lo que puede mejorar el rendimiento y 
la eficiencia en situaciones donde cargar la imagen es costoso.

En resumen, el patrón Proxy se utiliza para controlar el acceso a un objeto y proporcionar una representación o 
funcionalidad adicional. El proxy actúa como intermediario y puede ayudar a mejorar el rendimiento y la eficiencia al 
retrasar la creación o carga del objeto real hasta que sea necesario.
"""