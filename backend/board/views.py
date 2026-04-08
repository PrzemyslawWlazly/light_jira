from rest_framework import viewsets # ViewSety to gotowe pakiety logiki (GET, POST, PUT, DELETE)
from .models import Project, Sprint, Issue, Comment
from .serializers import ProjectSerializer, SprintSerializer, IssueSerializer, CommentSerializer

# Widok dla Projektów
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # Skąd brać dane? Z całej tabeli Project.
    serializer_class = ProjectSerializer # Jakiego tłumacza użyć? ProjectSerializer.

# Widok dla Sprintów
class SprintViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer

# Widok dla Zgłoszeń
class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer

    # Nadpisujemy domyślną funkcję pobierającą bazę danych
    def get_queryset(self):
        # 1. Pobieramy wszystkie zadania jako punkt wyjścia
        queryset = Issue.objects.all().order_by('backlog_order')
        
        # 2. Sprawdzamy, czy React przesłał nam parametr o nazwie 'projectKey'
        project_key = self.request.query_params.get('projectKey', None)
        
        # 3. Jeśli parametr istnieje (czyli nie jest None)
        if project_key is not None:
            # Filtrujemy bazę. Zapis "project__project_key" oznacza: 
            # "Wejdź z zadania do powiązanego projektu i weź jego pole project_key"
            queryset = queryset.filter(project__project_key=project_key)
            
        return queryset # 4. Zwracamy przefiltrowaną listę (lub pełną, jeśli nie było parametru)

# Widok dla Komentarzy
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer