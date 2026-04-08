from django.contrib import admin # Importujemy narzędzia panelu admina
from .models import Project, Sprint, Issue, Comment # Importujemy nasze modele

# Rejestrujemy każdy model, aby pojawił się w panelu na stronie
admin.site.register(Project)
admin.site.register(Sprint)
admin.site.register(Issue)
admin.site.register(Comment)