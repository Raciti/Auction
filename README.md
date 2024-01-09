🇮🇹🇮🇹🇮🇹
# Auctions
In questa repo è presente un progetto che verte nella creazione di un e-commerce di oggetti tramite un sistema ad aste, implementato tramite il framework ***Django***.

## Versione 1
Nella prima versione il sito viene implementato con un'architettura monolitica, dove tutte le funzionalità sono inserito in una sola applicaziome e il database è in comune.

## Versione 2
Nella seconda versione, vengono sfruttate al massimo le potenzialità fornite da Django in questo modo è stato possibile creare un unico progetto con all'interno tre applicazioni separate, le applicazioni condividevano lo stesso database ma le tabelle erano separate e le responsabilità su di esse ricadevano all'applicazione specifica.

## Versione 3
Nella terza versione tramite l'ausilio di *rest_framework* e di *corsheaders* è stato utilizzato un approccio a **microservizi**. In questo scenario sono state definiti tre progetti separati ognuno con un proprio database e la comunicazione tra i vari servizi è stata gestita tramite REST API.

# FRONTEND
## Fase iniziale
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

## Oggetti
Una volta effettuato l'accesso è possibile usufruire delle funzionalità del sito web, sono disponibili tre sezioni di visualizzazione degli oggetti in vendita 
<div style="display: flex; justify-content: space-between;">
    <img src="https://github.com/Raciti/Auction/blob/main/Img/tutte_aste.png" alt="Img0" width="300"/>
    <img src="https://github.com/Raciti/Auction/blob/main/Img/aste_attive.png" alt="Img1" width="300"/>
    <img src="https://github.com/Raciti/Auction/blob/main/Img/aste_giorno.png" alt="Img2" width="300"/>
</div>
<br/> <br/> 
Cliccando sul nome di un oggetto non ancora scaduto si verrà reindirizzati nella pagina per effettuare l'offerta
<br/> <br/> <br/> 
<img src="https://github.com/Raciti/Auction/blob/main/Img/dettaglio_prodotto.png" alt="Img0" width="300"/>
<br/> <br/> 
Cliccando su "Fai un'offerta" sarà possibile fare un'offerta
<br/> <br/> <br/> 
<div style="display: flex; justify-content: space-between;">
    <img src="https://github.com/Raciti/Auction/blob/main/Img/modifica_offerta.png" alt="Img0" width="300"/>
    <img src="https://github.com/Raciti/Auction/blob/main/Img/aggiornamento_offerta.png" alt="Img1" width="300"/>
</div>

## Sezione Utente
Cliccando sul proprio nome in alto a destra si reinderizza alla pagina del profilo utente
<br/> <br/> <br/> 
<img src="https://github.com/Raciti/Auction/blob/main/Img/user.png" alt="Img0" width="300"/>
<br/> <br/> 
Dove vengono mostrate: **informazioni account**, ** oggetti vinti**, ** privileggi sistema** e ** permessi **.
## Assistenza
Cliccando su serve assistenza in basso a destra sarà possibile scrivere un messaggio agli admin, se si è admin nella pagine del proprio profilo vi sarà la sezione per leggere i messaggi.
<br/> <br/> <br/> 
<div style="display: flex; justify-content: space-between;">
    <img src="https://github.com/Raciti/Auction/blob/main/Img/messaggio.png" alt="Img0" width="300"/>
    <img src="https://github.com/Raciti/Auction/blob/main/Img/conferma_messaggio.png" alt="Img1" width="300"/>
</div>
<br/> <br/>
Gli admin avranno 
<img src="https://github.com/Raciti/Auction/blob/main/Img/lista_messaggi.png" alt="Img0" width="300"/>


🇬🇧🇬🇧🇬🇧
# Auctions

This repository contains a project focused on creating an e-commerce platform for items through an auction system, implemented using the ***Django*** framework.

## Version 1

In the first version, the site is implemented with a monolithic architecture, where all functionalities are placed within a single application, and the database is shared.

## Version 2

In the second version, the full potential of Django is leveraged to create a single project with three separate applications. While the applications share the same database, the tables are separate, and responsibilities are assigned to each specific application.

## Version 3

In the third version, with the help of *rest_framework* and *corsheaders*, a **microservices** approach is employed. In this scenario, three separate projects are defined, each with its own database, and communication between the various services is handled through REST APIs.

# Application Overview

## Initial Phase

The first screen encountered upon launching the application is the login screen.
<br/> <br/> 
<img src="https://github.com/Raciti/Auction/blob/main/Img/login.png" alt="Img1" width="300"/>
<br/> <br/>  <br/> 
If the user does not have an account, clicking on "Register" redirects them to the registration screen.
<br/> <br/> 
<img src="https://github.com/Raciti/Auction/blob/main/Img/register.png" alt="Img0" width="300"/>  
<br/> <br/> <br/> 
Once the user logs in, they will be on the home page.
<br/> <br/> 
<img src="https://github.com/Raciti/Auction/blob/main/Img/home.png" alt="Img1" width="300"/>

## Items

After logging in, users can make use of the website's features, with three sections available for viewing items for sale.

<div style="display: flex; justify-content: space-between;">
    <img src="https://github.com/Raciti/Auction/blob/main/Img/tutte_aste.png" alt="Img0" width="300"/>
    <img src="https://github.com/Raciti/Auction/blob/main/Img/aste_attive.png" alt="Img1" width="300"/>
    <img src="https://github.com/Raciti/Auction/blob/main/Img/aste_giorno.png" alt="Img2" width="300"/>
</div>
<br/> <br/> 
Clicking on the name of an item not yet expired redirects the user to the page to place a bid.
<br/> <br/> <br/> 
<img src="https://github.com/Raciti/Auction/blob/main/Img/dettaglio_prodotto.png" alt="Img0" width="300"/>
<br/> <br/> 
By clicking on "*Place a Bid*", users can make an offer.
<br/> <br/> <br/> 
<div style="display: flex; justify-content: space-between;">
    <img src="https://github.com/Raciti/Auction/blob/main/Img/modifica_offerta.png" alt="Img0" width="300"/>
    <img src="https://github.com/Raciti/Auction/blob/main/Img/aggiornamento_offerta.png" alt="Img1" width="300"/>
</div>
## User Section
Clicking on the user's name in the top right redirects to the user profile page.
<br/> <br/> <br/> 
<img src="https://github.com/Raciti/Auction/blob/main/Img/user.png" alt="Img0" width="300"/>
<br/> <br/> 
This page displays: **account information**, **won items**, **system privileges**, and **permissions**.
## Support

Clicking on "Need Assistance" at the bottom right allows users to write a message to the admins. If the user is an admin, the profile page will have a section to read messages.
<br/> <br/> <br/> 
<div style="display: flex; justify-content: space-between;">
    <img src="https://github.com/Raciti/Auction/blob/main/Img/messaggio.png" alt="Img0" width="300"/>
    <img src="https://github.com/Raciti/Auction/blob/main/Img/conferma_messaggio.png" alt="Img1" width="300"/>
</div>
<br/> <br/>
Admins will have a
<img src="https://github.com/Raciti/Auction/blob/main/Img/lista_messaggi.png" alt="Img0" width="300"/>
