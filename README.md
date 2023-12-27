# Auctions
In questa repo è presente un progetto che verte nella creazione di un e-commerce di oggetti tramite un sistema ad aste, implementato tramite il framework ***Django***.

## Versione 1
Nella prima versione il sito viene implementato con un'architettura monolitica, dove tutte le funzionalità sono inserito in una sola applicaziome e il database è in comune.

## Versione 2
Nella seconda versione, vengono sfruttate al massimo le potenzialità fornite da Django in questo modo è stato possibile creare un unico progetto con all'interno tre applicazioni separate, le applicazioni condividevano lo stesso database ma le tabelle erano separate e le responsabilità su di esse ricadevano all'applicazione specifica.

## Versione 3
Nella terza verisione tramite l'ausilio di *rest_framework* e di *corsheaders* è stato utilizzato un approccio a **microservizi**. In questo scenario sono state definiti tre progetti separati ognuno con un proprio database e la comunicazione tra i vari servizi è stata gestita tramite REST API.

# Visione Applicazione 
La prima schermata che si avrà davanti all'avvio dell'applicazione è la schermata di login
<br/> <br/> 
<img src="https://github.com/Raciti/Auction/blob/main/Img/login.png" alt="Img1" width="300"/>
<br/> <br/>  <br/> 
Se non si dovesse possedere un account cliccando su registrati l'utente verrà reindirizzato alla schermata di registrazione
<br/> <br/> 
<img src="https://github.com/Raciti/Auction/blob/main/Img/register.png" alt="Img0" width="300"/>  
<br/> <br/> <br/> 
Una volta che l'utente si ha effettuato l'accesso si troverà nella home
<br/> <br/> 
<img src="https://github.com/Raciti/Auction/blob/main/Img/home.png" alt="Img1" width="300"/>
