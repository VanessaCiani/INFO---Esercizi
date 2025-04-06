def genera_tabula_recta() -> list[list[str]]:
    matrice = []
    for i in range(0, 26):
        riga = []
        for j in range(0, 26):
            riga.append(chr((i + j) % 26 + ord('A')))
        matrice.append(riga)
    return matrice


def cifra(messaggio: str, chiave: str, tabula_recta: list[list[str]]) -> str:
    """Cifra un messaggio con il cifrario di Vigenère usando la tabula recta.
    
    Args:
        messaggio: Il testo da cifrare (solo lettere A-Z, senza spazi o caratteri speciali).
        chiave: La parola chiave usata per la cifratura.
        tabula_recta: La tabula recta pre-generata.
    
    Returns:
        Il testo cifrato.
    """
    messaggio_cifrato = ""
    for i in range(len(messaggio)):
        indice_riga = ord(messaggio[i]) - 65
        indice_colonna = ord(chiave[i]) - 65
        messaggio_cifrato += tabula_recta[indice_riga][indice_colonna]

    return messaggio_cifrato


def decifra(messaggio_cifrato: str, chiave: str, tabula_recta: list[list[str]]) -> str:
    """Decifra un messaggio cifrato con il cifrario di Vigenère usando la tabula recta.
    
    Args:
        messaggio_cifrato: Il testo cifrato.
        chiave: La parola chiave usata per la cifratura.
        tabula_recta: La tabula recta pre-generata.
    
    Returns:
        Il testo decifrato.
    """
    testo_decifrato = ""
    for i in range(len(messaggio_cifrato)):
        indice_riga = ord(chiave[i]) - 65
        riga = tabula_recta[indice_riga]
        lettera_da_trovare = messaggio_cifrato[i]
        indice_colonna = riga.index(lettera_da_trovare)
        testo_decifrato += chr(indice_colonna + 65)

    return testo_decifrato


def normalizza_testo(testo: str) -> str:
    """Rimuove caratteri non alfabetici e converte tutto in maiuscolo per garantire compatibilità con la cifratura.
    
    Args:
        testo: Il testo di input.
    
    Returns:
        Il testo pulito e in maiuscolo.
    """
    testo = testo.upper()
    testo_normalizzato = ""
    lettere_accentate = {"Á": "A", "È": "E", "Ì": "I", "Ò": "O", "Ú ": "U"}
    for lettera in testo:
        if lettera in lettere_accentate:
            testo_normalizzato += lettere_accentate[lettera]
        elif lettera.isalpha():
            testo_normalizzato += lettera
        else:
            print(f"Ho saltato il carattere non alfabetico '{lettera}'.")
    return testo_normalizzato


def estendi_chiave(chiave: str, lunghezza: int) -> str:
    """Espande la chiave fino alla lunghezza richiesta ripetendola ciclicamente.
    
    Args:
        chiave: La parola chiave originale.
        lunghezza: La lunghezza del testo da cifrare/decifrare.
    
    Returns:
        La chiave estesa.
    """
    chiave_estesa = ""
    for i in range(lunghezza):
        chiave_estesa += chiave[i % len(chiave)]
    return chiave_estesa


def main():
    """Funzione principale che gestisce l'interazione con l'utente."""
    print("Cifrario di Vigenère")
    
    tabula_recta = genera_tabula_recta()
    for riga in tabula_recta:
        print(f"{riga}")

    scelta = input("Vuoi cifrare (C) o decifrare (D)? ").strip().upper()

    if scelta == "C":
        messaggio = input("Inserisci il messaggio da cifrare: ")
        chiave = input("Inserisci la chiave: ")
        messaggio = normalizza_testo(messaggio)
        chiave = normalizza_testo(chiave)
        chiave_estesa = estendi_chiave(chiave, len(messaggio))
        testo_cifrato = cifra(messaggio, chiave_estesa, tabula_recta)
        print(f"Testo cifrato: {testo_cifrato}")

    elif scelta == "D":
        messaggio_cifrato = input("Inserisci il messaggio cifrato: ")
        chiave = input("Inserisci la chiave: ")
        messaggio_cifrato = normalizza_testo(messaggio_cifrato)
        chiave = normalizza_testo(chiave)
        chiave_estesa = estendi_chiave(chiave, len(messaggio_cifrato))
        testo_decifrato = decifra(messaggio_cifrato, chiave_estesa, tabula_recta)
        print(f"Testo decifrato: {testo_decifrato}")

    else:
        print("Scelta non valida.")


if __name__ == "__main__":
    main()