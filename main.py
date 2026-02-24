# Kancsók kapacitása
kapacitasok = (3, 5, 8)

# Kezdeti állapot (3L, 5L, 8L)
kezdo_allapot = (0, 0, 8)

# Cél liter
cel = 4


def kovetkezo_allapotok(allapot):
    uj_allapotok = []
    kancsok = list(allapot)

    # Átöntés műveletek (i -> j)
    for i in range(3):
        for j in range(3):
            if i == j:
                continue

            if kancsok[i] == 0:
                continue  # nincs mit önteni

            if kancsok[j] == kapacitasok[j]:
                continue  # nincs hely a célkancsóban

            uj = list(kancsok)
            atontheto = min(kancsok[i], kapacitasok[j] - kancsok[j])
            uj[i] -= atontheto
            uj[j] += atontheto
            uj_allapotok.append(tuple(uj))

    return uj_allapotok


def rekurziv_kereses(aktualis_allapot, latogatott, ut):
    # Cél ellenőrzése
    if cel in aktualis_allapot:
        return ut, aktualis_allapot

    # Következő lépések bejárása
    for uj_allapot in kovetkezo_allapotok(aktualis_allapot):
        if uj_allapot in latogatott:
            continue

        latogatott.add(uj_allapot)
        eredmeny = rekurziv_kereses(uj_allapot, latogatott, ut + [uj_allapot])
        if eredmeny is not None:
            return eredmeny

    return None


def megoldas():
    latogatott = {kezdo_allapot}
    eredmeny = rekurziv_kereses(kezdo_allapot, latogatott,[])

    if eredmeny is None:
        print("Nincs megoldás.")
        return

    ut, vegallapot = eredmeny
    print("Megoldás lépései:")
    for lepes in ut:
        print(lepes)
    print("Végállapot:", vegallapot)


if __name__ == '__main__':
    megoldas()
