import tkinter as tk   #import tkinter agar gui dapat dibentuk
import time            #import time untuk menjalankan waktu/timer dalam microwave
import threading       #import threading agar hitungan mundur dapat berjalan dengan semestinya

#Kamus
fungsi = [False for i in range(5)] #Array berupa Bool yang bertujuan untuk menyimpan value tiap mode dalam microwave
# fungsi[0] = Microwave
# fungsi[1] = Grill
# fungsi[2] = Crispy grill
# fungsi[3] = Oven
# fungsi[4] = Clean

tampilan = [False for i in range(4)] #Array berupa Bool yang menyimpan value untuk
# tampilan[0] = waktu                #tombol waktu, daya, temperature, dan preset temperature.
# tampilan[1] = Daya
# tampilan[2] = temperature
# tampilan[3] = preset

preset=[False for i in range(3)] #Array dengan value Bool dari [0] sampai [2]
# preset[0] = low                #untuk preset temperature rendah sedang dan tinggi.
# preset[1] = med
# preset[2] = high

waktu = 0          #variabel awal waktu
wattage = 0        #variabel awal wattage
temperature = 100  #Variabel awal temperature

#Algoritma

root = tk.Tk()
root.title("Smart Microwave") #Judul aplikasi

HEIGHT = 400  #besar tinggi awal dari aplikasi
WIDTH = 700   #besar lebar awal dari aplikasi
              #karena tidak menggunakan code untuk mengunci besar tinggi dan lebar, nantinya bisa diresize sendiri

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white") #membuat ukuran awal aplikasi / canvas
canvas.pack()

frame = tk.Frame(root, bg='#d9d9d9')    #membentuk frame di dalam canvas untuk membuat tampilan lebih rapih
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.8, anchor='n') #menentukan letak dan besar frame dalam canvas

def buttonTambah():       #define function untuk menambah menit dalam waktu microwave
    global tampilan
    if tampilan[0]==True: 
        #bila tampilan menunjukkan waktu,
        # maka command berikut mengatur penambahan dan pengurangan waktu
        global waktu
        if (waktu+600)<=5400:
            waktu += 600
        menit, detik = divmod(waktu, 60)
        if menit<10:
            menit=str(0)+str(menit)
        else:
            menit=str(menit)
        if detik<10:
            detik=str(0)+str(detik)
        else:
            detik=str(detik)
        label.config(text=str(menit)+":"+str(detik))
    elif tampilan[1]==True: 
        # bila tampilan menunjukan daya, 
        # maka command berikut menambahkan daya hingga 1000
        global wattage
        if (wattage+100)<=1000:
            wattage+=100
        label.config(text=str(wattage))
    elif tampilan[2]==True: 
        # bila tampilan menampilkan temperature,
        # maka command berikut menambakan temperature hingga 220
        global temperature
        if (temperature+20)<=220:
            temperature+=20
        label.config(text=str(temperature))

def buttonKurang():        #define function untuk mengurang menit dalam waktu microwave
    global tampilan
    if tampilan[0]==True:  
        # bila tampilan menunjukan waktu, 
        # fungsi berikut mengurangi waktu
        global waktu
        if (waktu-600)>0:
            waktu -= 600
        menit, detik = divmod(waktu, 60)
        if menit<10:
            menit=str(0)+str(menit)
        else:
            menit=str(menit)
        if detik<10:
            detik=str(0)+str(detik)
        else:
            detik=str(detik)
        label.config(text=str(menit)+":"+str(detik))
    elif tampilan[1]==True: 
        # bila tampilan menunjukan daya,
        # fungsi berikut mengurangi daya hingga 0
        global wattage
        if (wattage-100)>0:
            wattage -= 100
        label.config(text=str(wattage))
    elif tampilan[2]==True: 
        # bila tampilan menunjukan temperature, 
        # fungsi berikut mengurangi temperature hingga 100
        global temperature
        if (temperature-20)>=100:
            temperature-=20
        label.config(text=str(temperature))

def setFunc():  #funtion untuk mengubah dari tampilan menentukan daya ke tampilan menentukan waktu
    if tampilan[1]==True or tampilan[2]==True or tampilan[3]==True: #if untuk mengubah dari tampilan daya ke waktu
        for i in range(4):                                          #apabila tampilan [1,2,3] adalah True
            tampilan[i]=False
        tampilan[0]=True
        label.config(text="00:00")


def startFunc(): #function untuk memulai microwave dengan countdown timer hingga selesai
    button3.config(text="Stop") #mengubah tampilan start menjadi stop apabila pengguna ingin memberhentikan microwave.
    def countdown(): #function untuk mengatur bagaimana timer dapat countdown dengan semestinya
        global waktu
        while waktu>0:
            menit, detik = divmod(waktu, 60) #variabel yang mengatur jumlah menit dan detik
            if menit<10:
                menit=str(0)+str(menit) #update variabel tersebut
            else:
                menit=str(menit)
            if detik<10:
                detik=str(0)+str(detik)
            else:
                detik=str(detik)
            label.config(text=str(menit)+":"+str(detik)) #menampilkan sekaligus mengupdate waktu yang selalu
            waktu-=1                                     #menghitung mundur sampai 0
            time.sleep(1) #menghambat while function ini selama 1 detik agar tampilan seperti timer semestinya
        waktu=0
        label.config(text="00:00") #mengulang kembali waktu menjadi 00.00
        button3.config(text="Start") #merubah kembali tombol menjadi start
    threading.Thread(target=countdown).start() #mengatur agar countdown berjalan semestinya

def controller(): #function sebagai pengatur jalannya tombol
    global waktu
    if button3['text'] == "Stop": #mengubah tampilan tombol menjadi start dan waktu mengulang apabila
        waktu=0                   #tombol dipencet saat tombol menampilkan Stop
        label.config(text="00:00")
        button3.config(text="Start")
    elif button3["text"] == "Start": #bila tampilan start lalu ditekan, maka tombol akan menjalankan fungsi start
        startFunc()

        

def presetFunc0(): #funtion untuk mengatur tombol preset Low
    if preset[0]==False:
        warna=''  #tempat kosong untuk menentukan variabel warna
        if preset[1]==True: #untuk mengatur sehingga hanya ada 1 preset yang nyala
            presetFunc1()   #apabila ingin merubah dari preset Low ke preset lainnya
        if preset[2]==True:
            presetFunc2()
        preset[0]=True
        warna='#33ff33'  
        if list(fungsi) == [False for i in range(5)]: #kalau mode tidak ada yang dipencet, preset tidak bisa dipencet
          warna='#f2f2f2'
        if ((fungsi[0]==True)and(fungsi[1]==False))or(fungsi[2]==True)or(fungsi[3]==True)or(fungsi[4]==True):
            # batasan preset karena preset hanya dapat digunakan untuk mode grill dan microGrill
            preset[0]=False
            warna ='#f2f2f2'
        button11.config(bg=warna) #mengubah warna tombol sesuai if condition yang terjadi
    elif preset[0]==True:
        preset[0]=False
        preset[1]=False
        preset[2]=False
        button11.config(bg='#f2f2f2')

def presetFunc1(): #funtion untuk mengatur tombol preset Medium
    if preset[1]==False:
        warna=''     #tempat kosong untuk menentukan variabel warna
        if preset[0]==True: #untuk mengatur sehingga hanya ada 1 preset yang nyala
            presetFunc0()
        if preset[2]==True:
            presetFunc2()
        preset[1]=True
        warna='#33ff33'
        if list(fungsi) == [False for i in range(5)]:  #kalau mode tidak ada yang dipencet, preset tidak bisa dipencet
          warna='#f2f2f2'
        if ((fungsi[0]==True)and(fungsi[1]==False))or(fungsi[2]==True)or(fungsi[3]==True)or(fungsi[4]==True):
            # batasan preset karena preset hanya dapat digunakan untuk mode grill dan microGrill
            warna ='#f2f2f2'
            preset[1] = False
        button10.config(bg=warna) #mengubah warna tombol sesuai if condition
    elif preset[1]==True: #mereset warna apabila tombol dipencet dua kali
        preset[0]=False
        preset[1]=False
        preset[2]=False
        button10.config(bg='#f2f2f2')

def presetFunc2(): #funtion untuk mengatur tombol preset High
    if preset[2]==False:
        warna=''       #tempat kosong untuk menentukan variabel warna
        if preset[0]==True: #untuk mengatur sehingga hanya ada 1 preset yang nyala
            presetFunc0()
        if preset[1]==True:
            presetFunc1()
        preset[2]=True
        warna='#33ff33'
        if list(fungsi) == [False for i in range(5)]:   #kalau mode tidak ada yang dipencet, preset tidak bisa dipencet
            warna='#f2f2f2'
        if ((fungsi[0]==True)and(fungsi[1]==False))or(fungsi[2]==True)or(fungsi[3]==True)or(fungsi[4]==True):
            #batasan preset karena preset hanya dapat digunakan untuk mode grill dan microGrill
            warna ='#f2f2f2'
            preset[2] = False
        button9.config(bg=warna) #mengubah warna tombol sesuai if condition
    elif preset[2]==True: #mereset warna apabila tombol dipencet dua kali
        preset[0]=False
        preset[1]=False
        preset[2]=False
        button9.config(bg='#f2f2f2')

def microwaveFunc(): #function sebagai command untuk tombol Microwave
    global wattage, waktu
    if fungsi[0]==False:
        if fungsi[2] == True or fungsi[4] == True or fungsi[3]==True:
            # mengatur sehingga hanya ada 1 tombol yang dapat di pencet sekaligus, serta hanya dapat dipencet dengan
            # tombol grill
            fungsi[0] == False
        else:      #mengulang kembali tampilan tombol ke semula apabila dipencet 2 kali
            fungsi[0] = True
            button4.config(bg='#33ff33')
            tampilan[1]=True
            label.config(text=str(wattage))

    elif fungsi[0]==True: #mereset kembali tombol ke tampilan semula setelah countdown selesai
        fungsi[0] = False
        tampilan[0]=False
        tampilan[1]=False
        wattage=0
        waktu=0
        button4.config(bg='#e6e6e6')
        label.config(text="00:00")

def grillFunc(): #function sebagai command untuk tombol Grill
    global waktu
    if fungsi[1]==False:
        if fungsi[2] == True or fungsi[4] == True or fungsi[3]==True:
            # mengatur sehingga hanya ada 1 tombol yang dapat di pencet sekaligus serta hanya dapat dipencet bersama
            #tombol microwave
            fungsi[1] == False
        else:      #mengulang kembali tampilan tombol ke semula apabila dipencet 2 kali
            fungsi[1] = True
            button6.config(bg='#33ff33')
            tampilan[0]=True
            presetFunc2()
    elif fungsi[1]==True: #mereset kembali tombol ke tampilan semula setelah countdown selesai
        fungsi[1] = False
        tampilan[0]=False
        if preset[0]==True: #settingan untuk mengubah preset dari Low, Med, High
            presetFunc0()
        if preset[1]==True:
            presetFunc1()
        if preset[2]==True:
            presetFunc2()
        waktu=0
        button6.config(bg='#e6e6e6')
        label.config(text="00:00")

def crispyFunc(): #function sebagai command untuk tombol Crispy Grill
    global waktu
    if fungsi[2]==False:
        if fungsi[0] == True or fungsi[1] == True or fungsi[3] == True or fungsi[4] == True:
            # mengatur sehingga hanya ada 1 tombol yang dapat di pencet sekaligus
            fungsi[2] == False
        else: #mengulang kembali tampilan tombol ke semula apabila dipencet 2 kali
            fungsi[2] = True
            tampilan[0]=True
            button7.config(bg='#33ff33')
    elif fungsi[2]==True: #mereset kembali tombol ke tampilan semula setelah countdown selesai
        fungsi[2] = False
        tampilan[0] = False
        waktu=0
        button7.config(bg='#e6e6e6')
        label.config(text="00:00")


def microgrillFunc(): #function untuk mengatur combo Micro Grill
    if fungsi[0]==True and fungsi[1]==True: #fungsi baru berjalan apabila tombol Microwave dan Grill dinyalakan
        presetFunc2()
    elif preset[2]==True:
        presetFunc2()

def ovenFunc(): #funtion sebagai command untuk tombol Oven
    global waktu, temperature
    if fungsi[3]==False:
        if fungsi[0] == True or fungsi[1] == True or fungsi[2] == True or fungsi[4] == True:
            #mengatur sehingga hanya ada 1 tombol yang dapat di pencet sekaligus
            fungsi[3] == False
        else:                 #mengulang kembali tampilan tombol ke semula apabila dipencet 2 kali
            fungsi[3] = True
            tampilan[2]=True
            label.config(text=str(temperature))
            button5.config(bg='#33ff33')
            
    elif fungsi[3]==True: #mereset kembali tombol ke tampilan semula setelah countdown selesai
        fungsi[3] = False
        tampilan[0]=False
        tampilan[2]=False
        waktu=0
        temperature=0
        button5.config(bg='#e6e6e6')
        label.config(text="00:00")

def clean(): #function sebagai command untuk tombol clean
    global waktu
    if fungsi[4]==False:
        if fungsi[0] == True or fungsi[1] == True or fungsi[2] == True or fungsi[3] == True:
            fungsi[4] == False
        else:
            fungsi[4] = True
            waktu=1200
            button8.config(bg='#33ff33')
            label.config(text="20:00")
    elif fungsi[4]==True: #mereset kembali tombol ke tampilan semula setelah countdown selesai
        fungsi[4] = False
        waktu=0
        label.config(text="00:00")
        button8.config(bg='#e6e6e6')

label = tk.Label(frame, text="00:00", font=("Courier New", 40)) #label waktu
label.place(relx=0.365, rely=0.58)


button = tk.Button(frame, text='Set', font=('', 20), command=setFunc) #tombol 1, tulisan = Set
button.place(relx=0.13, rely=0.8, relwidth=0.15)

button1 = tk.Button(frame, text='+', font=('Forte', 20), command= buttonTambah) #tombol 2, text = +
button1.place(relx=0.55, rely=0.8, relwidth=0.15)

button2 = tk.Button(frame, text='-', font=('Britannic Bold', 20), command= buttonKurang)#tombol 3, text = -
button2.place(relx=0.34, rely=0.8, relwidth=0.15)

button3 = tk.Button(frame, text='Start', font=('', 20), command=controller) #tombol 4, text = Start
button3.place(relx=0.75, rely=0.8, relwidth=0.14)

button4 = tk.Button(frame, text='Microwave', font=('', 10), command=microwaveFunc)#tombol 5, text = Microwave
button4.place(relx=0.13, rely=0.1, relwidth=0.15, relheight=0.14)

button5 = tk.Button(frame, text='Oven', font=('', 17), command=ovenFunc) #tombol 6, text = Oven
button5.place(relx=0.13, rely=0.25, relwidth=0.15)

button6 = tk.Button(frame, text='Grill', font=('', 17), command=grillFunc) #tombol 7, text = Grill
button6.place(relx=0.13, rely=0.4, relwidth=0.15)

#Crispy grill dan grill beda, crispy grill seperti grill, tetapi untuk bahan makanan yang mengandung banyak lemak/minyak
#agar hasilnya sangat garing.

button7 = tk.Button(frame, text='Crispy\nGrill', font=('', 14), command=crispyFunc) #tombol 8, text = Crispy Grill
button7.place(relx=0.13, rely=0.55, relwidth=0.15, relheight=0.14)

button8 = tk.Button(frame, text='Clean', font=('', 16), command=clean) #tombol 9, text = Clean
button8.place(relx=0.73, rely=0.1, relwidth=0.15)

button9 = tk.Button(frame, text='High', font=('', 13), command=presetFunc2) #tombol 10, text = High
button9.place(relx=0.73, rely=0.25, relwidth=0.12)
button10 = tk.Button(frame, text='Med', font=('', 13), command=presetFunc1) #tombol 11, text = Med
button10.place(relx=0.73, rely=0.35, relwidth=0.12)
button11 = tk.Button(frame, text='Low', font=('', 13), command=presetFunc0) #tombol 12, text = Low
button11.place(relx=0.73, rely=0.45, relwidth=0.12)

root.mainloop()