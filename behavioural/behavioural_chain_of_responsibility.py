"""
Behavioural pattern Chain of Responsibility

El patrón Chain of Responsibility (Cadena de Responsabilidad) es un patrón de diseño de comportamiento que permite que 
varios objetos (llamados "manejadores") se encadenen y procesen una solicitud de manera secuencial. Cada manejador 
decide si puede manejar la solicitud o si debe pasarla al siguiente manejador en la cadena. De esta manera, se evita 
acoplar el emisor de la solicitud con su receptor, lo que permite una mayor flexibilidad en la asignación de 
responsabilidades y el procesamiento de las solicitudes.

Imagina que tienes una serie de clases que realizan diferentes tareas, y necesitas que una solicitud atraviese estas 
clases en un orden específico hasta que una de ellas pueda manejarla. El patrón Chain of Responsibility permite 
establecer una cadena de objetos que procesen la solicitud secuencialmente hasta que encuentren un objeto que pueda 
manejarla.

Ejemplo en Python:

Supongamos que tenemos una serie de descuentos aplicables a una compra en una tienda. Cada descuento tiene un límite de 
cantidad y si el monto de la compra supera ese límite, ese descuento no puede ser aplicado. Utilizaremos el patrón Chain 
of Responsibility para crear una cadena de manejadores que verificarán si pueden aplicar el descuento, y si no pueden, 
pasan la solicitud al siguiente manejador.
"""

# Clase base: Manejador de Descuento
class ManejadorDescuento:
    def __init__(self, siguiente=None):
        self.siguiente = siguiente

    def aplicar_descuento(self, monto_compra: float):
        pass

# Implementación concreta de ManejadorDescuento
class ManejadorDescuento10(ManejadorDescuento):
    def aplicar_descuento(self, monto_compra: float) -> float:
        if monto_compra >= 100:
            print("Descuento del 10% aplicado")
            return monto_compra * 0.10
        elif self.siguiente:
            return self.siguiente.aplicar_descuento(monto_compra)
        else:
            return 0

# Implementación concreta de ManejadorDescuento
class ManejadorDescuento20(ManejadorDescuento):
    def aplicar_descuento(self, monto_compra: float) -> float:
        if monto_compra >= 200:
            print("Descuento del 20% aplicado")
            return monto_compra * 0.20
        elif self.siguiente:
            return self.siguiente.aplicar_descuento(monto_compra)
        else:
            return 0

# Implementación concreta de ManejadorDescuento
class ManejadorDescuento30(ManejadorDescuento):
    def aplicar_descuento(self, monto_compra: float) -> float:
        if monto_compra >= 300:
            print("Descuento del 30% aplicado")
            return monto_compra * 0.30
        elif self.siguiente:
            return self.siguiente.aplicar_descuento(monto_compra)
        else:
            return 0

# Ejemplo de uso del patrón Chain of Responsibility
def aplicar_descuento_chain(manejador: ManejadorDescuento, monto_compra: float):
    descuento = manejador.aplicar_descuento(monto_compra)
    if descuento == 0:
        print("No se pudo aplicar ningún descuento.")
    else:
        print(f"Total con descuento: {monto_compra - descuento}")

# Creación de la cadena de manejadores
manejador_30 = ManejadorDescuento30()
manejador_20 = ManejadorDescuento20(manejador_30)
manejador_10 = ManejadorDescuento10(manejador_20)

# Prueba con diferentes montos de compra
aplicar_descuento_chain(manejador_10, 250)
# Output: Descuento del 20% aplicado
# Total con descuento: 200.0

aplicar_descuento_chain(manejador_10, 120)
# Output: Descuento del 10% aplicado
# Total con descuento: 108.0

aplicar_descuento_chain(manejador_10, 400)
# Output: Descuento del 30% aplicado
# Total con descuento: 280.0

"""
En este ejemplo, tenemos la clase ManejadorDescuento, que es la clase base para los manejadores concretos. Cada 
manejador concreto (por ejemplo, ManejadorDescuento10, ManejadorDescuento20, etc.) tiene su propia lógica para aplicar 
el descuento, y si no puede manejar la solicitud, pasa la solicitud al siguiente manejador en la cadena.

La función aplicar_descuento_chain() toma un manejador y un monto de compra como argumentos, y aplica el descuento en la 
cadena de manejadores hasta que encuentra uno que pueda manejar la solicitud.

En resumen, el patrón Chain of Responsibility es útil cuando tienes una serie de objetos que deben procesar una 
solicitud en un orden específico, pero no sabes cuál de ellos puede manejar la solicitud en tiempo de diseño. Con este 
patrón, puedes encadenar los objetos y pasar la solicitud a lo largo de la cadena hasta que uno de ellos la maneje. Esto 
promueve la desacoplaración y la flexibilidad en el procesamiento de las solicitudes.
"""