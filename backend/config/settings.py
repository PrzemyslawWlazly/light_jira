from pathlib import Path # Importujemy narzędzie z Pythona do łatwego zarządzania ścieżkami na dysku.

BASE_DIR = Path(__file__).resolve().parent.parent # Ustalamy ścieżkę do głównego folderu backendu (tam gdzie jest manage.py).

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c@0k(1c1mu6q_sefc@!5nry6*wamf+kng2mf#+@_&d!u#^+=zh' # Tajny klucz kryptograficzny Django (służy np. do szyfrowania ciasteczek).

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # Włącza tryb deweloperski (wyświetla szczegółowe błędy). Na serwerze produkcyjnym musi być False.

ALLOWED_HOSTS = [] # Lista domen/IP, które mogą hostować tę aplikację. Puste pole oznacza, że działa tylko lokalnie.

INSTALLED_APPS = [ # Główna lista modułów i aplikacji wchodzących w skład naszego systemu.
    'django.contrib.admin', # Wbudowany gotowy panel administratora Django.
    'django.contrib.auth', # Wbudowany moduł uwierzytelniania i uprawnień.
    'django.contrib.contenttypes', # Wbudowany moduł śledzący wszystkie modele w bazie danych.
    'django.contrib.sessions', # Wbudowany moduł zarządzający sesjami użytkowników (logowaniem).
    'django.contrib.messages', # Wbudowany moduł do wyświetlania jednorazowych komunikatów (np. "Zapisano").
    'django.contrib.staticfiles', # Wbudowany moduł serwujący pliki CSS/JS dla panelu admina.
    
    'rest_framework', # DODANE: Django REST Framework - narzędzie niezbędne do wystawiania API dla Reacta.
    'corsheaders', # DODANE: Biblioteka zapobiegająca blokowaniu zapytań z Reacta do Django przez przeglądarkę.
    
    'users', # DODANE: Nasza aplikacja 'users' z uproszczonym modelem kont[cite: 83, 84].
    'board', # DODANE: Nasza aplikacja 'board' zawierająca logikę Scrum (zgłoszenia, sprinty)[cite: 82, 83].
] # Koniec listy aplikacji.

MIDDLEWARE = [ # Filtry (oprogramowanie pośredniczące), przez które przechodzi każde zapytanie HTTP.
    'django.middleware.security.SecurityMiddleware', # Zabezpieczenia takie jak wymuszanie HTTPS (na produkcji).
    'corsheaders.middleware.CorsMiddleware', # DODANE: Przechwytuje pytania z Reacta i dodaje nagłówki zezwalające na komunikację.
    'django.contrib.sessions.middleware.SessionMiddleware', # Pozwala Django rozpoznawać sesję (ciasteczko) użytkownika.
    'django.middleware.common.CommonMiddleware', # Dodaje m.in. ukośniki na końcu adresów URL, jeśli ich brakuje.
    'django.middleware.csrf.CsrfViewMiddleware', # Chroni formularze przed atakami typu Cross-Site Request Forgery.
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Przypisuje zalogowanego użytkownika do przychodzącego zapytania.
    'django.contrib.messages.middleware.MessageMiddleware', # Współpracuje z aplikacją messages z INSTALLED_APPS.
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Chroni przed atakiem clickjacking (blokuje ładowanie w ramkach iframe).
] # Koniec listy middleware.

ROOT_URLCONF = 'config.urls' # Wskazuje plik, w którym Django ma szukać głównych tras (routingu) API.

TEMPLATES = [ # Ustawienia silnika generowania HTML (przyda się dla wbudowanego panelu admina).
    { # Otwieramy słownik konfiguracji domyślnego silnika szablonów.
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # Wskazujemy użycie wbudowanego silnika Django.
        'DIRS': [], # Ewentualne dodatkowe ścieżki do plików HTML (u nas na razie pusto).
        'APP_DIRS': True, # Nakazuje Django szukać folderów 'templates' automatycznie w każdej aplikacji z INSTALLED_APPS.
        'OPTIONS': { # Dodatkowe opcje i zmienne przekazywane do szablonów HTML.
            'context_processors': [ # Funkcje wrzucające określone dane do każdego szablonu HTML na stronie.
                'django.template.context_processors.request', # Udostępnia dane o zapytaniu HTTP w HTML.
                'django.contrib.auth.context_processors.auth', # Udostępnia dane o zalogowanym użytkowniku w HTML.
                'django.contrib.messages.context_processors.messages', # Udostępnia komunikaty systemowe w HTML.
            ], # Koniec listy procesorów kontekstu.
        }, # Koniec opcji szablonów.
    }, # Koniec słownika szablonów.
] # Koniec listy szablonów.

WSGI_APPLICATION = 'config.wsgi.application' # Wskazuje główny plik startowy dla serwerów produkcyjnych w Pythonie.

DATABASES = { # Konfiguracja bazy danych dla naszego MVP[cite: 81].
    'default': { # Konfiguracja głównej (i jedynej) bazy danych.
        'ENGINE': 'django.db.backends.sqlite3', # Używamy SQLite, które jest najprostsze we wdrożeniu MVP[cite: 81].
        'NAME': BASE_DIR / 'db.sqlite3', # Wskazujemy, że plik bazy powstanie bezpośrednio w głównym folderze backendu.
    } # Koniec konfiguracji domyślnej bazy.
} # Koniec słownika baz danych.

AUTH_PASSWORD_VALIDATORS = [ # Mechanizmy zabezpieczające użytkowników przed ustawieniem słabych haseł.
    { # Walidator podobieństwa.
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # Blokuje hasła zbyt podobne do loginu lub e-maila.
    }, # Koniec pierwszego walidatora.
    { # Walidator długości.
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # Blokuje hasła, które mają mniej niż 8 znaków.
    }, # Koniec drugiego walidatora.
    { # Walidator popularności.
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # Odrzuca hasła ze słowników popularnych haseł (np. 12345678).
    }, # Koniec trzeciego walidatora.
    { # Walidator cyfr.
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # Blokuje hasła składające się wyłącznie z cyfr.
    }, # Koniec czwartego walidatora.
] # Koniec listy zabezpieczeń haseł.

LANGUAGE_CODE = 'en-us' # Domyślny język panelu admina (można zmienić na 'pl' w przyszłości).

TIME_ZONE = 'UTC' # Strefa czasowa, w której zapisywane są daty utworzenia (np. przy Created_At).

USE_I18N = True # Włącza system tłumaczeń w Django.

USE_TZ = True # Włącza poprawną obsługę stref czasowych, uwzględniając TIME_ZONE.

STATIC_URL = 'static/' # Prefix w adresie URL, pod którym będą serwowane pliki takie jak obrazki i skrypty.

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # Ustala, że domyślne identyfikatory (ID) w tabelach będą 64-bitowymi liczbami całkowitymi.

AUTH_USER_MODEL = 'users.CustomUser' # DODANE: Nadpisuje domyślnego użytkownika naszym, który zawiera podział na role[cite: 84].

CORS_ALLOWED_ORIGINS = [ # DODANE: Zezwala poniższym stronom na łączenie się z naszym backendem Django.
    "http://localhost:5173", # Dopuszcza lokalny serwer Vite (React), na którym tworzymy aplikację.
    "http://127.0.0.1:5173", # Alternatywny format adresu dla lokalnego serwera Vite.
] # Koniec listy CORS.