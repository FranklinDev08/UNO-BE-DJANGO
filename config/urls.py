from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView

# TODO: Definir las rutas principales del proyecto Django
urlpatterns = [
    # TODO: Ruta para acceder al panel de administración de Django
    path('admin/', admin.site.urls),

    # TODO: Ruta para acceder al endpoint GraphQL
    # Se habilita la interfaz GraphiQL para pruebas interactivas
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]
