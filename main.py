from PIL import Image
import os
import glob

# Please remember to install Pillow

# Directory for input images
folder_input = 'images'

# Directory for output images
folder_output = 'converted'

news_img = os.listdir(folder_input)

news_img_select = [file for file in news_img if file.endswith(('jpg', 'png'))]

for n_img in news_img_select:
    image = Image.open(folder_input + '/' + n_img)
    image.convert('RGB')

    file = n_img.replace('.jpg', '').replace('.png', '')

    image.save(folder_output + '/' + file + '.webp', 'webp')
    print('--- Done', n_img)

