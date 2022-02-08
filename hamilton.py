import itertools

def dosyaoku():
	baslik = True
	with open(dosya,'r') as f:
		for line in f:
			satir = line.strip().split(sep='\t')
			print('satir:',satir)

			if baslik:
				baslik = False
				for s in satir:
					sehirler.append(s)

				print('Sehirler:',sehirler)
				continue

			sehir = satir[0]
			for sira, mesafe in enumerate(satir[1:]):
				anahtar = (sehir, sehirler[sira])
				mesafeler[anahtar] = int(mesafe)

			print('Mesafeler:',mesafeler)

def hesapla():
	global ilk_sehir, gezinti_sehirleri

	# gezinti_sehirleri küme'ye çevrilecek. Kümenin içinde ilk_sehir varsa kümeden çıkartılacak.
	# gezintiKumesi = set(gezinti_sehirleri)
	# gezintiKumesi.discard(ilk_sehir)

	gezintiKumesi = gezinti_sehirleri


	sehir_adedi = len(gezintiKumesi)

	en_kisa_mesafe = 1e10
	en_kisa_yol = ''

	# P(gezintiKumesinin, sehir_adedi) yani permutasyon kümeleri bulunacak.
	for kume in itertools.permutations(gezintiKumesi, sehir_adedi):

		yolsirasi =(ilk_sehir,) + kume + (ilk_sehir,)
		topmesafe = 0

		for i in range(len(yolsirasi)-1):
			anahtar = (yolsirasi[i], yolsirasi[i+1])
			topmesafe += mesafeler[anahtar]
		print('Mesafe: %5d Yol Sirasi: %s' % (topmesafe, yolsirasi))

		if en_kisa_mesafe > topmesafe:
			en_kisa_mesafe = topmesafe
			en_kisa_yol = yolsirasi

	print('SONUÇ: En Kısa Mesafe: %5d En Kısa Yol Sirasi: %s' % (en_kisa_mesafe, en_kisa_yol))


sehirler = list()
mesafeler = dict()

ilk_sehir = 'a'
gezinti_sehirleri = ('b','c','d','e')
dosya = 'yol1.txt'

dosyaoku()
hesapla()

input('ikincitest için bir tuşa basınız')

sehirler = list()
mesafeler = dict()

ilk_sehir = 'Konya'
gezinti_sehirleri = ('Ankara','Bursa','Eskişehir','Antalya')
dosya = 'turkiye.txt'
dosyaoku()
hesapla()
