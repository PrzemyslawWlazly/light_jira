from rest_framework import serializers # Importujemy narzędzia DRF
from .models import Project, Sprint, Issue, Comment # Importujemy nasze tabele
from users.models import CustomUser # Importujemy model użytkownika

# Serializer dla użytkowników (żeby wiedzieć kto jest przypisany do zadania)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser # Wskazujemy model
        fields = ['id', 'username', 'email', 'role'] # Pola, które chcemy wysłać do Reacta

# Serializer dla Projektów
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__' # '__all__' oznacza: weź wszystkie pola z modelu

# Serializer dla Sprintów
class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'

# Serializer dla Komentarzy
class CommentSerializer(serializers.ModelSerializer):
    author_details = UserSerializer(source='author', read_only=True) # Dodatkowo wysyłamy pełne dane autora

    class Meta:
        model = Comment
        fields = '__all__'

# Serializer dla Zgłoszeń (Zadań)
class IssueSerializer(serializers.ModelSerializer):
    # Dzięki temu React dostanie od razu ładne obiekty usera, a nie tylko jego ID
    assignee_details = UserSerializer(source='assignee', read_only=True) 
    reporter_details = UserSerializer(source='reporter', read_only=True)

    class Meta:
        model = Issue
        fields = '__all__'