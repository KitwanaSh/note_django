from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path("notes/", views.GetNotes, name="notes"),
    # path('notes/create/', views.createNote, name="create-note"),
    # path('notes/<str:pk>/update/', views.UpdateNote, name="update-note"),
    # path('notes/<str:pk>/delete/', views.DeleteNote, name="delete-note"),

    path('notes/<str:pk>/', views.GetNote, name="note")
]
