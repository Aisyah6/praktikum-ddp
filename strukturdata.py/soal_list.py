#soal
 #lish makanan dengan 2 dimensi
list_makanan=[
     ["bakwan","tempe","tahu",],
     ["nasi uduk","nasi pecel","sate padang"]
 ] 
#print nasi pecel
print(list_makanan[1][1])

#print tahu
print(list_makanan[0][2])

 #bagaimana mengeprint semuanya?
 #harus keluar dari kotak
 
for makanan in list_makanan:
    print(makanan) 
    
    for makanan in list_makanan:
        for detail_makanan in makanan:
            print(detail_makanan)