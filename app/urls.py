from django.urls import path
from . import views

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),

    path('relaciones', views.relaciones, name='relaciones'),

    path('recetas', views.recetas_lista, name='recetas_lista'),
    path('receta/<int:pk>', views.receta_detalle, name='receta_detalle'),
    path('receta/<int:receta_pk>/agregar_ingrediente/<int:ingrediente_pk>', views.receta_agregar_ingrediente, name='receta_agregar_ingrediente'),

    path('ingredientes', views.IngredienteListaView.as_view(), name='ingredientes_lista'),
        
    path('ingredientes/nuevo', views.IngredienteNuevoView.as_view(), name='ingredientes_nuevo'),
    path('ingredientes/<int:pk>', views.IngredienteDetalleView.as_view(), name='ingredientes_detalle'),
    path('ingredientes/<int:pk>/editar', views.IngredienteEditarView.as_view(), name='ingredientes_editar'),
    path('ingredientes/<int:pk>/borrar', views.IngredienteEliminarView.as_view(), name='ingredientes_borrar'),

    path('ingredientes/nuevomodel', views.ingredientes_nuevo_model, name='ingredientes_nuevo_model'),
]