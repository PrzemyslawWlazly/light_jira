import React, { useState, useEffect } from 'react'; // Podstawowe importy Reacta
import { useParams, Link } from 'react-router-dom'; // useParams wyciąga zmienne z paska adresu URL
import api from '../services/api'; // Nasz komunikator z backendem

function ProjectView() { // Definicja komponentu
  const { projectKey } = useParams(); // Wyciągamy 'projectKey' ze ścieżki (czyli to, co jest po /project/...)
  const [issues, setIssues] = useState([]); // Stan na pobrane z backendu zadania
  const [loading, setLoading] = useState(true); // Stan ładowania
  const [error, setError] = useState(null); // Stan błędów

useEffect(() => {
    // ZMIANA: Zamiast pukać do samego 'issues/', dodajemy parametr URL za pomocą zmiennej z adresu (projectKey)
    // Używamy tu tzw. template literals z JavaScriptu (odwrotne apostrofy ` ` zamiast cudzysłowów)
    api.get(`issues/?projectKey=${projectKey}`) 
      .then(response => {
        // Teraz Django odsyła nam gotową, wyselekcjonowaną listę!
        // Zapisujemy ją bezpośrednio do stanu, bez żadnego dodatkowego kombinowania.
        setIssues(response.data); 
        setLoading(false); 
      })
      .catch(err => { 
        console.error("Błąd pobierania zadań:", err); 
        setError("Nie udało się załadować zadań."); 
        setLoading(false); 
      });
  }, [projectKey]);

  
  if (loading) return <div>Ładowanie danych projektu...</div>; // Ekran ładowania
  if (error) return <div>{error}</div>; // Ekran błędu

  return ( // Generowanie widoku HTML
    <div style={{ padding: '20px' }}> {/* Główny div marginesami */}
      {/* Przycisk powrotu do strony głównej */}
      <Link to="/dashboard" style={{ textDecoration: 'none', color: 'blue' }}>&larr; Wróć do projektów</Link>
      
      <h1 style={{ marginTop: '20px' }}>Tablica Projektu: {projectKey}</h1> {/* Dynamiczny nagłówek z kluczem projektu */}
      
      <div style={{ marginTop: '20px' }}>
        <h2>Wszystkie Zadania (Surowa lista)</h2> {/* Sekcja z zadaniami */}
        
        {/* Jeśli tablica z zadaniami jest pusta, wyświetl komunikat */}
        {issues.length === 0 ? (
          <p>Ten projekt nie ma jeszcze żadnych zadań.</p>
        ) : (
          // W przeciwnym razie renderuj listę <ul>
          <ul style={{ listStyle: 'none', padding: 0 }}>
            {issues.map(issue => ( // Pętla po zadaniach
              // Wyświetlamy proste kafelki dla każdego zadania (klucz + tytuł + status)
              <li key={issue.id} style={{ border: '1px solid #ddd', padding: '10px', marginBottom: '10px', borderRadius: '4px' }}>
                <strong>[{issue.issue_key}]</strong> {issue.title} {/* Klucz np. WEB-1 i tytuł */}
                <span style={{ float: 'right', backgroundColor: '#eee', padding: '2px 8px', borderRadius: '10px', fontSize: '0.8em' }}>
                  {issue.status} {/* Wyświetlenie statusu (np. TO_DO) po prawej stronie */}
                </span>
              </li> // Koniec pojedynczego elementu listy
            ))}
          </ul> // Koniec listy
        )}
      </div>
    </div> // Koniec głównego div'a
  );
}

export default ProjectView; // Udostępniamy komponent dla routingu