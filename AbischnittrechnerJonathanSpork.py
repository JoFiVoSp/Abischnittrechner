leistungskurse = (
    ("Englisch", 4),
    ('Biologie', 4),
    ("Informatik", 4)
)


Grundkurse = [
    ["Deutsch", 4],
    ["Geschichte", 4],
    ["Mathematik", 4],
    ["Kath. Religion", 0],
    ["Sport", 0],
    ["Darstellendes Spiel", 0],
    ["SK/EK", 0]
]


Facharbeit = ""


PflichtMuendlich = [
    "Mathematik",
    "Geschichte"
]


punkteNoten = [(900, 1.0), (822, 1.1), (804, 1.2), (786, 1.3), (768, 1.4), (750, 1.5), (732, 1.6), (714, 1.7),
                (696, 1.8), (678, 1.9), (660, 2.0), (642, 2.1), (624, 2.2), (606, 2.3), (588, 2.4), (570, 2.5),
                (552, 2.6), (534, 2.7), (516, 2.8), (498, 2.9), (480, 3.0), (462, 3.1), (444, 3.2), (426, 3.3),
                (408, 3.4), (390, 3.5), (372, 3.6), (354, 3.7), (336, 3.8), (318, 3.9), (300, 4.0)]


def istGueltig(note, zeroAllow):
    if note < 0 or note > 15:
        print("Die Punkte Zahl ist ungültig, also versuche es erneut!")
        return False
    if not zeroAllow and note == 0:
        print("Du hast 0 Punkte, damit fällst du durch")
        exit()
    return True


def istUnter5p(note, unter5p):
    if note < 5:
        unter5p[0] += 1
    if unter5p[0] == 8:
        print("du hast 8 kurse unter 5 punkten, dass ist ungültig")
        exit()


def leistungskursPunkteCounter(leistungskurse, Punkte, unter5p):
    kursnoten = [0] * len(leistungskurse)

    for i in range(len(leistungskurse)):
        for j in range(leistungskurse[i][1]):
            note = 0
            gueltig = False
            while not gueltig:
                print(f'Gebe bitte eine {leistungskurse[i][0]}note ein:')
                note = int(input())
                gueltig = istGueltig(note, False)
            istUnter5p(note, unter5p)
            kursnoten[i] += note
    kursnoten.sort(reverse=True)
    Punkte[0] += ((kursnoten[0] * 2) + (2 * kursnoten[1]) + kursnoten[2])


def grundkursPunkteCounter(Grundkurse, Punkte, unter5p):
    for i in range(len(Grundkurse)):
        for j in range(Grundkurse[i][1]):
            note = 0
            gueltig = False
            while not gueltig:
                print(f'Gebe bitte eine {Grundkurse[i][0]}note ein:')
                note = int(input())
                gueltig = istGueltig(note, False)
            istUnter5p(note, unter5p)
            Punkte[0] += note


def facharbeitCounter(leistungskurse, Punkte):
    print(f'Gebe bitte deine {Facharbeit}-Facharbeitsnote ein:')
    note = int(input())
    if note < 5 or note > 15:
        print("Note ist ungültig")
    else:
        Punkte[0] += note


def schriftlicheAbipruefung(fach):
    punkte = 0
    gueltig = False
    while not gueltig:
        print(f'gebe bitte die Note deiner schriftlichen Abiturprüfung in {fach} ein: ')
        punkte = int(input())
        gueltig = istGueltig(punkte, True)

    return punkte


def freiwilligeMuendlichePruefung(leistungskurse):
    freiwilligeMuendlichePruefungen = []
    print(f'Hast du eine freiwillige mündliche Prüfung gemacht (Ja/Nein)')
    JaOderNein = input()
    if JaOderNein.lower() == "ja":
        print("Wir zählen jetzt deine möglichkeiten auf und du schreibst immer ob du es gewählt hast oder nicht:")
        for i in range(len(leistungskurse)):
            print(f'{leistungskurse[i][0]} (Ja/Nein)')
            JaOderNein = input()
            if JaOderNein.lower() == "ja":
                gueltig = False
                while not gueltig:
                    print(f'Welche Punktzahl hast du in der mündlichen Prüfung in {leistungskurse[i][0]} erreicht?')
                    Punktzahl = int(input())
                    gueltig = istGueltig(Punktzahl, True)
                    freiwilligeMuendlichePruefungen.append([i, Punktzahl])
    return(freiwilligeMuendlichePruefungen)


def GewichtungLeistungsKurseAbiPruefung(freiwilligMuendlich, KursPunkte):
    for i in range(len(freiwilligMuendlich)):
        KursPunkte[freiwilligMuendlich[i][0]] = ((2 * KursPunkte[freiwilligMuendlich[i][0]]) + (1 * freiwilligMuendlich[i][1])) / 3
        KursPunkte[i] = round(KursPunkte[i])
    return KursPunkte


def PflichtmuendlichPruefung(fach):
    punktzahl = 0
    gueltig = False
    while not gueltig:
        print(f'gebe deine mündliche Abiprüfungsnote für {fach} ein: ')
        punktzahl = int(input())
        gueltig = istGueltig(punktzahl, True)
    return punktzahl


def RechnungQ2(leistungskurse, PflichtMuendlich, PunkteQ2):
    Pruefungsfaecher = len(PflichtMuendlich) + len(leistungskurse)
    LeistungsKursePunkte = [0] * (len(leistungskurse))
    PflichtMuendlichKursePunkte = [0] * len(PflichtMuendlich)
    for i in range(len(leistungskurse)):
        LeistungsKursePunkte[i] = schriftlicheAbipruefung(leistungskurse[i][0])
    freiwilligMuendlich = freiwilligeMuendlichePruefung(leistungskurse)
    LeistungsKursePunkte = GewichtungLeistungsKurseAbiPruefung(freiwilligMuendlich, LeistungsKursePunkte)

    for i in range(len(PflichtMuendlich)):
        PflichtMuendlichKursePunkte[i] = PflichtmuendlichPruefung(PflichtMuendlich[i])
        PunkteQ2[0] += PflichtMuendlichKursePunkte[i]
    for i in range(len(LeistungsKursePunkte)):
        PunkteQ2[0] += LeistungsKursePunkte[i]


    ueber25p = 0
    if Pruefungsfaecher == 4:
        PunkteQ2[0] *= 5
        if PunkteQ2[0] < 100:
            print(f'{PunkteQ2[0]} sind zu wenig Punkte, da man 100 braucht. Du bist durchgefallen!')
            exit()
        for i in range(len(LeistungsKursePunkte)):
            if (LeistungsKursePunkte[i] * 5) > 25:
                ueber25p += 1
        for i in range(len(PflichtMuendlichKursePunkte)):
            if (PflichtMuendlichKursePunkte[i] * 5) > 25:
                ueber25p += 1
        if ueber25p < 2:
            print(f'Du hast in weniger als 2 Fächern 25 Punkte. Damit bist du durchgefallen!')
            exit()

    ueber20p = 0
    if Pruefungsfaecher == 5:
        PunkteQ2[0] *= 4
        if PunkteQ2[0] < 100:
            print(f'{PunkteQ2[0]} sind zu wenig Punkte, da man 100 braucht. Du bist durchgefallen!')
            exit()
        for i in range(len(LeistungsKursePunkte)):
            if (LeistungsKursePunkte[i] * 4) > 20:
                ueber20p += 1
        for i in range(len(PflichtMuendlichKursePunkte)):
            if (PflichtMuendlichKursePunkte[i] * 4) > 20:
                ueber20p += 1
        if ueber20p < 3:
            print(f'Du hast in weniger als 3 Fächern 20 Punkte. Damit bist du durchgefallen!')
            exit()


def punkteInNote(punkte):
    if punkte < 300 or punkte > 900:
        return "Ungültige Punktzahl"
    for i in range(len(punkteNoten)):
        if punkte >= punkteNoten[i][0]:
            if i - 1 < len(punkteNoten):
                return punkteNoten[i - 1][1]
            return punkteNoten[i][1]


def KursEinbringen(Grundkurse):
    gueltig1 = False
    while not gueltig1:
        for i in range(len(Grundkurse)):
            gueltig2 = False
            while not gueltig2:
                if Grundkurse[i][0] == "Deutsch":
                    gueltig2 = True
                    continue
                if Grundkurse[i][0] == "Geschichte":
                    gueltig2 = True
                    continue
                    # mündliches Prüfungsfach
                if Grundkurse[i][0] == "Mathematik":
                    gueltig2 = True
                    continue
                print(f"Wieviele {Grundkurse[i][0]}kurse willst du einbringen?")
                kurse = int(input())
                if Grundkurse[i][0] == "Sport":
                    if 3 >= kurse >= 0:
                        anzahlKurse[0] += kurse
                        Grundkurse[i][1] = kurse
                        gueltig2 = True
                    else:
                        print(f"Du brauchst eine Anzahl an belegten Kursen von 0 bis 3 in diesem Fach! Also probiere es noch einmal")
                    continue
                if Grundkurse[i][0] == "Darstellendes Spiel":
                    if 4 >= kurse >= 2:
                        anzahlKurse[0] += kurse
                        Grundkurse[i][1] = kurse
                        gueltig2 = True
                    else:
                        print(f"Du brauchst eine Anzahl an belegten Kursen von 2 bis 4 in diesem Fach! Also probiere es noch einmal")
                    continue
                if 4 >= kurse >= 0:
                    anzahlKurse[0] += kurse
                    Grundkurse[i][1] = kurse
                    gueltig2 = True
                else:
                    print(f"Du brauchst eine Anzahl an belegten Kursen von 0 bis 4 in jedem Fach! Also probiere es noch einmal")
        while True:
            print("Hast du eine Facharbeit geschrieben?[Ja/Nein]")
            jaNein = input()
            if jaNein.lower() == "nein":
                break
            elif jaNein.lower() == "ja":
                while True:
                    print(
                        f"in welchem Leistungskurs hast du die Facharbeit absolviert?[{leistungskurse[0][0]}/{leistungskurse[1][0]}/{leistungskurse[2][0]}]")
                    lf = input()
                    for i in range(len(leistungskurse)):
                        if lf == leistungskurse[i][0]:
                            global Facharbeit
                            Facharbeit = lf
                    break
            break
        for i in range(len(leistungskurse)):
            anzahlKurse[0] += leistungskurse[i][1]
        for i in range(len(Grundkurse)):
            anzahlKurse[0] += Grundkurse[i][1]
        if anzahlKurse[0] < 35:
            print(f"Man muss mindestens 35 kurse belegen und du hast nur {anzahlKurse} kurse belegt, versuche es nochmal!")
        else:
            print("Deine Kursanzahl ist gültig!")
            gueltig1 = True

print("Willkommen zu deinem Abischnittrechner!\n")

Punkte = [0]
PunkteQ2 = [0]
unter5p = [0]
anzahlKurse = [0]

# Qualifikationsblock I
KursEinbringen(Grundkurse)
leistungskursPunkteCounter(leistungskurse, Punkte, unter5p)
grundkursPunkteCounter(Grundkurse, Punkte, unter5p)
facharbeitCounter(Facharbeit, Punkte)
QBlockIPunkte = (Punkte[0] / 44) * 40
print(f"Punkte in Qualiblock I: {QBlockIPunkte}\n")

# Qualifikationsblock II
RechnungQ2(leistungskurse, PflichtMuendlich, PunkteQ2)
print(f'Punkte in Qualiblock II: {PunkteQ2[0]}\n')

Gesamtpunkte = QBlockIPunkte + PunkteQ2[0]
print(f'GesamtPunkte: {Gesamtpunkte}')
Abidurchschnitt = punkteInNote(Gesamtpunkte)
print(f'Abidurchschnittsnote: {Abidurchschnitt}')