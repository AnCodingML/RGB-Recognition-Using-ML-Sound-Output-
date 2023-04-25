# Recognize and Predicts RGB Colors Using Machine Learning and Sound Output<br>

Biasanya, warna RGB digunakan untuk grafis komputer. Ia terdiri dari tiga warna, yakni merah, hijau,
dan biru. Dari warna inilah namanya diambil. Dalam bahasa Inggris, ketiganya berarti (r)ed, (g)reeen, dan
(b)lue, tiga warna ini digambarkan lewat angka 0 hingga 1. Angka-angka ini bisa membentuk persamaan
matematika. Oleh karena itu, gabungan ketiganya bisa digambarkan lewat garis tiga dimensi. Garis ini
akan membentuk kubus. Kamu bisa melihatnya lewat gambar di bawah ini.

Biasanya, warna RGB digunakan untuk grafis komputer. Ia terdiri dari tiga warna, yakni merah, hijau,
dan biru. Dari warna inilah namanya diambil. Dalam bahasa Inggris, ketiganya berarti (r)ed, (g)reeen, dan
(b)lue, tiga warna ini digambarkan lewat angka 0 hingga 1. Angka-angka ini bisa membentuk persamaan
matematika. Oleh karena itu, gabungan ketiganya bisa digambarkan lewat garis tiga dimensi. Garis ini
akan membentuk kubus. Kamu bisa melihatnya lewat gambar di bawah ini.<br>

![image](https://user-images.githubusercontent.com/117325158/234335544-5039e7f4-f60a-49ee-8c1c-bff608562f51.png)<br>

Warna awal dalam RGB adalah hitam. Ia berubah dengan menambahkan merah, biru, serta hijau.
Gabungan beberapa warna akhirnya membentuk corak baru. Kamu bisa melihat adanya corak
kuning, cyan, magenta, hingga putih. Di tengah-tengah kubus, ada garis abu-abu. Garis ini
menyambungkan warna hitam dan putih. Jumlah warna dalam RGB sendiri sangat banyak, nilainya
mencapai 16.777.216. Sayangnya, mata manusia hanya bisa menangkap kurang lebih 7 juta warna.

---

## Dataset

Tahap pertama adalah membuat dataset yang akan digunakan pada pemodelan machine learning, namun perlu dipastikan agar menyediakan camera yang cukup dalam melakukan citra warna.<br>
```
while True:
    ret,img =cap.read()
    #cv2.regtangle(img,(300,220),       (340,260),(0,0,255),3)
    for x in range (330,340,1):
        for y in range(220,260,1):
            color = img[x,y]
            colorB = img [y,x,0]
            colorG = img[y,x,1]
            colorR = img[y,x,2]
    #print(color, 'WHITE')
    cv2.imshow('Pengambilan Database', img)
```
Program tersebut akan mendeteksi warna RGB yang ditangkap citra kamera secara realtime, untuk memudahkan bisa ditambahkan perintah `print(color, '(warna)')` dalam membuat database. Hal tersebut dilakukan berulang sesuai jumlah warna yang ingin dideteksi, dan jumlah data setiap warna disesuaikan dengan kebutuhan kemampuan deteksi warna dari program. <br>

Simpan hasil pengambilan data pada terminal pada sebuah file dan file tersebut akan dijadikan dataset untuk dilakukan modeling machine learning.<br>
<br>
Pada dataset yang dibuat, didapatkan 3 jenis warna yakni merah, hijau, dan putih. dengan deskripsi dataset:
- R = merepretasikan hasil citra dari **merah** (numerical)
- G = merepretasikan hasil citra dari **hijau** (numerical)
- B = merepretasikan hasil citra dari **biru** (numerical)
- Target = warna yang dideteksi berdasarkan RGB (categorical)

---

## Modeling<br>

Untuk pemodelan yang digunakan adalah Support Vector Machine Classifier,
```
#x = Data, y=Target
x = Database[[u'B', u'G', u'R']]
y = Database.Target

#Training and Classify
clf = svm.SVC()
clf.fit(x,y)
```
Kemudian dibuat program looping untuk mendeteksi warna berdasarkan hasil modeling<br>
```
    if clf.predict([color]) == 'BIRU':
        print("BIRU")

    elif clf.predict([color]) == 'HIJAU':
        print("HIJAU")
        file = 'hijau.wav'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(3)

    elif clf.predict([color]) == 'KUNING':
        print("KUNING")

    elif clf.predict([color]) == 'MERAH':
        print("MERAH")
        file = 'merah.wav'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(3)

    elif clf.predict([color]) == 'PUTIH':
        print("PUTIH")
        file = 'putih.wav'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(3)
```
Berdasarkan program tersebut hasil prediksi akan memiliki output berupa audio yang sudah disiapkan sebelumnya sesuai dengan jenis warna yang terprediksi

---

## Penelitian lain
reference (https://drive.google.com/file/d/127D3NzGlp2f69yFXcdLGQvHakj6DW-90/view?usp=sharing)
