import numpy as np
import os.path
from IPython.display import clear_output
import time

if os.path.exists("file.txt"):
  os.remove("file.txt")

kolom=4000
baris=4000
chunksize=1000

def chunk(value,chunksize):
  chunk_size=[]
  for i in range(int(value/chunksize)):
    chunk_size.append(chunksize)
  if not value%chunksize==0:
    chunk_size.append(value%chunksize)
  return chunk_size

def gen_matrix(baris,kolom):
  for i in range(baris):
    persen=((i+1)/baris)*100
    clear_output(wait=True)
    print(f'{persen:.2f} %')

    for j in range(len(kolom)):
      array1 = np.random.randint(10, size=(1, kolom[j]))
      array1=np.array(array1)
      
      f=open('file.txt','a')
      np.savetxt(f, array1.flatten(), delimiter=',', fmt='%d', newline=', ')
      f.write("")
      f.close()

    f=open('file.txt','a')
    f.write("\n")
    f.close()

starttime = time.time()
kolom=chunk(kolom,chunksize)
# baris=chunk(baris,chunksize)
gen_matrix(baris,kolom)

print(' {} s'.format(time.time() - starttime))
# f = open("file.txt", "r")
# print(f.read())
