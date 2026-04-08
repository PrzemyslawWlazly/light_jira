from django.contrib import admin
from django.urls import path, include # Dodaliśmy 'include' do importów

urlpatterns = [
    path('admin/', admin.site.urls), # Domyślny panel admina Django
    path('api/', include('board.urls')), # DODANE: Wszystkie ścieżki z aplikacji board będą miały przedrostek /api/
]