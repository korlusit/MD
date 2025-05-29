import sqlite3
import re

baglanti=sqlite3.connect("database.db")
islem = baglanti.cursor()
baglanti.commit()

def id_kayitcek(sutun, tablo, idf):
            idf = idf
            sorgu = "select {} from {} where id = ?".format(sutun, tablo)
            islem.execute(sorgu, (idf,))
            cikti = islem.fetchone()
            if cikti:
                return cikti[0]
            else:
                return 0

def normalize_gsm(numara: str) -> str:
    """Tüm numara formatlarını normalize eder."""
    if not numara:
        return ""
    temiz = re.sub(r'\D', '', numara)
    if temiz.startswith("0"):
        temiz = temiz[1:]
    if temiz.startswith("90") and len(temiz) > 10:
        temiz = temiz[2:]
    return temiz

def gsm_kayitcek(sutun, tablo, gsm):
    g_normalize = normalize_gsm(gsm)

    # Veritabanındaki tüm kayıtları çek (numarayı da al!)
    sorgu = f"SELECT {sutun}, gsm FROM {tablo}"
    islem.execute(sorgu)
    kayitlar = islem.fetchall()

    for satir in kayitlar:
        deger, gsm_kayitli = satir
        if normalize_gsm(gsm_kayitli) == g_normalize:
            return deger

    return 0  # eşleşme yoksa
