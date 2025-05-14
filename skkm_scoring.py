
def hitung_poin(jenis: str, tingkat: str, peran: str) -> int:
    if jenis == "Lomba":
        if peran == "Juara I" and tingkat == "Nasional":
            return 65
        elif peran == "Juara II" and tingkat == "Nasional":
            return 55
        elif peran == "Peserta" and tingkat == "Lokal":
            return 5
    if jenis == "Seminar":
        if peran == "Peserta":
            return 10
    return 0
