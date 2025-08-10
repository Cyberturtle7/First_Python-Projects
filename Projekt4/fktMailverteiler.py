def ListeEinlesen():
    mails = []
    f = open("adressen.txt","r")
    inhalt = f.readlines()
    i = 0

    while i < len(inhalt):
        name = inhalt[i]
        name = name[:-1]
        adresse = inhalt[i + 1]
        i += 3
        mails.append((name,adresse))
    f.close()
    return mails

def ListeAnzeigen(mails):
    for mail in mails:
        print(f"Name: {mail[0]}; E-Mail-Adresse: {mail[1]}")
    if len(mails) == 0:
        print("\nKeine Einträge!\n")

def ListeErgaenzen(mails):
    name = input("Der Name:")
    adresse = input("Die E-Mail-Adresse:")
    mails.append((name,adresse))

def ListeSpeichern(mails):
    f = open("adressen.txt","w")
    for mail in mails:
        f.write(mail[0] + "\n")
        f.write(mail[1] + "\n")
        f.write("\n")
    f.close()
