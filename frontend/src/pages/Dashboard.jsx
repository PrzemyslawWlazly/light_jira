import React, { useState, useEffect } from 'react'; // Importujemy Reacta oraz hooki: useState (do trzymania danych) i useEffect (do wywoływania kodu po załadowaniu strony)
import { Link } from 'react-router-dom'; // Link działa jak tag <a> w HTML, ale bez przeładowywania strony
import api from '../services/api'; // Importujemy naszą skonfigurowaną wcześniej instancję Axios do łączenia z backendem

function Dashboard() { // Deklarujemy komponent
  const [projects, setProjects] = useState([]); // Tworzymy stan 'projects' (domyślnie pusta tablica) i funkcję do jego aktualizacji
  const [loading, setLoading] = useState(true); // Stan przechowujący informację, czy dane się jeszcze ładują
  const [error, setError] = useState(null); // Stan do ewentualnego chwytania błędów (np. gdy serwer Django nie działa)

  useEffect(() => { // useEffect wykona się automatycznie raz, gdy komponent pojawi się na ekranie
    api.get('projects/') // Pukamy do Django pod adres http://localhost:8000/api/projects/
      .then(response => { // Jeśli serwer odpowie poprawnie...
        setProjects(response.data); // ...zapisujemy pobrane dane (listę projektów) do naszego stanu
        setLoading(false); // ...i wyłączamy ekran ładowania
      })
      .catch(err => { // Jeśli wystąpi błąd (np. brak połączenia)...
        console.error("Błąd pobierania projektów:", err); // ...wypisujemy błąd w konsoli przeglądarki
        setError("Nie udało się załadować projektów."); // ...i ustawiamy przyjazny komunikat dla użytkownika
        setLoading(false); // ...wyłączamy ekran ładowania
      });
  }, []); // Pusta tablica zależności oznacza: wykonaj ten useEffect tylko jeden raz (przy starcie)

  if (loading) return <div>Ładowanie projektów...</div>; // Zanim dane nadejdą, wyświetlamy ten tekst
  if (error) return <div>{error}</div>; // Jeśli był błąd, wyświetlamy go na ekranie

  return ( // Renderujemy właściwy widok HTML
    <div style={{ padding: '20px' }}> {/* Główny kontener z lekkim marginesem wewnątrz */}
      <h1>Wybierz projekt</h1> {/* Nagłówek */}
      
      {/* Używamy CSS Grid do ułożenia projektów w siatce (kafle) */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', gap: '20px' }}>
        
        {projects.map(project => ( // Przechodzimy pętlą po każdym pobranym projekcie
          // Każdy element z pętli musi mieć unikalny klucz (key), u nas to ID projektu
          <div key={project.id} style={{ border: '1px solid #ccc', padding: '15px', borderRadius: '8px' }}>
            <h2>{project.name}</h2> {/* Wyświetlamy nazwę projektu */}
            <p>Klucz: <strong>{project.project_key}</strong></p> {/* Wyświetlamy klucz (np. WEB) */}
            
            {/* Link przenoszący nas do widoku konkretnego projektu (zmienia adres URL) */}
            <Link to={`/project/${project.project_key}`}>
              <button style={{ padding: '10px', cursor: 'pointer' }}>Otwórz projekt</button>
            </Link>
          </div> // Koniec kafelka
        ))} {/* Koniec pętli */}
        
        {/* Obsługa sytuacji, w której baza projektów jest pusta */}
        {projects.length === 0 && <p>Brak projektów. Dodaj je w panelu admina!</p>}
      </div>
    </div> // Koniec głównego kontenera
  );
}

export default Dashboard; // Eksportujemy, by App.jsx mogło to zaimportować