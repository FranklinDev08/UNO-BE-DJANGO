from django.apps import AppConfig

# TODO: Configuración de la aplicación "core"
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # TODO: ID por defecto para los modelos
    name = 'core'  # TODO: nombre de la app, debe coincidir con el paquete
