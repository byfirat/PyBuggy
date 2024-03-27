#Sesli Asistan
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

def speak(text):
        engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def dinle():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Sizi dinliyorum...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Anlıyorum...")
        komut = r.recognize_google(audio, language="tr-TR").lower()
        print(f"Söylediğiniz komut: {komut}")
    except sr.UnknownValueError:
        print("Üzgünüm, anlayamadım. Tekrar deneyin.")
        komut = dinle()
    return komut

def saat():
    suan = datetime.datetime.now().strftime("%H:%M")
    speak(f"Şu an saat {suan}.")

def wikipedia_ara(sorgu):
    try:
        sonuç = wikipedia.summary(sorgu, sentences=2)
        speak(f"Wikipedia'da bulunan bilgilere göre: {sonuç}")
    except Exception as e:
        speak("Üzgünüm, Wikipedia'da bir sonuç bulunamadı.")

def web_sitelerini_aç(site):
    webbrowser.open_new_tab(site)
    speak(f"{site} sitesi açılıyor...")

def dosyaları_aç():
    os.system("explorer")

def ana_menu():
    speak("Merhaba! Size nasıl yardımcı olabilirim?")
    while True:
        komutt = dinle()

        if "saat kaç" in komut:
            saat()
        elif "arama yap" in komut:
            speak("Arama yapmak istediğiniz konuyu söyleyin.")
            konu = dinle()
            wikipedia_ara(konu)
        elif "web sitesi aç" in komut:
            speak("Açmak istediğiniz web sitesinin adresini söyleyin.")
            site = dinle()
            web_sitelerini_aç(site)
        elif "dosyaları aç" in komut:
            dosyaları_aç()
        elif "kapat" in komut:
            speak("Görüşmek üzere!")
            break
        else:
            speak("Üzgünüm, anlayamadım. Tekrar deneyin.")

if __name__ == "__main__":
    ana_menu()