from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # Importujemy domyślny wygląd panelu dla użytkowników
from .models import CustomUser

# Rejestrujemy naszego CustomUsera, używając gotowego szablonu UserAdmin
admin.site.register(CustomUser, UserAdmin)