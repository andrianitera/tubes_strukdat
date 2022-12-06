#
#PROGRAM PENCARIAN RUTE KOTA PULAU SUMATERA DENGAN BFS 
#(sebagai tugas untuk ujian akhir semester mata kuliah kecerdasan buatan)

#RECODING BY : GALIH AP, M.ILHAM IHSANUDIN, KHOIRUL UMAM
#SOURCE : OPEN SOURCE (GITHUB, WEB, ETC)
#TYPESETTER : GALIH AP 
#
#

#DATABASE RUTE
jawa={#Banten
      'Merak':set(['Cilegon','Bojonegara']),
      'Bojonegara':set(['Cilegon','Merak']),
      'Cilegon':set(['Merak','Bojonegara','Anyer','Kramatwatu']),
      'Anyer':set(['Labuan','Padarincang''Mancak','Cilegon',]),
      'Kramatwatu':set(['Cilegon','Mancak','Serang','Banten']),
      'Mancak':set(['Ciomas','Anyer']),
      'Padarincang':set(['Ciomas','Labuan','Anyer']),
      'Labuan':set(['Anyer','Padarincang','Jiput','Menes','Situ Cikeudal','Pagelaran','Munjul','Tanjung Lesung','Cigeulis']),
      'Serang':set(['Pandeglang','Kramatwatu','Curug','Ciruas','Kasemen']),
      'Banten':set(['Kramatwatu','Kasemen']),
      'Ciomas':set(['Kaduhejo','Padarincang','Mancak']),
      'Jiput':set(['Labuan','Menes','Situ Cikeudal','Cikoromoy']),
      'Menes':set(['Labuan','Jiput','Situ Cikeudal', 'Cikoromoy','Saketi']),
      'Situ Cikeudal':set(['Labuan','Jiput','Menes','Pagelaran']),
      'Pagelaran':set(['Labuan','Situ Cikeudal','Munjul']),
      'Munjul':set(['Pagelaran','Saketi','Cigeulis','Cikeusik','Malingping']),
      'Tanjung Lesung':set(['Labuan','Cigeulis']),
      'Cigeulis':set(['Tanjung Lesung','Munjul','Cibaliung','Labuan']),
      'Kasemen':set(['Serang','Banten','Ciruas','Tanara']),
      'Ciruas':set(['Serang','Kasemen','Tanara','Walantaka','Pamarayan']),
      'Kragilan':set(['Walantaka','Ciruas','Tanara']),
      'Curug':set(['Serang','Pandeglang','Walantaka','Pamarayan','Rangkasbitung']),
      'Pandeglang':set(['Serang','Ciomas','Curug','Kaduhejo','Saketi','Walantaka','Rangkasbitung']),
      'Kaduhejo':set(['Ciomas','Pandeglang','Cikoromoy']),
      'Cikoromoy':set(['Jiput','Menes','Kaduhejo']),
      'Saketi':set(['Menes','Pandeglang','Munjul','Kaduhejo','Cikeusik','Malingping','Gunung Kencana']),
      'Cikeusik':set(['Munjul','Cikeusik','Malingping','Cibaliung']),
      'Malingping':set(['Munjul','Cikeusik','Gunung Kencana','Cibaliung','Cibobos']),
      'Tanara':set(['Kasemen','Ciruas','Balaraja','Karawaci','Kota Tangerang','Bandara Soekarno Hatta']),
      'Walantaka':set(['Ciruas','Curug','Pandeglang','Pamarayan','Rangkasbitung']),
      'Balaraja':set(['Ciruas','Tanara','Pamarayan','Karawaci','Maja']),
      'Pamarayan':set(['Ciruas','Curug','Pandeglang','Walantaka','Balaraja','Rangkasbitung','Maja']), 
      'Karawaci':set(['Tanara','Balaraja','Kota Tangerang','Bandara Soekarno Hatta','Depok']), 
      'Rangkasbitung':set(['Curug','Pandeglang','Walantaka','Pamarayan','Maja','Gunung Kencana','Leuwidamar','Sajira']),
      'Gunung Kencana':set(['Munjul','Saketi','Cikeusik','Malingping','Rangkasbitung','Cibobos','Leuwidamar','Cibeo','Cikotok',' Tg Karang Taraje']), 
      'Cibaliung':set(['Munjul','Cigeulis','Cikeusik','Malingping','Sumur']),
      'Cibobos':set(['Malingping','Gunung Kencana','Leuwidamar','Cibeo','Cikotok','Tg Karang Taraje']), 
      'Kota Tangerang':set(['Tanara','Karawaci','Bandara Soekarno Hatta','Kalideres','Cipondoh','Kembangan']),
      'Bandara Soekarno Hatta':set(['Tanara','Karawaci','Kota Tangerang','Kalideres']),
      'Maja':set(['Balaraja','Pamrayan','Rangkasbitung','Sajira']),
      'Leuwidamar':set(['Rangkasbitung','Gunung Kencana','Cibobos','Sajira','Cibeo','Cikotok','Tg Karang Taraje','Ciboleger']),
      'Sajira':set(['Rangkasbitung','Maja','Leuwidamar','Cikotok','Ciboleger','Bogor']),
      'Cibeo':set(['Gunung Kencana','Cibobos','Leuwidamar',' Cikotok','Tg Karang Taraje']),
      'Cikotok':set(['Gunung Kencana','Cibobos','Cibeo','Leuwidamar','Sajira','Tg Karang Taraje','Ciboleger','Sukabumi']),
      'Tg Karang Taraje':set(['Gunung Kencana','Cibobos','Leuwidamar','Cibeo','Cikotok','Darmasari']),
      'Sumur':set(['Cibaliung']),
      'Cipondoh':set(['Kota Tangerang','Cengkareng','Serpong']),
      'Ciboleger':set(['Leuwidamar','Sajira','Cikotok']),
      'Darmasari':set(['Tg Karang Taraje','Darmasari','Sawarna']),
      'Serpong':set(['Cipondoh']),
      'Sawarna':set(['Sawarna','Darmasari','Sukabumi']),
      #
      #DKI JAKARTA
      'Kalideres':set(['Bandara Soekarno Hatta','Kota Tangerang', 'Penjaringan','Cengkareng']),
      'Cengkareng':set(['Kalideres','Penjaringan', 'Grogol Petamburan', 'Kebon Jeruk', 'Kembangan','Cipondoh']),
      'Penjaringan':set(['Kalideres', 'Tambora',  'Grogol Petamburan',  'Cengkareng']),
      'Kembangan':set(['Kota Tangerang','Cengkareng', 'Kebon Jeruk', 'Pesangrahan']),
      'Kebon Jeruk':set(['Kembangan','Cengkareng', 'Grogol Petamburan', 'Palmerah', 'Kebayoran Lama','Pesangrahan']),
      'Grogol Petamburan':set(['Kebon Jeruk', 'Cengkareng', 'Penjaringan','Tambora', 'Gambir','Palmerah']),
      'Tambora':set(['Grogol Petamburan', 'Penjaringan', 'Taman Sari', 'Gambir']),
      'Pademangan':set(['Penjaringan', 'Tanjung Priok', 'Kemayoran', 'Sawah Besar', 'Taman Sari']),
      'Pesangrahan':set(['Kembangan','Kebon Jeruk', 'Kebayoran Lama']),
      'Kebayoran Lama':set(['Pesangrahan','Kebon Jeruk', 'Palmerah', 'Tanah Abang', 'Kebayoran Baru', 'Cilandak']),
      'Palmerah':set(['Kebon Jeruk', 'Grogol Petamburan', 'Tanah Abang', 'Kebayoran Lama']),
      'Gambir':set(['Grogol Petamburan', 'Tambora', 'Taman Sari', 'Sawah Besar', 'Senen', 'Menteng', 'Tanah Abang', 'Palmerah']),
      'Taman Sari':set(['Tambora', 'Pademangan', 'Sawah Besar','Gambir']),
      'Sawah Besar':set(['Taman Sari', 'Pademangan', 'Kemayoran', 'Senen','Gambir']),
      'Cilandak':set(['Kebayoran Lama', 'Kebayoran Baru', 'Mampang Prapatan', 'Pasarminggu', 'Jagaraksa']),
      'Kebayoran Baru':set(['Kebayoran Lama', 'Tanah Abang', 'Setiabudi', 'Mampang Prapatan', 'Cilandak']),
      'Tanah Abang':set(['Palmerah', 'Gambir', 'Kebayoran Lama', 'Kebayoran Baru', 'Menteng', 'Setiabudi']),
      'Menteng':set(['Tanah Abang', 'Gambir', 'Senen', 'Matraman', 'Tebet', 'Setiabudi']),    
      'Senen':set(['Menteng','Gambir', 'Sawah Besar', 'Kemayoran', 'Johar Baru', 'Cempaka Putih', 'Matraman']),
      'Kemayoran':set(['Sawah Besar', 'Pademangan', 'Tanjung Priok', 'Cempaka Putih','Johar Baru', 'Senen']),
      'Tanjung Priok':set(['Pademangan', 'Koja', 'Kelapa Gading','Kemayoran']),
      'Jagaraksa':set(['Cilandak', 'Pasarminggu', 'Pasar Rebo','Depok']),
      'Pasarminggu':set(['Cilandak', 'Mampang Prapatan', 'Pancoran', 'Kramat Jati', 'Pasar Rebo', 'Jagaraksa']),
      'Mampang Prapatan':set(['Kebayoran Baru', 'Setiabudi', 'Tebet', 'Pancoran', 'Pasarminggu''Cilandak']),
      'Setiabudi':set(['Tanah Abang', 'Menteng', 'Matraman', 'Tebet', 'Pancoran', 'Mampang Prapatan', 'Kebayoran Baru']),
      'Johar Baru':set(['Senen','Kemayoran', 'Cempaka Putih']),
      'Pancoran':set(['Mampang Prapatan', 'Tebet', 'Kramat Jati', 'Pasarminggu']),
      'Tebet':set(['Setiabudi','Menteng', 'Matraman', 'Jatinegara', 'Kramat Jati', 'Pancoran','Mampang Prapatan']),
      'Matraman':set(['Menteng', 'Senen', 'Cempaka Putih', 'Pulo Gadung', 'Jatinegara', 'Tebet']),
      'Cempaka Putih':set(['Johar Baru', 'Kemayoran', 'Pulo Gadung', 'Matraman', 'Senen']),
      'Pasar Rebo':set(['Jagaraksa', 'Pasarminggu', 'Kramat Jati', 'Ciracas']),
      'Kramat Jati':set(['Pasarminggu', 'Pancoran', 'Jatinegara', 'Makasar', 'Ciracas', 'Pasar Rebo']),
      'Jatinegara':set(['Tebet','Matraman', 'Pulo Gadung', 'Durensawit', 'Makasar', 'Kramat Jati']),
      'Pulo Gadung':set(['Matraman', 'Cempaka Putih', 'Kelapa Gading', 'Cakung', 'Durensawit', 'Jatinegara']),
      'Kelapa Gading':set(['Tanjung Priok', 'Koja', 'Cilincing', 'Cakung', 'Pulo Gadung']),
      'Koja':set(['Tanjung Priok', 'Cilincing','Kelapa Gading']),
      'Ciracas':set(['Pasat Rebo', 'Kramat Jati', 'Cipayung']),
      'Makasar':set(['Kramat Jati','Jatinegara', 'Durensawit', 'Cipayung']),
      'Durensawit':set(['Jatinegara','Pulo Gadung','Cakung', 'Bekasi','Makasar']),
      'Cakung':set(['Pulo Gadung', 'Kelapa Gading', 'Cilincing','Durensawit']),
      'Cilincing':set(['Koja','Cakung', 'Kelapa Gading']),
      'Cipayung':set(['Kramat Jati', 'Ciracas', 'Makasar']),
      #
      #Jawa Barat
      'Depok' :set(['Jagaraksa','Bekasi', 'Bogor','Karawaci']),
      'Bogor':set(['Depok','Bekasi','Cianjur','Sukabumi']),
      'Bekasi' :set(['Depok','Durensawit','Karawang','Bogor']),
      'Sukabumi':set(['Bogor','Cianjur','Sawarna','Cikotok']),
      'Cianjur':set(['Sukabumi','Bogor','Bandung']),
      'Karawang':set(['Bekasi','Subang','Purwakarta']),
      'Bandung':set(['Cianjur','Cimahi','Garut']),
      'Purwakarta':set(['Karawang','Subang','Cimahi']),
      'Subang':set(['Purwakarta','Karawang','Indramayu','Sumedang','Cimahi']),
      'Garut':set(['Bandung','Sumedang','Tasikmalaya']),
      'Cimahi':set(['Purwakarta','Subang','Sumedang','Bandung']),
      'Sumedang':set(['Cimahi','Subang','Majalengka','Garut']),
      'Indramayu':set(['Subang','Cirebon','Majalengka']),
      'Tasikmalaya':set(['Garut','Ciamis']),
      'Majalengka':set(['Sumedang','Indramayu','Cirebon','Kuningan','Ciamis']),
      'Cirebon':set(['Majalengka','Indramayu','Brebes']),
      'Ciamis':set(['Majalengka','Kuningan','Banjar','Tasikmalaya']),
      'Kuningan':set(['Majalengka','Brebes','Ciamis']),
      'Banjar':set(['Ciamis','Purwokerto','Cilacap']),
      #
      #JAWA TENGAH
      'Brebes' :set(['Kuningan','Cirebon','Tegal','Slawi']),
      'Tegal' :set(['Brebes','Slawi','Pemalang']),
      'Slawi':set(['Brebes','Tegal','Purwokerto']),
      'Purwokerto':set(['Slawi','Purbalingga','Kebumen','Kroya','Cilacap']),
      'Cilacap':set(['Banjar','Purwokerto','Kroya']),
      'Kroya':set(['Cilacap','Purwokerto','Kebumen']),
      'Kebumen':set(['Kroya','Purwokerto','Purworejo']),
      'Purworejo':set(['Kebumen','Magelang','Wates']),
      'Magelang':set(['Purworejo','Wonosobo','Temanggung','Salatiga','Boyolali','Sleman']),
      'Boyolali':set(['Klaten','Solo','Salatiga','Magelang']),
      'Klaten':set(['Sleman','Boyolali']),
      'Solo':set(['Sukoharjo','Sragen','Purwodadi','Boyolali','Magetan']),
      'Sukoharjo':set(['Wonosari','Solo','Wonogiri']),
      'Wonogiri':set(['Wonosari','Sukoharjo','Ponorogo','Pacitan']),
      'Sragen':set(['Solo','Blora','Ngawi']),
      'Blora':set(['Rembang','Sragen','Purwodadi']),
      'Rembang':set(['Blora','Kudus','Bojonegoro']),
      'Kudus':set(['Demak','Purwodadi','Tuban','Rembang']),
      'Demak':set(['Semarang','Purwodadi','Kudus']),
      'Semarang':set(['Demak','Salatiga','Kendal']),
      'Kendal':set(['Pekalongan','Temanggung','Semarang']),
      'Pekalongan':set(['Kendal','Pemalang']),
      'Pemalang':set(['Pekalongan','Tegal','Purbalingga']),
      'Purbalingga':set(['Purwokwerto','Banjarnegara','Pemalang']),
      'Banjarnegara':set(['Purbalingga','Wonosobo']),
      'Wonosobo':set(['Banjarnegara','Magelang','Temanggung']),
      'Temanggung':set(['Wonosobo','Kendal','Salatiga','Magelang']),
      'Salatiga':set(['Temanggung','Magelang','Boyolali','Semarang']),
      'Purwodadi':set(['Demak','Kudus','Blora','Solo']),
      #
      #Yogyakarta
      'Wates':set(['Purworejo','Yogyakarta']),
      'Sleman':set(['Magelang','Yogyakarta']),
      'Yogyakarta':set(['Wates','Sleman','Klaten','Wonosari','Bantul']),
      'Bantul':set(['Yogyakarta','Wonosari']),
      'Wonosari':set(['Bantul','Yogyakarta','Sukoharjo','Wonogiri']),
      #
      #Jawa Timur
      'Tuban':set(['Gresik','Lamongan','Bojonegoro']),
      'Bojonegoro':set(['Ngawi','Blora','Rembang','Tuban','Lamongan','Nganjuk']),
      'Ngawi':set(['Sragen','Bojonegoro','Nganjuk','Madiun']),
      'Magetan':set(['Karangayar','Madiun']),
      'Pacitan':set(['Wonogiri','Ponorogo']),
      'Lamongan':set(['Jombang','Bojonegoro','Tuban','Gresik','Mojokerto']),
      'Nganjuk':set(['Madiun','Ngawi','Bojonegoro','Jombang','Kediri']),
      'Ponorogo':set(['Pacitan','Madiun','Trenggalek']),
      'Trenggalek':set(['Ponorogo','Tulungagung']),
      'Gresik':set(['Lamongan','Tuban','Surabaya']),
      'Jombang':set(['Kediri','Nanjuk','Lamongan','Mojokerto']),
      'Kediri':set(['Tulungagung','Nganjuk','Jombang','Batu']),
      'Tulungagung':set(['Trenggalek','Kediri','Blitar']),
      'Surabaya':set(['Mojokerto','Gresik','Bangkalan','Sidoarjo']),
      'Mojokerto':set(['Jombang','Lamongan','Surabaya','Pasuruan']),
      'Sidoarjo':set(['Surabaya','Pasuruan','Malang']),
      'Batu':set(['Kediri','Malang']),
      'Malang':set(['Blitar','Batu','Sidoarjo','Pasuruan','Lumajang']),
      'Blitar':set(['Tulungagung','Kediri','Malang']),
      'Pasuruan':set(['Malang','Mojokerto','Sidoarjo','Probolinggo']),
      'Bangkalan':set(['Surabaya','Ketapang','Sampang']),
      'Probolinggo':set(['Lumajang','Pasuruan','Situbondo']),
      'Lumajang':set(['Malang','Probolinggo','Jember']),
      'Ketapang':set(['Sampang','Bangkalan','Sumenep']),
      'Pamekasan':set(['Sampang','Sumenep']),
      'Sumenep':set(['Pamekasan','Ketapang']),
      'Situbondo':set(['Bondowoso','Probolinggo','Banyuwangi']),
      'Bondowoso':set(['Situbondo','Jember']),
      'Jember':set(['Lumajang','Bondowoso','Banyuwangi']),
      'Banyuwangi':set(['Jember','Situbondo'])
      }
      
sumatra={
    #Lampung
    'Lampung Barat':set(['Pesisir Barat', 'Tanggamus', 'Lampung Tengah', 'Lampung Utara','Way Kanan']),
    'Lampung Selatan':set(['Bandar Lampung', 'Pesawaran', 'Lampung Timur', 'Lampung Tengah']),
    'Lampung Tengah':set(['Lampung Timur','Metro','Lampung Selatan','Pesawaran','Pringsewu','Tanggamus','Lampung Barat','Laampung Utara','Tulang Bawang Barat','Tulang Bawang']),
    'Lampung Timur':set(['Lampung Selatan','Metro','Lampung Tengah','Tulang Bawang']),
    'Lampung Utara':set(['Lampung Tengah','Lampung Barat','Way Kanan','Tulang Bawang Barat']),
    'Mesuji':set(['Tulang Bawang','Tulang Bawang Barat']),
    'Pesawaran':set(['Bandar Lampung','Lampung Tengah','Pringsewu','Tanggamus']),
    'Pesisir Barat':set(['Lampung Barat','Tanggamus']),
    'Pringsewu':set(['Pesawaran','Lampung Tengah','Tanggamus',]),
    'Tanggamus':set(['Lampung Tengah','Lampung Barat','Pringsewu','Pesawaran','Pesisir Barat']),
    'Tulang Bawang':set(['Lampung Timur','Mesuji','Tulang Bawang Barat','Lampung Tengah']),
    'Tulang Bawang Barat':set(['Mesuji','Tulang Bawang','Lampung Tengah','Lampung Utara','Way Kanan']),
    'Way Kanan':set(['Tulang Bawang Barat','Lampung Utara','Lampung Barat']),
    'Bandar Lampung':set(['Lampung Selatan','Pesawaran']),
    'Metro':set(['Lampung Timur', 'Lampung Tengah']),
    #
    #Kepulauan Bangka Belitung
    'Bangka Barat':set(['Bangka']),
    'Bangka':set(['Bangka Barat','Pangkal Pinang','Bangka Tengah']),
    'Pangkal Pinang':set(['Bangka','Bangka Tengah']),
    'Bangka Tengah':set(['Bangka','Pangkal Pinang','Bangka Selatan']),
    'Bangka Selatan':set(['Bangka Tengah','Belitung']),
    'Belitung':set(['Bangka Selatan','Belitung Timur']),
    'Belitung Timur':set(['Belitung']),
    #
    #Sumatera Selatan
    'Banyuasin':set(['Musi Banyuasin','Abab Lematang Ilir','Palembang','Ogan Komering Ilir']),
    'Empat Lawang':set(['Musi Rawas','Lahat','Pagar Alam']),
    'Lahat':set(['Empat Lawang','Pagar Alam','Muara Enim','Musi Rawas']),
    'Muara Enim':set(['Lahat','Musi Rawas','Abab Lematang Ilir','Prabumulih','Ogan Ilir','Ogan Komering Ulu','Ogan Komering Ulu Selatan']),
    'Musi Banyuasin':set(['Musi Rawas Utara','Musi Rawas','Abab Lematang Ilir','Banyuasin']),
    'Musi Rawas':set(['Musi Rawas Utara','Lubuklinggau','Empat Lawang','Lahat','Muara Enim','Abab Lematang Ilir','Musi Banyuasin']),
    'Musi Rawas Utara':set(['Musi Rawas','Musi Banyuasin']),
    'Ogan Ilir':set(['Muara Enim','Prabumulih','Ogan Komering Ulu','Ogan Komering Ulu Timur','Ogan Komering Ilir','Banyuasin','Palembang']),
    'Ogan Komering Ilir':set(['Banyuasin','Palembang','Ogan Ilir','Ogan Komering Ulu Timur']),
    'Ogan Komering Ulu':set(['Muara Enim','Ogan Komering Ulu Selatan','Ogan Komering Ulu Timur','Ogan Ilir']),
    'Ogan Komering Ulu Selatan':set(['Ogan Komering Ulu','Muara Enim','Ogan Komering Ulu Timur']),
    'Ogan Komering Ulu Timur':set(['Ogan Komering Ilir','Ogan Ilir','Ogan Komering Ulu','Ogan Komering Ulu Selatan']),
    'Abab Lematang Ilir':set(['Musi Banyuasin','Musi Rawas','Muara Enim','Prabumulih','Banyuasin']),
    'Lubuklinggau':set(['Musi Rawas']),
    'Pagar Alam':set(['Empat Lawang','Lahat','Muara Enim']),
    'Palembang':set(['Banyuasin','Muara Enim','Ogan Ilir','Ogan Komering Ilir']),
    'Prabumulih':set(['Muara Enim','Ogan Ilir','Abab Lematang Ilir']),
    #
    #Bengkulu
    'Bengkulu Selatan':set(['Kaur','Seluma']),
    'Bengkulu Tengah':set(['Seluma','Kepahiang','Rejang Lebong','Bengkulu Utara','Bengkulu']),
    'Bengkulu Utara':set(['Mukomuko','Lebong','Rejang Lebong','Bengkulu Tengah']),
    'Kaur':set(['Bengkulu Selatan']),
    'Kepahiang':set(['Rejang Lebong','Bengkulu Tengah','Seluma']),
    'Lebong':set(['Rejang Lebong','Bengkulu Utara']),
    'Mukomuko':set(['Bengkulu Utara']),
    'Rejang Lebong':set(['Lebong','Bengkulu Utara','Bengkulu Tengah','Kepahiang']),
    'Seluma':set(['']),
    'Bengkulu':set(['']),
    }

#CODINGAN BAGIAN DARI BFS
def bfs(sumatera, mulai, tujuan):
    queue =[[mulai]]
    visited =set()

    while queue:
        #input antrian paling depan ke variabel jalur
        jalur=queue.pop(0)
        #simpan node ke variabel state
        state=jalur[-1]
        #cek apa statenya sama dengan tujuan atau tidak, kalau sama kita return
        if state == tujuan:
            return jalur
        #jika tidak sama dengan tujuan, cek state apa ada di visited
        elif state not in visited:
            #jika state tidak ada di visited maka cek cabang
            for cabang in jawa.get(state,[]): #cek semua cabang dari state
                jalur_baru = list(jalur) #masukan isi variabel jalur ke variabel jalur baru
                jalur_baru.append(cabang) #update isi jalur baru dengan cabang
                queue.append(jalur_baru) #update queue dengan jalur baru
        #tandai state yang telah dikunjungi menjadi visited
        visited.add(state)
        #cek isi antrian
        isi = len(queue)
        if isi == 0:
            print("Tidak Ditemukan")

#CODINGAN BAGIAN UNTUK DFS
def dfs(jawa, mulai, tujuan):
    queue = [[mulai]]
    visited = set()

    while queue :
        #hitung panjang tumpukan dan masukan ke variabel panjang_tumpukan
        panjang_tumpukan = len(queue)-1
        #masukan tumpukan paling atas ke variabel jalur
        jalur = queue.pop(panjang_tumpukan)
        #simpan node yang dipilih ke variabel state
        state = jalur[-1]
        #cek state apakah ada yanng sama seperti tujuan, jika ada, kita return
        if state == tujuan:
            return jalur
        #jika state tidak sama dengan tujuan, maka cek state tidak ada di visited
        elif state not in visited :
            #jika state tidak ada divisited maka cek cabang
            for cabang in jawa.get(state, []):
                jalur_baru = list(jalur)
                jalur_baru.append(cabang)
                queue.append(jalur_baru)
            #tandai state yang sudah dikunjungi sebagai visited
            visited.add(state)
            #cek isi tumpukan
            isi = len(queue)
            if isi == 0:
                print("Tidak Ditemukan")
