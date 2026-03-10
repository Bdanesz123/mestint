class NKiralyno:
    def __init__(self, n):
        # Az állapot formátuma:
        # (
        #   [0, 0, 1, 0],   # 0. sor
        #   [1, 0, 0, 0],   # 1. sor
        #   [0, 0, 0, 0],   # 2. sor
        #   [0, 1, 0, 0]    # 3. sor
        # )
        #
        # 1 = királynő
        # 0 = üres mező
        self.N = n
        self.kezdő = tuple([ [0] * n for _ in range(n) ])

    def célteszt(self, a):
        # Akkor célállapot, ha pontosan N királynő van a táblán
        db = 0
        for sor in a:
            db += sum(sor)
        return db == self.N

    def _másolat(self, a):
        # tuple-ben lévő listák másolása
        return tuple(sor.copy() for sor in a)

    def kiralynok_szama(self, a):
        db = 0
        for sor in a:
            db += sum(sor)
        return db

    def biztonsagos(self, a, sor, oszlop):
        # Van-e már királynő ugyanabban az oszlopban?
        for i in range(self.N):
            if a[i][oszlop] == 1:
                return False

        # Van-e már királynő ugyanabban a sorban?
        for j in range(self.N):
            if a[sor][j] == 1:
                return False

        # Bal felső átló
        i, j = sor - 1, oszlop - 1
        while i >= 0 and j >= 0:
            if a[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Jobb felső átló
        i, j = sor - 1, oszlop + 1
        while i >= 0 and j < self.N:
            if a[i][j] == 1:
                return False
            i -= 1
            j += 1

        # Bal alsó átló
        i, j = sor + 1, oszlop - 1
        while i < self.N and j >= 0:
            if a[i][j] == 1:
                return False
            i += 1
            j -= 1

        # Jobb alsó átló
        i, j = sor + 1, oszlop + 1
        while i < self.N and j < self.N:
            if a[i][j] == 1:
                return False
            i += 1
            j += 1

        return True

    def rákövetkez(self, a):
        # A következő szintre úgy lépünk, hogy a következő üres sorba
        # megpróbálunk egy királynőt lerakni minden lehetséges oszlopba
        gyerekek = []

        eddigi_kiralynok = self.kiralynok_szama(a)

        # ha már N királynő fent van, nincs tovább
        if eddigi_kiralynok >= self.N:
            return gyerekek

        uj_sor = eddigi_kiralynok

        for oszlop in range(self.N):
            if self.biztonsagos(a, uj_sor, oszlop):
                uj = self._másolat(a)
                uj[uj_sor][oszlop] = 1
                gyerekek.append(uj)

        return gyerekek


def szelessegi_kereses(feladat):
    nyilt = [feladat.kezdő]
    megoldasok = []

    while len(nyilt) > 0:
        aktualis = nyilt.pop(0)

        if feladat.célteszt(aktualis):
            megoldasok.append(aktualis)
            continue

        gyerekek = feladat.rákövetkez(aktualis)
        nyilt.extend(gyerekek)

    return megoldasok


def allapot_kiirasa(a):
    for sor in a:
        print(" ".join("Q" if elem == 1 else "." for elem in sor))
    print()


if __name__ == "__main__":
    feladat = NKiralyno(4)

    megoldasok = szelessegi_kereses(feladat)

    print(f"Megoldások száma: {len(megoldasok)}\n")

    for i, megoldas in enumerate(megoldasok, start=1):
        print(f"{i}. megoldás:")
        allapot_kiirasa(megoldas)