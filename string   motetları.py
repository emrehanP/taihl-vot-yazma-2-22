okul = "sancaktEPe tekNOLOji imamhatip Anadolu liSEsi"

# tüm karakterleri büyük yapma

print(okul.upper())

#tümkarakterleri küçük yapma

print(okul.lower())

#her kelimenin ilk harfini büyük yapma

print(okul.title())

#karakter dizisinin ilk karakterini büyük diğer karakterlerini küçük yapma

print(okul.capitalize())

#belirli bir ifadenin kaç defa yer aldığını bulalım

print(okul.count("i"))

#velirli bir ifadenin kaç tanre olduğuna bakar

makale = "Teknolojinin hızla geliştiği ve günlük hayatımızın her alanına sirayetettiği bir çağda kalkınma ile teknolojik gelişme arasında doğru orantı kurmakmümkündür Bu yüzden teknoloji okuryazarlığı ve teknoloji öğretimi kavramları giderek önem kazanmıştı Kalkınmış ülkeler eğitim programlarını teknolojiye çabuk uyum sağlayabilenteknolojiyi verimli kullanabilen ve yeni teknolojiler üretebilen bireyler yetiştirebilmeyi hedefleyecek şekilde geliştirmişlerdirBu çalışmada ABDİngiltere ve Fransa gibi kalkınmış ülkelerde uygulanan eğitim programları içerisinde teknoloji öğretiminin yerinin saptaması veTürkiye’deki mevcut durumla karşılaştırılması amaçlanmıştır Yapılan karşılaştırmada adı geçen ülkelerin teknoloji öğretimi açısından genel bir bilinç geliştirdikleri ve eğitim sistemlerini de buna göre geliştirdikleri görülmüştürTürkiyede ise bu bilinç nispeten geç gelişmiş ve diğer örneklerde olduğu gibisivil kurum ve kuruluşlardan yeterince destek alınamamıştır Ayrıca teknolojidersleriyle diğer dersler arasındaki yatay kaynaşıklığın yaratılması açısından dafarklılıklar gözlenmiştir"

print(makale.lower().count("teknoloji"))


#soldaki ve sağdaki boşluk karakterlerini temiz leyelim
ad = input("adınız: ")
print(ad.strip()+"|")

#soldaki ve sağdaki karaklerleri temizleyelim

urun_kodu = "HEP20221022"

print(urun_kodu.strip("HEP"))

#SOLDAKİ, BOŞLUK VVEYA BELİRLİ İFADEUYİ temizlem


print(ad + "|")
print(ad.lstrip()+"|")
print(urun_kodu.lstrip("HEP"))


#Sağdaki, BOŞLUK VVEYA BELİRLİ İFADEUYİ temizlem


print(ad + "|")
print(ad.rstrip()+"|")
print(urun_kodu.rstrip("HEP"))

#karakter dizisini böleleim

print(okul.split())
print(makale.split())


#böldüğümüz ve listeye dönüşen ifadeleri birleştirelim

kelimeler = okul.split()
print(kelimeler)
print("---".join(kelimeler))

print("emirhan".center(25,"a"))






































