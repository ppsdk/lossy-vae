from PIL import Image
import numpy as np
import glob
import os

train_path = glob.glob('D:/Dataset/lossy-vae/tecnick/*')

save_path = 'D:/Dataset/lossy-vae/tecnick_new/'

for path in train_path:
    # 使用PIL库打开图片
    print(path)
    img=np.asarray(Image.open(path))
    new_filename = os.path.basename(path).split('.')[0] + '_new.png' 
    RAW=[]
    even=True
    R=True
    G=True
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if even:
                if R:
                    RAW.append(img[i][j][0])
                else:
                    RAW.append(img[i][j][1])
                R = not R
            else:
                if G:
                    RAW.append(img[i][j][1])
                else:
                    RAW.append(img[i][j][2])
                G = not G
        even = not even
    RAW=np.asarray(RAW)
    image = Image.fromarray(RAW.reshape(img.shape[0], img.shape[1]))
    image.save(save_path + new_filename)


    



            

                