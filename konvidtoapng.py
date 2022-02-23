import cv2
import os
from apng import APNG

# Opens the Video file
cap= cv2.VideoCapture('videoplaybackpp.mp4') 
# fps = cap.get(cv2.CAP_PROP_FPS) # check video fps
fps=15 # capture {int} fps
framerate=1/fps
i=0
sec=0

try:
  # create folder tmpdata
  if not os.path.exists('tmpdata'):
    os.makedirs('tmpdata')
  else:
    for f in os.listdir('tmpdata'):
      os.remove(os.path.join('tmpdata', f))

except OSError:
  print('Error: Creating directory of data')
  
while(cap.isOpened()):
  # capture image from video
  cap.set(cv2.CAP_PROP_POS_MSEC, (sec*1000))
  ret, frame = cap.read()
  name = './tmpdata/frame' + str(i) + '.png'

  if ret == False:
      break

  cv2.imwrite(name,frame)
  
  sec = sec + framerate
  i+=1

cap.release()
cv2.destroyAllWindows()
# sort list of file
path=('./tmpdata/')
ls=sorted(os.listdir(path), key=lambda x: int(x[5:-4])) 
# convert to apng
os.chdir('./tmpdata')
APNG.from_files(ls, delay=10).save('aresult.png') 
os.chdir('..')
print('Done')
