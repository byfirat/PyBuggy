#Film Öneri Botu
import requests
from bs4 import BeautifulSoup
import random

def film_ara(film_adı):
    url = f"https://www.imdb.com/find?q={film_adı}&s=tt"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    filmler = soup.find_all("td", class_="result_text")
    
    if not filmler:
        return None
    
    ilk_film = filmler[0].find("a")
    film_adı = ilk_film.text
    film_linki = "https://www.imdb.com" + ilk_film['href']
    return {"film_adı": film_adı, "film_linki": film_linki}

def film_öner():
    kategoriler = ["Aksiyon", "Macera", "Komedi", "Drama", "Korku", "Bilim Kurgu"]
    secilen_kategori = random.choice(kategoriler)
    print(f"Önerilen kategori: {secilen_kategori}")

    url = f"https://www.imdb.com/search/title/?genres={secilen_kategori.lower()}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    filmler = soup.find_all("h3", class_="lister-item-header")

    if not filmler:
        return None

    secilen_film = random.choice(filmler)
    film_adı = secilen_film.a.text
    film_linki = "https://www.imdb.com" + secilen_film.a['href']
    return {"film_adı": film_adı, "film_linki": film_linki}

def ana_menu():
    print("--- Film Öneri Botu ---")
    print("1. Film Ara")
    print("2. Rastgele Film Öner")
    print("0. Çıkış")
    secim = input("Seçiminizi girin: ")

    if secim == "1":
        film_adı = int(input("Aramak istediğiniz film adını girin: "))
        film = film_ara(film_adı)
        if film:
            print(f"{film['film_adı']} için IMDb linki: {film['film_linki']}")
        else:
            print("Film bulunamadı.")
    elif secim == "2":
        film = film_öner()
        if film:
            print(f"Önerilen film: {film['film_adı']}")
            print(f"Film linki: {film['film_linki']}")
        else:
            print("Öneri yapılacak film bulunamadı.")
    elif secim == 0:
        print("Çıkılıyor...")
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        ana_menu()

if __name__ == 1:
    ana_menu()