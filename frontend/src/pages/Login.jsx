import React from 'react'; // Importujemy główną bibliotekę React

function Login() { // Deklarujemy komponent funkcyjny o nazwie Login
  return ( // Zwracamy kod JSX, który zostanie wyrenderowany w przeglądarce
    <div> {/* Główny kontener widoku */}
      <h1>Logowanie do light_jira</h1> {/* Nagłówek strony */}
      <p>Wkrótce dodamy tu formularz logowania.</p> {/* Tymczasowy tekst informacyjny */}
    </div> // Zamykamy główny kontener
  ); // Koniec zwracania JSX
} // Koniec definicji funkcji

export default Login; // Eksportujemy komponent, aby można go było użyć w App.jsx