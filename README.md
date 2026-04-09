Wymagania wstępne

Aby uruchomić projekt na swoim komputerze, upewnij się, że masz zainstalowane:

    Python (wersja 3.8 lub nowsza)

    Node.js (wersja 18 lub nowsza) oraz menedżer pakietów npm

    Git

Instrukcja uruchomienia (Środowisko Deweloperskie)

Projekt składa się z dwóch niezależnych części. Należy uruchomić dwa osobne terminale – jeden dla serwera backendowego, drugi dla interfejsu frontendowego.
Krok 1: Klonowanie repozytorium

Pobierz projekt na swój dysk lokalny:


git clone https://github.com/PrzemyslawWlazly/light_jira
cd light_jira

Krok 2: Uruchomienie Backend (Django)

Warstwa serwerowa wykorzystuje wirtualne środowisko, aby nie zaśmiecać głównego systemu pakietami Pythona.

    Wejdź do folderu backendu:



cd backend

    Utwórz nowe środowisko wirtualne (ponieważ nie jest ono przesyłane na GitHuba):


python -m venv venv

    Aktywuj środowisko wirtualne:

    Linux/macOS: source venv/bin/activate

    Windows (Command Prompt): venv\Scripts\activate

    Windows (PowerShell): venv\Scripts\Activate.ps1

    Zainstaluj wymagane biblioteki:



pip install -r requirements.txt

(Uwaga: Jeśli plik requirements.txt jeszcze nie istnieje, zainstaluj ręcznie: pip install django djangorestframework django-cors-headers i wygeneruj plik poleceniem: pip freeze > requirements.txt)
5. Wykonaj migracje (utworzenie lokalnej bazy danych SQLite):


python manage.py migrate

    Uruchom serwer testowy:



python manage.py runserver

Serwer API będzie dostępny pod adresem: http://127.0.0.1:8000/api/
Krok 3: Uruchomienie Frontend (React + Vite)

Warstwa kliencka wymaga pobrania bibliotek node'a przed pierwszym uruchomieniem.

    Otwórz nowe, drugie okno terminala i wejdź do folderu frontendu:



cd frontend

    Zainstaluj wszystkie niezbędne pakiety (odbuduje to ukryty folder node_modules):



npm install

    Uruchom serwer deweloperski Vite:


npm run dev

Aplikacja będzie dostępna pod adresem: http://localhost:5173/
🔑 Konto Administratora (Opcjonalnie)

Aby uzyskać dostęp do panelu administracyjnego Django (do ręcznego zarządzania bazą danych), utwórz konto superużytkownika w aktywnym środowisku wirtualnym w folderze backend:
Bash

python manage.py createsuperuser

Panel admina dostępny jest pod adresem: http://127.0.0.1:8000/admin/
📂 Struktura Projektu

    /backend - Logika API (Django REST Framework), modele bazy danych, system autoryzacji.

    /frontend - Interfejs graficzny SPA (React), widoki tablicy Kanban, formularze, logika Drag & Drop.
