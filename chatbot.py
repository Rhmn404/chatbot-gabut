import re
import random
#author sangka & rahman
#Instagram : sangka_kpm & rahman_nayyers

#Membuat balasan botnya 
bot = ["hallo juga"]
bot2 = ["hai juga","hay juga"]
nama = ["nama saya Oliv"]
kenalan = ["Ayok, namamu siapa ?"]
kenalan2 = ["boleh kok hehe"]
asal = ["saya berasal dari bot"]
cipta = ["saya di buat / di ciptakan oleh Sangka"]
tempat_tinggal = ["tempat tinggal saya di mesin :)","jangan tanya mulu Oliv lagi pms"]
jadi = ["Saya mau menjadi pacarmu kok","ya mau dong hehe","ya mau lah","Oliv mau kok","Mau dong"]
kue = ["Saya tidak terlalu mengerti coba lihat di google"]
ganteng = ["Kalo ganteng itu sudah dari bawaan wkwkw"]
rindu = ["tentu saja aku merindukanmu","saya merindunkanmu :("]
kangen = ["kangen kepadamu itu adalah kewajibanku :)","Iyaa saya kangen kepadamu","kangen lah :("]
rindu2 = ["jangan rindu kamu gaakan kuat biar Oliv saja","Oliv juga rindu :("]



#membuat pertanyaan dari user
#mengambil balasan bot dari atas

while(True):
 user = str(input("Root@Mr.Tersakiti : "))
 if re.findall(r"hallo", user):
    print(random.choice(bot))
 elif re.findall(r"hai|hay", user):
    print("bot : ", random.choice(bot2))
 elif re.findall(r"siapa namamu ?|namamu siapa ?", user): 
    print("bot : ", random.choice(nama))
 elif re.findall(r"kenalan yok ?|kenalan yuk ?", user):
    print(random.choice(kenalan))
 elif re.findall(r"boleh kenalan ?|boleh kenalan ga nih ?", user):
    print("bot : ", random.choice(kenalan2))
 elif re.findall(r"darimana asalmu ?|asalmu darimana ?|dimana asalmu ?|asalmu dimana ?|kalo boleh tau asalmu darimana ?", user):
    print("bot : ", random.choice(asal))
 elif re.findall(r"siapa penciptamu ?|siapa yang membuat kamu ?|siapa pembuatmu ?|pembuatmu siapa ?|penciptamu siapa ?", user):
    print(random.choice(cipta))
 elif re.findall(r"dimana tempat tinggalmu ?|dimana tinggalmu|tinggal dimana kamu ?|kamu tinggal dimana ?|Oliv tinggal dimana ?|dimana tempat tinggal mu ?|dimana tempatmu ?", user):
    print(random.choice(tempat_tinggal))
 elif re.findall(r"apakah kau mau menjadi pacarku ?|apakah kamu mau menjadi pacarku ?|apa kamu mau menjadi pacarku ?|kamu mau ga jadi pacarku ?|kamu mau jadi pacarku ?|kamu mau jadi pacarku ?|Oliv mau jadi pacarku ?|Oliv mau ga jadi pacarku ?", user):
 	  print(random.choice(jadi)) 
 elif re.findall(r"maukah kamu menjadi pacarku ?|bagaimana cara membuat kue ?|bagaimana cara buat kue ?|buat kue gimana ya caranya|cara buat kue gimana|buat kue kek mana ya", user):
    print(random.choice(kue))
 elif re.findall(r"bagaimana cara menjadi ganteng ?|cara biar ganteng gimana ?|biar ganteng gimana ya ?|tutor ganteng dong|caranya ganten gimana ?|gimana caranya biar ganteng ?|caranya ganteng gimana ya ?|caranya ganteng gimana ya cape di hina terus", user):
    print(random.choice(ganteng))
 elif re.findall(r"apakah kamu rindu aku ?|apakah kamu merindikanku ?|apa kamu merindikanku ?|apa lu merindukanku ?|apa kamu rindu ?|apa kamu rindu aku ?|apakah oliv rindu aku ?", user):
    print(random.choice(rindu))
 elif re.findall(r"apakah kamu kangen padaku ?|apakah kamu kangen kepadaku ?|apa oliv kangen ke aku ?|apa kamu kangem ke aku ?|kamu kangen ga ke aku ?", user):
    print(random.choice(kangen))
 elif re.findall(r"aku merindukanmu|aku rindu kamu|aku rindu|gw rindu|saya rindu|saya merindukanmu|gw merindukanmu|gua merindukanmu|gua rindu", user):
    print(random.choice(rindu2))
 else:
    print("maaf saya tidak mengerti")
