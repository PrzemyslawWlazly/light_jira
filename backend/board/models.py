from django.db import models # Import narzędzi do tworzenia tabel
from django.conf import settings # Import ustawień, aby podpiąć naszego CustomUsera jako klucz obcy

class Project(models.Model): # Klasa reprezentująca tabelę projektów
    name = models.CharField(max_length=100) # Pole znakowe na nazwę projektu (np. Aplikacja Mobilna)
    project_key = models.CharField(max_length=5, unique=True) # Krótki, unikalny klucz do generowania ID (np. MOB)
    created_at = models.DateTimeField(auto_now_add=True) # Data utworzenia, zapisywana automatycznie przy tworzeniu rekordu

    def __str__(self): # Reprezentacja tekstowa
        return self.name # Zwraca nazwę projektu

class Sprint(models.Model): # Klasa reprezentująca iteracje (sprinty)
    STATUS_CHOICES = (('PLANNED', 'Planned'), ('ACTIVE', 'Active'), ('CLOSED', 'Closed')) # Możliwe statusy sprintu
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='sprints') # Klucz obcy do Projektu. Usunięcie projektu usuwa sprinty (CASCADE).
    name = models.CharField(max_length=100) # Nazwa sprintu (np. Sprint 1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PLANNED') # Pole statusu, domyślnie "zaplanowany"
    start_date = models.DateField(null=True, blank=True) # Data startu (opcjonalna przed startem)
    end_date = models.DateField(null=True, blank=True) # Data zakończenia (opcjonalna)

class Issue(models.Model): # Klasa dla Zgłoszeń (Zadania, Błędy, Historyjki)
    TYPE_CHOICES = (('STORY', 'Story'), ('TASK', 'Task'), ('BUG', 'Bug')) # Typy zgłoszeń zakodowane na sztywno
    PRIORITY_CHOICES = (('HIGH', 'High'), ('MEDIUM', 'Medium'), ('LOW', 'Low')) # Priorytety
    STATUS_CHOICES = (('TO_DO', 'To Do'), ('IN_PROGRESS', 'In Progress'), ('CODE_REVIEW', 'Code Review'), ('DONE', 'Done')) # Prosty obieg pracy

    project = models.ForeignKey(Project, on_delete=models.CASCADE) # Powiązanie zadania z konkretnym projektem
    sprint = models.ForeignKey(Sprint, on_delete=models.SET_NULL, null=True, blank=True) # Powiązanie ze sprintem (NULL oznacza, że jest w Backlogu)
    issue_key = models.CharField(max_length=20, unique=True) # Klucz zgłoszenia (np. MOB-14) widoczny dla usera
    title = models.CharField(max_length=255) # Wymagany tytuł zadania
    description = models.TextField(null=True, blank=True) # Pole tekstowe na dłuższy opis
    type = models.CharField(max_length=20, choices=TYPE_CHOICES) # Wybór typu zgłoszenia
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES) # Wybór priorytetu
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TO_DO') # Status na tablicy, domyślnie TO_DO
    story_points = models.IntegerField(null=True, blank=True) # Wycena w Story Points
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reported_issues', on_delete=models.CASCADE) # Twórca zadania (User)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='assigned_issues', on_delete=models.SET_NULL, null=True, blank=True) # Przypisany użytkownik
    backlog_order = models.IntegerField(default=0) # Pole do przechowywania kolejności drag&drop
    created_at = models.DateTimeField(auto_now_add=True) # Data dodania
    updated_at = models.DateTimeField(auto_now=True) # Data ostatniej modyfikacji (nadpisuje się przy save())

class Comment(models.Model): # Klasa dla komentarzy pod zgłoszeniami
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments') # Przypisanie komentarza do konkretnego zadania
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Autor komentarza
    content = models.TextField() # Treść wpisu
    created_at = models.DateTimeField(auto_now_add=True) # Czas dodania