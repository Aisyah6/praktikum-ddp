class mahasiswa:
 nim= ""
 nama= ""
 rombel= ""
 
def _init_(self,nim,nama,rombel):
    self.nim=nim
    self.nama=nama
    self.rombel=rombel
    
    def welcome(self):
        print("hallo", self.nama,"di STT Terpadu Nurulfikri")
    

    def lulus ( self,nilai):
        if(nilai > 90):
            print ("lulus")
        else :
             print ("tidak lulus")
        
mhs1= mahasiswa("0110222129","siti aisah","TI13")
# mhs1.nama ="siti aisah"
# mhs1.nim = "0110222129"
# mhs1.rombel="TI13"

print("Nama Mahasiswa", mhs1.nama)
print("NIM :", mhs1.nim)
print("Rombel :", mhs1.rombel)
mhs1.lulus(91)
