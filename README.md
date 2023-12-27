# Auctions
In questa repo è presente un progetto che verte nella creazione di un e-commerce di oggetti tramite un sistema ad aste, implementato tramite il framework ***Django***.

## Versione 1
Nella prima versione il sito viene implementato con un'architettura monolitica, dove tutte le funzionalità sono inserito in una sola applicaziome e il database è in comune.

## Versione 2
Nella seconda versione, vengono sfruttate al massimo le potenzialità fornite da Django in questo modo è stato possibile creare un unico progetto con all'interno tre applicazioni separate, le applicazioni condividevano lo stesso database ma le tabelle erano separate e le responsabilità su di esse ricadevano all'applicazione specifica.

## Versione 3
Nella terza verisione tramite l'ausilio di *rest_framework* e di *corsheaders* è stato utilizzato un approccio a **microservizi**. In questo scenario sono state definiti tre progetti separati ognuno con un proprio database e la comunicazione tra i vari servizi è stata gestita tramite REST API.

# Visione Applicazione 

