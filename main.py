print ("=========Anda Memasuki Kawasan Bebas Pilih Pasangan========", "\n")
print ("=====================Khusus Pria====================", "\n")
ulang = True

while ulang:

  Nama = input("\nMasukkan Nama Anda :")
  cewek = ["1.ayu","2.ela","3.nara","4.ani","5.sasa"]
  print ("\n","========== SELAMAT DATANG " + Nama, "============","\n")
  print ("Menu","\n","1.Cari Jodoh","\n","2.Info Cewek","\n","3.Exit","\n")

  pilih = int(input("pilih Menu 1/2/3: "))
  if pilih == 1:
    ulang = False
    print ("\n","Daftar Wanita yang mungkin Jodoh anda!!")
    print ("\n",cewek,"\n")

    pilih2 = int (input("Pilih Cewek: "))

    if pilih2==1:
      Nama1 = "Ayu"
      Usia1 = 22
      hobi1 = "Makan"
      print ("\n","Nama: ",Nama1,"\n","Usia: ",Usia1,"\n","Hobi: ",hobi1)
      import random
      kecocokan = random.randrange(0,100)
      print("\n","kecocokan: ", kecocokan,"%")
      if kecocokan > 80:
          print("\n","Selamat Anda Cocok")
      elif kecocokan > 60:
          print("\n","Mulailah Pendekatan Sapa tau Jodoh")
      elif kecocokan > 40:
          print("\n","Yah Anda Kurang Cocok Cobak Deh Ajak Jalan:)")
      elif kecocokan > 20:
          print("\n","Gak Cocok")
      elif kecocokan > 0:
          print ("\n","Dah lah Mending Lo Ketaman Meratapi Nasib")
    elif pilih2==2:
      Nama2 = "Ela"
      Usia2 = 25
      hobi2 = "Renang"
      print ("\n","Nama: ",Nama2,"\n","Usia: ",Usia2,"\n","Hobi: ",hobi2)
      import random
      kecocokan = random.randrange(0,100)
      print("\n","kecocokan: ", kecocokan,"%")
      if kecocokan > 80:
          print("\n","Selamat Anda Cocok")
      elif kecocokan > 60:
          print("\n","Mulailah Pendekatan Sapa tau Jodoh")
      elif kecocokan > 40:
          print("\n","Yah Anda Kurang Cocok Cobak Deh Ajak Jalan:)")
      elif kecocokan > 20:
          print("\n","Gak Cocok")
      elif kecocokan > 0:
          print ("\n","Dah lah Mending Lo Ketaman Meratapi Nasib")
    elif pilih2==3:
      Nama3 = "Nara"
      Usia3 = 20
      hobi3 = "Shopping"
      print ("\n","Nama: ",Nama3,"\n","Usia: ",Usia3,"\n","Hobi: ",hobi3)
      import random
      kecocokan = random.randrange(0,100)
      print("\n","kecocokan: ", kecocokan,"%")
      if kecocokan > 80:
          print("\n","Selamat Anda Cocok")
      elif kecocokan > 60:
          print("\n","Mulailah Pendekatan Sapa tau Jodoh")
      elif kecocokan > 40:
          print("\n","Yah Anda Kurang Cocok Cobak Deh Ajak Jalan:)")
      elif kecocokan > 20:
          print("\n","Gak Cocok")
      elif kecocokan > 0:
          print ("\n","Dah lah Mending Lo Ketaman Meratapi Nasib")
    elif pilih2==4:
      Nama4 = "Ani"
      Usia4 = 21
      hobi4 = "Olah Raga"
      print ("\n","Nama: ",Nama4,"\n","Usia: ",Usia4,"\n","Hobi: ",hobi4)
      import random
      kecocokan = random.randrange(0,100)
      print("\n","kecocokan: ", kecocokan,"%")
      if kecocokan > 80:
          print("\n","Selamat Anda Cocok")
      elif kecocokan > 60:
          print("\n","Mulailah Pendekatan Sapa tau Jodoh")
      elif kecocokan > 40:
          print("\n","Yah Anda Kurang Cocok Cobak Deh Ajak Jalan:)")
      elif kecocokan > 20:
          print("\n","Gak Cocok")
      elif kecocokan > 0:
          print ("\n","Dah lah Mending Lo Ketaman Meratapi Nasib")
    elif pilih2==5:
      Nama5 = "Ani"
      Usia5 = 23
      hobi5 = "Jalan-Jalan"
      print ("\n","Nama: ",Nama5,"\n","Usia: ",Usia5,"\n","Hobi: ",hobi5)
      import random
      kecocokan = random.randrange(0,100)
      print("\n","kecocokan: ", kecocokan,"%")
      if kecocokan > 80:
          print("\n","Selamat Anda Cocok")
      elif kecocokan > 60:
          print("\n","Mulailah Pendekatan Sapa tau Jodoh")
      elif kecocokan > 40:
          print("\n","Yah Anda Kurang Cocok Cobak Deh Ajak Jalan:)")
      elif kecocokan > 20:
          print("\n","Gak Cocok")
      elif kecocokan > 0:
          print ("\n","Dah lah Mending Lo Ketaman Meratapi Nasib")
    else:
      print ("\n","Pilihan tidak ada")
      print ("\n","Silahkan Kembali Menu Utama")
      ulang = False


    lagi = input("\nTekan y untuk Cari Jodoh Lagi Dan N Untuk Kelur: ")

    if lagi =="y":
      ulang = True
    elif lagi =="n":
      ulang = False

  elif pilih ==2:
    ulang = False
    Nama1 = "Ayu"
    Usia1 = 22
    hobi1 = "Makan"
    print ("\n","Nama: ",Nama1,"\n","Usia: ",Usia1,"\n","Hobi: ",hobi1)
    Nama2 = "Ela"
    Usia2 = 25
    hobi2 = "Renang"
    print ("\n","Nama: ",Nama2,"\n","Usia: ",Usia2,"\n","Hobi: ",hobi2)
    Nama3 = "Nara"
    Usia3 = 20
    hobi3 = "Shopping"
    print ("\n","Nama: ",Nama3,"\n","Usia: ",Usia3,"\n","Hobi: ",hobi3)
    Nama4 = "Ani"
    Usia4 = 21
    hobi4 = "Olah Raga"
    print ("\n","Nama: ",Nama4,"\n","Usia: ",Usia4,"\n","Hobi: ",hobi4)
    Nama5 = "Ani"
    Usia5 = 23
    hobi5 = "Jalan-Jalan"
    print ("\n","Nama: ",Nama5,"\n","Usia: ",Usia5,"\n","Hobi: ",hobi5)

    print ("\n","Sudah Menemukan Wanita Yang Cocok Sama Kamu???","\n")

    lagi1 = input("Tekan y untuk Cari Jodoh Dan N Untuk Kelur: ")

    if lagi1 =="y":
      ulang = True
    elif lagi1 =="n":
      ulang = False

  elif pilih ==3:
    ulang = False
    print ("\n","Terima Kasih Telah Menggunakan Layanan Kami!!!")

  else:
    ulang = False
    print ("\n","Menu tidak ada")