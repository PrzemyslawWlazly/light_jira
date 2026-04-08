from django.contrib.auth.models import AbstractUser # Importujemy bazowy model użytkownika z Django, który rozszerzymy
from django.db import models # Importujemy narzędzia bazodanowe Django

class CustomUser(AbstractUser): # Tworzymy własną klasę użytkownika dziedziczącą po AbstractUser
    ROLE_CHOICES = ( # Definiujemy krotkę z dostępnymi rolami (wymóg MVP)
        ('ADMIN', 'Administrator'), # Rola Administratora (klucz w bazie, nazwa w UI)
        ('USER', 'User'), # Rola zwykłego użytkownika
    ) # Zamykamy krotkę
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='USER') # Dodajemy pole "role" typu znakowego z ograniczeniem do wyborów wyżej

    def __str__(self): # Definiujemy metodę tekstowej reprezentacji obiektu
        return self.email # Zwracamy e-mail, co ułatwi odczytywanie w panelu admina