from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView

# TODO: Definir rutas principales del proyecto
urlpatterns = [
    # TODO: Ruta del panel de administración de Django
    path('admin/', admin.site.urls),

    # TODO: Ruta para GraphQL
    # - graphiql=True habilita la interfaz web de pruebas de GraphQL
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]
