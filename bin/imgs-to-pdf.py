import cv2
from PIL import Image
from os import path
ims=[]
i=1
ext=""
print("Enter image extension")
ext=str(input())
if(ext[0]!="."):
    ext="."+ext
name=str(i).zfill(2)+ext
while(1):
    name=str(i).zfill(2)+ext
    if(path.exists(name)):
        name=str(i).zfill(2)+ext
        ims.append(cv2.imread(name))
        ims[i-1]=cv2.cvtColor(ims[i-1],cv2.COLOR_BGR2RGB)
        i+=1
    else:
        break
print("I found ",i-1,"files")
im_n=cv2.vconcat(ims)
cv2.imwrite('im_compiled.png', cv2.cvtColor(im_n, cv2.COLOR_RGB2BGR))    
im1=Image.open(r"im_compiled.png")
im1.save(r"compiled.pdf")
print("Done")
