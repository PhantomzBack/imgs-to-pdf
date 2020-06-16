from PIL import Image
from os import path
ims=[]
i=1
ext=""
print("Enter image extension")
ext=str(input())
print("Enter output file name")
name_out=str(input())
if(ext[0]!="."):
    ext="."+ext
if(name_out[(len(name_out)-4):]!=".pdf"):
    name_out+=".pdf"
name=str(i).zfill(2)+ext
while(1):
    name=str(i).zfill(2)+ext
    if(path.exists(name)):
        name=str(i).zfill(2)+ext
        ims.append(Image.open(name))
        ims[i-1]=ims[i-1].convert('RGB')
        i+=1
    else:
        break
print("I found ",i-1,"files")
ims[0].save(name_out,save_all=True, append_images=ims[1:])
print("Done")
