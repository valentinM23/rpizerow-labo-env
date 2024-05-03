from gpiozero import LED, Button  # Importa las clases LED y Button del módulo gpiozero  
from signal import pause   # Importa la función pause del módulo signal.
# Crea una instancia de la clase LED, que controla un LED conectado al pin 26.
led = LED(26)  # Crea una instancia de la clase Button, que representa un botón conectado al pin 18.
button = Button(18)   # Cuando el botón es presionado, se activa el método "on" del LED, encendiéndolo.

button.when_pressed = led.on  # Cuando el botón es presionado, se activa el método "on" del LED, encendiéndolo.  .
button.when_released = led.off    # Cuando el botón es soltado, se activa el método "off" del LED, apagándolo.

pause()   # Mantenemos el programa en ejecución para que pueda responder a eventos de botones.
