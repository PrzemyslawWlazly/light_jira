import React from 'react'; // Importujemy bibliotekę React, która jest sercem naszego frontendu
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'; // Importujemy klocki do budowy nawigacji

import Login from './pages/Login'; // Podłączamy nasz plik z ekranem logowania
import Dashboard from './pages/Dashboard'; // Podłączamy nasz widok wyświetlający projekty
import ProjectView from './pages/ProjectView'; // Podłączamy widok konkretnej tablicy Scrum

function App() { // Deklarujemy główny komponent funkcyjny całej naszej aplikacji
  return ( // Zaczynamy instrukcję zwrotną, która wygeneruje kod HTML na ekranie
    <Router> {/* Router oplata całą aplikację i nasłuchuje zmian w pasku adresu (URL) */}
      <div className="app-container"> {/* Tworzymy główny tag kontenera z klasą dla przyszłych stylów CSS */}
        <Routes> {/* Komponent Routes działa jak inteligentny przełącznik ekranów */}
          <Route path="/" element={<Navigate to="/dashboard" replace />} /> {/* Odwiedziny na stronie głównej automatycznie przekierowują do panelu */}
          <Route path="/login" element={<Login />} /> {/* Adres /login wyświetla użytkownikowi komponent logowania */}
          <Route path="/dashboard" element={<Dashboard />} /> {/* Adres /dashboard wyświetla kafelki z projektami */}
          <Route path="/project/:projectKey" element={<ProjectView />} /> {/* Adres ze zmienną (np. /project/WEB) przekazuje ten klucz do tablicy */}
        </Routes> {/* Zamykamy blok naszych wszystkich zdefiniowanych ścieżek */}
      </div> {/* Zamykamy główny tag kontenera wizualnego aplikacji */}
    </Router> // Koniec głównego elementu (tutaj zwykły komentarz jest bezpieczny i nie psuje JSX)
  ); // Koniec bloku return
} // Zamknięcie nawiasu funkcji App

export default App; // Eksportujemy komponent, aby React mógł go załadować jako punkt startowy