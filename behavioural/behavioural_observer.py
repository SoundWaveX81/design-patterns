"""
Behavioural pattern Observer

El patrón Observer es un patrón de diseño de comportamiento que permite que un objeto (llamado sujeto o observable) 
notifique a otros objetos (llamados observadores) sobre cualquier cambio de estado que ocurra en el sujeto. De esta 
manera, los observadores pueden reaccionar y tomar acciones basadas en los cambios del sujeto sin acoplarse directamente 
a él.

El Observer es útil cuando tienes una relación uno a muchos entre objetos, es decir, un objeto (el sujeto) tiene muchos 
dependientes (los observadores) que deben ser notificados cuando el estado del sujeto cambia.

Ejemplo en Python:

Supongamos que tenemos un sistema de noticias en el que hay una clase NotificadorNoticias que actúa como el sujeto y 
diferentes clases que representan las fuentes de noticias (los observadores). Cuando una nueva noticia es publicada, 
el NotificadorNoticias notifica a todas las fuentes de noticias registradas sobre la nueva noticia.
"""
# Clase Observador (Observer)
class FuenteNoticias:
    def actualizar(self, noticia):
        pass

# Clase Sujeto (Observable)
class NotificadorNoticias:
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def eliminar_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, noticia):
        for observador in self.observadores:
            observador.actualizar(noticia)

    def publicar_noticia(self, noticia):
        print(f"Noticia publicada: {noticia}")
        self.notificar_observadores(noticia)

# Implementación concreta de observador (Fuente de Noticias)
class FuenteNoticiasABC(FuenteNoticias):
    def actualizar(self, noticia):
        print(f"Noticia recibida en ABC: {noticia}")

# Implementación concreta de observador (Fuente de Noticias)
class FuenteNoticiasBBC(FuenteNoticias):
    def actualizar(self, noticia):
        print(f"Noticia recibida en BBC: {noticia}")

# Ejemplo de uso del patrón Observer
notificador = NotificadorNoticias()

fuente_abc = FuenteNoticiasABC()
fuente_bbc = FuenteNoticiasBBC()

notificador.agregar_observador(fuente_abc)
notificador.agregar_observador(fuente_bbc)

notificador.publicar_noticia("¡Nuevo avance científico!")
# Output:
# Noticia publicada: ¡Nuevo avance científico!
# Noticia recibida en ABC: ¡Nuevo avance científico!
# Noticia recibida en BBC: ¡Nuevo avance científico!

"""
En este ejemplo, tenemos la clase FuenteNoticias que actúa como el observador y define un método actualizar() que será 
llamado por el sujeto cuando haya una nueva noticia.

Luego, tenemos la clase NotificadorNoticias, que actúa como el sujeto y mantiene una lista de observadores registrados. 
Tiene métodos para agregar, eliminar y notificar a los observadores.

Después, creamos dos clases concretas FuenteNoticiasABC y FuenteNoticiasBBC, que son fuentes de noticias específicas y 
heredan de FuenteNoticias para implementar el método actualizar().

Finalmente, creamos una instancia del NotificadorNoticias y agregamos las instancias de las fuentes de noticias 
(FuenteNoticiasABC y FuenteNoticiasBBC) como observadores. Luego, cuando se publica una nueva noticia, el 
NotificadorNoticias notifica a todos los observadores registrados y estos reaccionan imprimiendo la noticia recibida.

En resumen, el patrón Observer es útil cuando necesitas establecer una relación uno a muchos entre objetos, permitiendo 
que los observadores sean notificados automáticamente sobre los cambios del sujeto sin acoplarse directamente a él. Esto 
facilita la extensibilidad y la reutilización del código, ya que puedes agregar nuevos observadores sin modificar el 
código del sujeto.
"""