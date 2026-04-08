from django.urls import path, include # Importujemy narzędzia z Django do definiowania ścieżek URL oraz dołączania zgrupowanych list URL-i.
from rest_framework.routers import DefaultRouter # Importujemy router z DRF, który automatycznie wygeneruje adresy dla operacji CRUD (tworzenie, czytanie, edycja, usuwanie).
from .views import ProjectViewSet, SprintViewSet, IssueViewSet, CommentViewSet # Importujemy klasy widoków z naszego pliku views.py, które zawierają logikę bazy danych.

router = DefaultRouter() # Tworzymy główny obiekt routera, który zaraz "nakarmimy" naszymi widokami.
router.register(r'projects', ProjectViewSet) # Rejestrujemy trasę dla projektów. Będą one dostępne pod adresem końcowym /projects/.
router.register(r'sprints', SprintViewSet) # Rejestrujemy trasę dla sprintów. Będą one dostępne pod adresem końcowym /sprints/.
router.register(r'issues', IssueViewSet, basename='issue') # KLUCZOWE: Rejestrujemy trasę /issues/. Dodajemy basename='issue', ponieważ usunęliśmy w widoku domyślne pole queryset, a router potrzebuje nazwy bazowej.
router.register(r'comments', CommentViewSet) # Rejestrujemy trasę dla komentarzy. Będą one dostępne pod adresem końcowym /comments/.

urlpatterns = [ # Deklarujemy standardową listę urlpatterns, której Django szuka w każdym pliku konfiguracji tras.
    path('', include(router.urls)), # Przekazujemy wszystkie wygenerowane przez router adresy do pustej ścieżki bazowej (która w głównym urls.py ma przedrostek /api/).
] # Zamykamy listę tras.