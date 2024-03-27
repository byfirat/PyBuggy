impor sqlite3

baglanti = sqlite3.connect("veritabani.db")
imlec = baglanti.cursor

imlec.execute("""CREATE TABLE ogrenciler (
                isim TEXT,
                soyisim TEXT,
                numara INTEGER
                )""")

imlec.execute("""INSERT INTO ogrenciler VALUES 
                ('Ali', 'Yılmaz', 123),
                ('Ayşe', 'Kaya', 456),
                ('Mehmet', 'Demir', 789)""")

baglanti commit()
baglanti.close()