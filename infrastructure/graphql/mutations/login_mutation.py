# TODO: Importaciones necesarias
import graphene                   # Librería GraphQL para definir esquemas y mutaciones
import hashlib                    # Para encriptar la contraseña usando SHA256
import jwt                        # Para generar tokens JWT
from django.conf import settings  # Para acceder a la configuración del proyecto (SECRET_KEY)
from infrastructure.models.user_model import UserModel  # Modelo de usuario desde la capa de infraestructura


# TODO: Definición de la estructura de respuesta de la mutación de login
class LoginResult(graphene.ObjectType):
    """
    TODO: Clase que define el formato de la respuesta de la mutación.
    Contiene información sobre éxito del login, datos del usuario y token JWT.
    """
    success = graphene.Boolean()   # Indica si la operación fue exitosa
    message = graphene.String()    # Mensaje informativo para el cliente
    userId = graphene.ID()         # ID del usuario (GraphQL ID)
    username = graphene.String()   # Nombre de usuario
    email = graphene.String()      # Correo electrónico del usuario
    token = graphene.String()      # JWT generado al iniciar sesión


# TODO: Definición de la mutación de login
class LoginMutation(graphene.Mutation):
    # TODO: Argumentos que recibe la mutación
    class Arguments:
        username = graphene.String(required=True)  # Nombre de usuario (obligatorio)
        password = graphene.String(required=True)  # Contraseña en texto plano (obligatoria)

    # TODO: Tipo de salida de la mutación
    Output = LoginResult

    # TODO: Lógica principal de la mutación
    def mutate(root, info, username, password):
        # TODO: Encriptar la contraseña usando SHA256 para compararla con la almacenada
        password_hash = hashlib.sha256(password.encode()).hexdigest()

        try:
            # TODO: Intentar obtener el usuario activo con las credenciales proporcionadas
            user = UserModel.objects.get(username=username, password=password_hash, activo=True)

            # TODO: Generar token JWT con información básica del usuario
            payload = {
                "user_id": user.id,
                "username": user.username,
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")  # TODO: Firmar con SECRET_KEY

            # TODO: Retornar resultado exitoso con información del usuario y token
            return LoginResult(
                success=True,
                message="Login correcto",
                userId=user.id,
                username=user.username,
                email=user.email,
                token=token
            )

        except UserModel.DoesNotExist:
            # TODO: Retornar resultado fallido si usuario o contraseña son incorrectos
            return LoginResult(
                success=False,
                message="Usuario o contraseña incorrectos",
                userId=None,
                username=None,
                email=None,
                token=None
            )


# TODO: Clase contenedora de las mutaciones relacionadas al login
class LoginMutations(graphene.ObjectType):
    login = LoginMutation.Field()  # TODO: Definir la mutación 'login' como un campo GraphQL
