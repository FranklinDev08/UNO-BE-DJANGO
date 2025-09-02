
import os
import sys

# TODO: Función principal para ejecutar las tareas administrativas de Django
def main():
    # TODO: Establecer la configuración base del proyecto
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
    try:
        # TODO: Importar el comando principal de Django para ejecutar tareas desde la línea de comandos
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # TODO: Mostrar mensaje de error si Django no está instalado o no se encuentra en el entorno
        raise ImportError(
            "No se pudo importar Django. Asegúrate de tenerlo instalado y disponible en tu PYTHONPATH."
        ) from exc
    # TODO: Ejecutar los comandos de Django recibidos como argumentos
    execute_from_command_line(sys.argv)

# TODO: Punto de entrada principal cuando se ejecuta este archivo directamente
if __name__ == '__main__':
    main()
