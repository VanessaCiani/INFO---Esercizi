import random

VUOTO = " "

def crea_giocatori():
    giocatori = {}
    nome1 = input("Scrivi il tuo nome: ")
    giocatori[nome1] = {"Simbolo": 'X', "Punteggio": 0}
    print("---I DUE NOMI NON DEVONO ESSERE UGUALI!---")
    nome2 = input("Scrivi il tuo nome: ")
    
    if nome1 == nome2:
        print("I nomi non devono essere uguali! Riprova.")
        return None 
    
    giocatori[nome2] = {"Simbolo": 'O', "Punteggio": 0}
    return giocatori

def inizializza_tabellone() -> list[list[str]]:
    """Crea e restituisce una matrice 3x3 vuota."""
    matrice = []
    for i in range(3):
        tabellone = []
        matrice.append(tabellone)
        for _ in range(3):
            matrice[i].append(VUOTO)
    return matrice

def mostra_tabellone(tabellone: list[list[str]]) -> None:
    """Stampa la griglia di gioco in modo leggibile."""
    print()
    for i in range(3):
        print(" | ".join(tabellone[i]))
        if i < 2:
            print("—————————")
    print()

def gioca_turno(tabellone: list[list[str]], giocatore: str, simbolo: str) -> None:
    """Gestisce l'input del giocatore e aggiorna il tabellone."""
    while True:
        riga = int(input(f"{giocatore}, scegli la riga (0, 1, 2): "))
        colonna = int(input(f"{giocatore}, scegli la colonna (0, 1, 2): "))
        if tabellone[riga][colonna] == VUOTO:
            tabellone[riga][colonna] = simbolo
            break
        else:
            print("Questa posizione nel tabellone è già occupata! Scegline un'altra...")

def verifica_vittoria(tabellone: list[list[str]]) -> bool:
    """Verifica se c'è un vincitore."""
    # Controllo righe
    for i in range(3):
        if tabellone[i][0] == tabellone[i][1] == tabellone[i][2] and tabellone[i][0] != VUOTO:
            return True
    # Controllo colonne
    for j in range(3):
        if tabellone[0][j] == tabellone[1][j] == tabellone[2][j] and tabellone[0][j] != VUOTO:
            return True
    # Controllo diagonali
    if tabellone[0][0] == tabellone[1][1] == tabellone[2][2] and tabellone[0][0] != VUOTO:
        return True
    if tabellone[0][2] == tabellone[1][1] == tabellone[2][0] and tabellone[0][2] != VUOTO:
        return True
    return False

def aggiorna_punteggio(giocatori: dict, vincitore: str) -> None:
    """Aggiorna il punteggio del giocatore vincente."""
    if vincitore in giocatori:
        giocatori[vincitore]["Punteggio"] += 1

def partita(giocatori: dict) -> None:
    """Gestisce il flusso principale del gioco, alternando i turni e determinando il risultato finale."""
    tabellone = inizializza_tabellone()
    turno = 0
    while turno < 9:
        if turno % 2 == 0:  #Quando è uguale a 0 tocca al Giocatore1
            giocatore_attuale = list(giocatori.keys())[0]
            simbolo = giocatori[giocatore_attuale]["Simbolo"]
        else:  #Quando è uguale a 1 tocca al Giocatore2
            giocatore_attuale = list(giocatori.keys())[1]
            simbolo = giocatori[giocatore_attuale]["Simbolo"]
        
        mostra_tabellone(tabellone)
        gioca_turno(tabellone, giocatore_attuale, simbolo)
        
        if verifica_vittoria(tabellone):
            mostra_tabellone(tabellone)
            print(f"{giocatore_attuale} ha vinto!")
            aggiorna_punteggio(giocatori, giocatore_attuale)
            break
        turno += 1
    if turno == 9:
        mostra_tabellone(tabellone)
        print("È un pareggio!")

def main() -> None:
    """Gestisce la sfida al meglio dei tre e dichiara il vincitore finale."""
    giocatori = crea_giocatori()
    
    vittorie_giocatore1 = 0
    vittorie_giocatore2 = 0
    
    while vittorie_giocatore1 < 2 and vittorie_giocatore2 < 2:
        partita(giocatori)
        giocatore1 = list(giocatori.keys())[0]
        giocatore2 = list(giocatori.keys())[1]
        
        print(f"Il Giocatore {giocatore1} ha totalizzato: {giocatori[giocatore1]['Punteggio']} Punti.")
        print(f"Il Giocatore {giocatore2} ha totalizzato: {giocatori[giocatore2]['Punteggio']} Punti.")
        
        if giocatori[giocatore1]["Punteggio"] > giocatori[giocatore2]["Punteggio"]:
            vittorie_giocatore1 += 1
        elif giocatori[giocatore1]["Punteggio"] < giocatori[giocatore2]["Punteggio"]:
            vittorie_giocatore2 += 1
    
    if vittorie_giocatore1 > vittorie_giocatore2:
        print(f"{giocatore1} ha vinto la sfida!")
    elif vittorie_giocatore1 < vittorie_giocatore2:
        print(f"{giocatore2} ha vinto la sfida!")
    else:
        print("La sfida è terminata in pareggio!")

main()
