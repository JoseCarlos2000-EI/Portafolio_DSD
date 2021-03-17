from django.urls import path
from . import views

urlpatterns=[
    path('',views.lisusuario,name="principal"),
    path('agregar/',views.agregarusuario,name="agregar_usuario"),
    path('eliminar/<int:ide>',views.eliminarusuario,name="eliminar_usuario"),
    path('pagina_editar/<int:id>',views.pagina_editar,name="pedit"),
    path('pagina_actualizar/<int:ide>',views.actualizar_usu,name="actualizar")
]