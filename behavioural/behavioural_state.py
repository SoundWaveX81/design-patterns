"""
Behavioural pattern State

El patrón State (Estado) es un patrón de diseño de comportamiento que permite que un objeto cambie su comportamiento 
cuando su estado interno cambia. Este patrón se basa en la idea de representar diferentes estados del objeto como clases 
separadas y permitir que el objeto cambie de una clase de estado a otra conforme cambie su estado interno.

El patrón State es útil cuando un objeto tiene diferentes comportamientos según su estado, y estos comportamientos 
pueden cambiar en tiempo de ejecución.

Ejemplo en Python:

Supongamos que tenemos una clase ReproductorMusica que puede reproducir música. Queremos que el reproductor tenga 
diferentes estados, como "Reproduciendo", "En pausa" y "Detenido", y que pueda cambiar su comportamiento dependiendo de 
su estado.
"""

# Interfaz de Estado
class EstadoReproductorMusica:
    def reproducir(self):
        pass

    def pausar(self):
        pass

    def detener(self):
        pass

# Implementación concreta de Estado (Reproduciendo)
class EstadoReproduciendo(EstadoReproductorMusica):
    def reproducir(self):
        print("El reproductor ya está reproduciendo música.")

    def pausar(self):
        print("Pausando la reproducción.")
        return EstadoPausa()

    def detener(self):
        print("Deteniendo la reproducción.")
        return EstadoDetenido()

# Implementación concreta de Estado (En pausa)
class EstadoPausa(EstadoReproductorMusica):
    def reproducir(self):
        print("Reanudando la reproducción.")
        return EstadoReproduciendo()

    def pausar(self):
        print("El reproductor ya está en pausa.")

    def detener(self):
        print("Deteniendo la reproducción.")
        return EstadoDetenido()

# Implementación concreta de Estado (Detenido)
class EstadoDetenido(EstadoReproductorMusica):
    def reproducir(self):
        print("Iniciando la reproducción.")
        return EstadoReproduciendo()

    def pausar(self):
        print("El reproductor está detenido y no se puede pausar.")

    def detener(self):
        print("El reproductor ya está detenido.")

# Clase Contexto (ReproductorMusica)
class ReproductorMusica:
    def __init__(self):
        self.estado_actual = EstadoDetenido()

    def cambiar_estado(self, nuevo_estado):
        self.estado_actual = nuevo_estado

    def reproducir(self):
        self.estado_actual.reproducir()

    def pausar(self):
        self.estado_actual.pausar()

    def detener(self):
        self.estado_actual.detener()

# Ejemplo de uso del patrón State
reproductor = ReproductorMusica()

reproductor.reproducir()  # Output: Iniciando la reproducción.
reproductor.pausar()  # Output: El reproductor está detenido y no se puede pausar.

reproductor.cambiar_estado(EstadoReproduciendo())
reproductor.reproducir()  # Output: El reproductor ya está reproduciendo música.
reproductor.pausar()  # Output: Pausando la reproducción.
reproductor.detener()  # Output: Deteniendo la reproducción.


"""
En este ejemplo, tenemos la interfaz EstadoReproductorMusica, que define los métodos reproducir(), pausar() y detener(), 
que serán implementados por las clases concretas de estado.

Luego, tenemos tres implementaciones concretas de estado: EstadoReproduciendo, EstadoPausa y EstadoDetenido, cada una 
con su propio comportamiento para los métodos.

La clase ReproductorMusica es el contexto que contiene el estado actual y llama a los métodos correspondientes del 
estado actual.

En el ejemplo, creamos un reproductor de música que inicialmente está en estado "Detenido". Luego, cambiamos su estado a 
"Reproduciendo" y llamamos a los métodos reproducir(), pausar() y detener() según corresponda al estado actual.

En resumen, el patrón State es útil cuando tienes un objeto que puede cambiar su comportamiento según su estado interno. 
Con este patrón, puedes representar diferentes estados como clases separadas y permitir que el objeto cambie de un 
estado a otro conforme cambie su estado interno. Esto promueve la flexibilidad y el mantenimiento del código, ya que 
puedes agregar nuevos estados y comportamientos sin afectar el contexto que los utiliza.
"""