#
#PROGRAM PENCARIAN RUTE KOTA PULAU SUMATERA DENGAN BFS 
#(sebagai tugas untuk ujian akhir semester mata kuliah kecerdasan buatan)

#Kelompok 9 :
#Husni Na'fa Mubarok
#TYPESETTER : GALIH AP 
#
#

#DATABASE RUTE    
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
    #Jambi
    'Muaro Jambi':set(['Tanjung Jabung Timur', 'Batanghari', 'Tanjung Jabung Barat']),
    'Tanjung Jabung Timur':set(['Tanjung Jabung Barat', 'Muaro Jambi']),
    'Batanghari':set(['Muaro Jambi', 'Sarolangun', 'Tanjung Jabung Barat', 'Tebo']),
    'Tanjung Jabung Barat':set(['Tanjung Jabung Timur','Muaro Jambi','Batanghari','Tebo']),
    'Tebo':set(['Batanghari','Tanjung Jabung Barat','Bungo','Merangin','Sarolangun']),
    'Bungo':set(['Tebo','Merangin','Kerinci']),
    'Merangin':set(['Kerinci','Bungo','Sarolangun','Tebo']),
    'Sarolangun':set(['Batanghari','Merangin','Tebo']),
    'Kerinci':set(['Bungo', 'Merangin']),
    #Riau
    'Indragiri Hilir':set(['Indragiri Hulu', 'Pelalauan']),
    'Indragiri Hulu':set(['Indragiri Hilir', 'Pelalauan', 'Kuantan Singingi']),
    'Pelalauan':set(['Indragiri Hilir','Indragiri Hulu','Kuantan Singingi','Siak','Pekan Baru','Kampar','Kepulauan Menanti']),
    'Kuantan Singingi':set(['Indragiri Hulu','Pelalauan','Kampar']),
    'Kampar':set(['Pekan Baru','Kuantan Singingi','Pelalauan','Rokan Hulu','Siak']),
    'Pekan Baru':set(['Kampar','Siak','Pelalauan']),
    'Siak':set(['Pekan Baru','Pelalauan','Bengkalis','Kampar','Rokan Hulu','Kepulauan Menanti']),
    'Rokan Hulu':set(['Kampar','Rokan Hilir','Siak','Bengkalis']),
    'Rokan Hilir':set(['Rokan Hulu','Bengkalis','Siak','Dumai']),
    'Bengkalis':set(['Siak','Rokan Hulu','Rokan Hilir','Dumai']),
    'Dumai':set(['Bengkalis','Rokan Hilir']),
    'Kepulauan Menanti':set(['Pelalauan','Siak']),
    #Sumatera Barat
    'Agam':set(['Bukittinggi','Padang Pariaman','Pasaman Barat','Pasaman','Lima Puluh Kota','']),
    'Dharmasraya':set(['Sijunjung','Solok','Solok Selatan']),
    'Kepulauan Mentawai':set(['']),
    'Lima Puluh Kota':set(['Pasaman','Agam','Payakumbuh','Tanah Datar','Sijunjung']),
    'Padang Pariaman':set(['Pariaman','Agam','Padang','Padang Panjang','Tanah Datar']),
    'Pasaman':set(['Pasaman Barat','Lima Puluh Kota','Agam']),
    'Pasaman Barat':set(['Pasaman','Agam']),
    'Pesisir Selatan':set(['Solok Selatan','Solok','Kota Padang','']),
    'Sijunjung':set(['Dharmasraya','Solok']),
    'Solok':set(['']),
    'Solok Selatan':set(['Solok','Pesisir Selatan','Dharmasraya','']),
    'Tanah Datar':set(['']),
    'Bukittinggi':set(['']),
    'Padang':set(['']),
    'Padang Panjang':set(['']),
    'Pariaman':set(['']),
    'Payakumbuh':set(['']),
    'Sawahlunto':set(['Sijunjung','']),
    'Kota Solok':set(['Pesisir Selatan','Solok Selatan','Kota Padang','']),
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
            for cabang in sumatera.get(state,[]): #cek semua cabang dari state
                jalur_baru = list(jalur) #masukan isi variabel jalur ke variabel jalur baru
                jalur_baru.append(cabang) #update isi jalur baru dengan cabang
                queue.append(jalur_baru) #update queue dengan jalur baru
        #tandai state yang telah dikunjungi menjadi visited
        visited.add(state)
        #cek isi antrian
        isi = len(queue)
        if isi == 0:
            print("Tidak Ditemukan")

def add(sumatera, key, value):
    sumatera[key] = value

rute = bfs(sumatra, 'Way Kanan', 'Lampung Selatan')
print(rute)