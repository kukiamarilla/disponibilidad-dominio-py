
# .py Domain Availability Checker

Este programa verifica la disponibilidad de dominios en el sitio web de NIC Paraguay (nic.py). Utiliza Selenium para interactuar con el navegador y obtener el estado de disponibilidad de un dominio específico.

## Requisitos

Antes de ejecutar el programa, asegúrate de tener instalados los siguientes paquetes de Python:

- Selenium
- webdriver-manager

Puedes instalar estos paquetes utilizando `pip` con el archivo `requirements.txt` incluido en este repositorio.

```bash
pip install -r requirements.txt
```

## Configuración

Este programa utiliza Chrome en modo headless (sin interfaz gráfica). Asegúrate de que tienes Chrome instalado en tu máquina.

## Uso

Puedes ejecutar el script desde la línea de comandos. Proporciona el nombre del dominio como argumento. El dominio debe tener el formato `nombre.dominio.py`.

```bash
python domain_checker.py nombre.dominio.py
```

### Ejemplo

Para verificar la disponibilidad de `example.com.py`, ejecuta:

```bash
python domain_checker.py example.com.py
```

## Salida

El programa devuelve un JSON con la disponibilidad del dominio. La salida tendrá el siguiente formato:

```json
{
    "google.com.py": false,
    "google.coop.py": true,
    "google.edu.py": true,
    "google.gov.py": true,
    "google.mil.py": true,
    "google.net.py": true,
    "google.org.py": true
}
```

Donde `true` indica que el dominio está disponible y `false` indica que no lo está.

## Notas

- Asegúrate de que el dominio que estás verificando termina con `.py`.
- El programa tiene un tiempo de espera de 3 segundos para permitir que la página cargue completamente. Puedes ajustar este tiempo según tus necesidades.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias o mejoras, siéntete libre de abrir un issue o enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.
