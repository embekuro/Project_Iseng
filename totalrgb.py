import PIL
import itertools
import multiprocessing as mp
import time

image = PIL.Image.open("photo.jpg")
width, height = image.size

# print(width,'x', height)
# get list rgb value of image
colorls = [ image.getpixel((j,i)) for i,j in itertools.product(range(height), range(width)) ]

def find(i):

  # simple rgb clasification
  red, green, blue, blank = 0, 0, 0, 0
  k = colorls[i]
  if k[0] > k[1] and k[0] > k[2]:
    red = 1
  elif k[1] > k[0] and k[1] > k[2]:
    green = 1
  elif k[2] > k[0] and k[2] > k[1]:
    blue = 1
  else:
    blank = 1
  
  return red, green, blue, blank

def chunk_list(value,chunk):

  # create chunk
  a = []
  a.append(0)
  v = value/chunk
  for i in range(int(v)):
    a.append(int(value))
    value = value-chunk
  a.sort()

  return a

if __name__ == "__main__":
    num_tasks = len(colorls)
    chunksize = 10000 # must be under width*height
    chunks = chunk_list(len(colorls), chunksize)
    rgbtotal = []

    for j in range(len(chunks)-1):
      pool = mp.Pool(processes=2, maxtasksperchild=500)
      print("Start", j)
      tasks =  [pool.apply_async(find,(i,)) for i in range(chunks[j],chunks[j+1])]
      lsrgb = []
      
      for f in tasks:
        y=f.get()
        lsrgb.append(y)
        
      lsrgbsum = tuple([sum(x) for x in zip(*lsrgb)])
      pool.close()
      pool.join()
      print("Finish", j)
      time.sleep(1)
      rgbtotal.append(lsrgbsum)

    red, green, blue, blank=[sum(x) for x in zip(*rgbtotal)]
    print('red : %2d, green : %2d, blue : %d, blank : %2d' % (red, green, blue, blank))
