************************************
Desing Patterns (Patrones de Diseño)
************************************

En ingeniería de software, los patrones de diseño son soluciones probadas y comprobadas para problemas comunes que surgen durante el proceso de diseño y desarrollo de software. Se dividen en tres categorías principales: patrones de diseño estructurales, patrones de diseño creacionales y patrones de diseño de comportamiento. A continuación, describiré las diferencias entre cada categoría:


Patrones de diseño estructurales:
#################################

Los patrones de diseño estructurales se centran en cómo las clases y objetos se componen para formar estructuras más grandes y flexibles. Estos patrones ayudan a lograr una organización eficiente de las clases y simplifican las relaciones entre ellas. Algunos ejemplos de patrones de diseño estructurales incluyen:

* **Adapter (Adaptador):** Permite que clases incompatibles trabajen juntas a través de una interfaz común.
* **Bridge (Puente):** Separa la interfaz de una clase de su implementación, lo que permite cambios independientes en ambas.
* **Decorator (Decorador):** Agrega funcionalidad adicional a objetos de manera dinámica.
* **Composite (Compuesto):** Permite tratar objetos individuales y composiciones de objetos de manera uniforme.
* **Facade (Fachada):** Proporciona una interfaz simple para un subsistema complejo.
* **Proxy (Proxy):** Actúa como intermediario para controlar el acceso a un objeto.

Patrones de diseño creacionales:
################################

Los patrones de diseño creacionales se enfocan en la creación de objetos de manera eficiente y flexible. Estos patrones ocultan la lógica de creación de objetos, lo que hace que el código sea más independiente de las clases concretas utilizadas en el sistema. Algunos ejemplos de patrones de diseño creacionales incluyen:

* **Factory Method (Método de fábrica):** Define una interfaz para crear objetos, pero permite que las subclases decidan qué clase instanciar.
* **Abstract Factory (Fábrica abstracta):**  Proporciona una interfaz para crear familias de objetos relacionados sin especificar sus clases concretas.
* **Singleton (Singleton):** Garantiza que una clase tenga una sola instancia y proporciona un punto de acceso global a ella.
* **Builder (Constructor):** Separa la construcción de un objeto complejo de su representación, lo que permite crear diferentes representaciones usando el mismo proceso de construcción.
* **Prototype (Prototipo):** Permite copiar objetos existentes sin hacer que el código dependa de sus clases concretas.

Patrones de diseño de comportamiento:
#####################################

Los patrones de diseño de comportamiento se centran en cómo las clases y objetos interactúan y distribuyen la responsabilidad entre ellos. Estos patrones ayudan a facilitar la comunicación y colaboración entre componentes de un sistema. Algunos ejemplos de patrones de diseño de comportamiento incluyen:

* **Observer (Observador):** Define una dependencia uno a muchos entre objetos, de modo que cuando un objeto cambia de estado, todos sus dependientes son notificados y actualizados automáticamente.
* **Strategy (Estrategia):** Permite definir una familia de algoritmos, encapsular cada uno de ellos y hacerlos intercambiables.
* **Chain of Responsibility (Cadena de responsabilidad):** Permite pasar solicitudes a lo largo de una cadena de manejadores que pueden procesar la solicitud o pasarla al siguiente manejador.
* **Command (Comando):** Encapsula una solicitud como un objeto, lo que permite parametrizar clientes con diferentes solicitudes, encolarlas o registrar su ejecución.
* **Interpreter (Intérprete):** Define una gramática para un lenguaje y proporciona una interpretación para las oraciones en ese lenguaje.
* **State (Estado):** Permite que un objeto cambie su comportamiento cuando su estado interno cambia.
* **Template Method (Método de plantilla):** Define el esqueleto de un algoritmo en una operación, dejando que las subclases proporcionen ciertos pasos del algoritmo sin cambiar su estructura.

En resumen, los patrones de diseño estructurales se centran en la organización de clases y objetos, los patrones de diseño creacionales se enfocan en la creación de objetos y los patrones de diseño de comportamiento se centran en cómo los objetos interactúan y distribuyen responsabilidades. Cada tipo de patrón aborda diferentes aspectos del diseño de software y ayuda a mejorar la modularidad, flexibilidad y reutilización del código.