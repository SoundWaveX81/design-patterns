"""
Structural pattern Facade

El patrón Facade es un patrón de diseño estructural que proporciona una interfaz simplificada y unificada para un 
conjunto de interfaces y subsistemas más complejos. El objetivo del patrón Facade es ocultar la complejidad detrás de 
una interfaz fácil de usar, permitiendo que los clientes interactúen con el sistema de manera más sencilla y reduciendo 
el acoplamiento entre los componentes.

Imagina que tienes un sistema complejo con muchas clases y subsistemas que se comunican entre sí para llevar a cabo una 
tarea. Sin embargo, para un cliente externo, todas las interacciones con el sistema pueden ser abrumadoras y difíciles 
de manejar. Aquí es donde entra en juego el patrón Facade, proporcionando una fachada (interfaz simple) que oculta toda 
la complejidad detrás de escena y simplifica la interacción con el sistema.

Ejemplo en Python:

Supongamos que tenemos un sistema que se encarga del encendido y apagado de una computadora. El sistema tiene varias 
clases y subsistemas que se encargan de diferentes tareas, como verificar la energía, cargar el sistema operativo y 
detener los servicios antes de apagar la computadora.
"""

# Subsistema para verificar la energía
class VerificadorEnergia:
    @property
    def esta_encendida(self):
        print("Verificando si la energía está encendida.")
        return True

# Subsistema para cargar el sistema operativo
class CargadorSistemaOperativo:
    def cargar(self):
        print("Cargando el sistema operativo.")

# Subsistema para detener servicios antes de apagar
class DetenerServicios:
    def detener(self):
        print("Deteniendo servicios antes de apagar.")

# La fachada que simplifica la interacción con el sistema complejo
class FachadaComputadora:
    def __init__(self):
        self.verificador_energia = VerificadorEnergia()
        self.cargador_sistema_operativo = CargadorSistemaOperativo()
        self.detener_servicios = DetenerServicios()

    def encender(self):
        if not self.verificador_energia.esta_encendida:
            self.cargador_sistema_operativo.cargar()
            print("Encendiendo la computadora.")
            return
        print("la computadora ya se encontraba encendida")


    def apagar(self):
        if self.verificador_energia.esta_encendida:
            self.detener_servicios.detener()
            print("Apagando la computadora.")
            return
        print("la computadora ya se encontraba apagada")


"""
En este ejemplo, tenemos tres clases que representan subsistemas dentro del sistema completo. Luego, creamos la clase 
FachadaComputadora, que proporciona una interfaz sencilla para encender y apagar la computadora. Esta fachada se encarga 
de interactuar con los subsistemas y oculta toda la complejidad interna de cómo se lleva a cabo el proceso.

Ahora podemos usar la fachada para interactuar con el sistema de manera simple:
"""

# Crear una instancia de la fachada
computadora = FachadaComputadora()

# Encender la computadora (utiliza los subsistemas internos)
computadora.encender()
# Output:
# Verificando si la energía está encendida.
# Cargando el sistema operativo.
# Encendiendo la computadora.

# Apagar la computadora (utiliza los subsistemas internos)
computadora.apagar()
# Output:
# Deteniendo servicios antes de apagar.
# Apagando la computadora.

"""
En este ejemplo, hemos utilizado la fachada FachadaComputadora para encender y apagar la computadora sin necesidad de 
conocer todos los detalles internos del sistema. La fachada proporciona una interfaz simple que oculta la complejidad de 
los subsistemas y simplifica la interacción con el sistema.

En resumen, el patrón Facade es útil cuando tienes un sistema complejo con múltiples clases y subsistemas y deseas 
proporcionar una interfaz simple y unificada para interactuar con el sistema sin tener que conocer todos los detalles 
internos. La fachada simplifica el acceso a funcionalidades complejas y reduce el acoplamiento entre los componentes 
del sistema.
"""