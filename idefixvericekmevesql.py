import requests
from bs4 import  BeautifulSoup
import sqlite3
import time
import random
con = sqlite3.connect("C:/Users/gold/Desktop/prestij-yayinlari-fullveri.db")
cursor = con.cursor()
#HEADER
hdr = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

#URL
link= "https://www.idefix.com/kategori/Kitap/Prestij-Kitaplari/grupno=00062"

def tabloolustur():
	cursor.execute("CREATE TABLE IF NOT EXISTS Idefix (kitapad TEXT,yazarad TEXT,fiyat TEXT)")
tabloolustur()
for i in range(1,9):
	url_value =link+str(i)
	r = requests.get(url_value,headers=hdr,verify=False)
	soup = BeautifulSoup(r.content,"html.parser")
	#Fiyat
	kitap_fiyat = soup.find_all("div",{"class":"box-line-4"})
	#Kitap isimleri
	kitap_isim = soup.find_all("div",{"class":"box-title"})
	#Yazarlar
	kitap_yazar = soup.find_all("div",{"class":"box-line-2 pName"})	



	for j in range(len(kitap_isim)):
		#İsim
		kitapad = kitap_isim[j].text.replace("\n","")
		#Yazar
		yazarad =kitap_yazar[j].text
		#Fiyat
		text = kitap_fiyat[j].text.replace("\n"," ")
		fiyat = text[len(text)-10:len(text)-5].replace(" ","").replace(",",".")
		#sqlite ekle
		cursor.execute("INSERT INTO Idefix (kitapad,yazarad,fiyat) VALUES(?,?,?)",(kitapad,yazarad,fiyat))
	time.sleep(random.randint(1,10))
con.commit()
con.close()
"""

		isim,yazar,yayıncı,basim_yili,adedi =giris_List[0],giris_List[1],giris_List[2],giris_List[3],giris_List[4]
		cursor.execute("INSERT INTO KitapVeri (isim,yazar,yayıncı,basim_yili,adedi) VALUES(?,?,?,?,?)",(isim,yazar,yayıncı,basim_yili,adedi))
"""


