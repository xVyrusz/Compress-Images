from PIL import Image
import os

cwd =  os.getcwd()
path  = os.path.join(cwd, 'COMPRESS_IMAGES')
path_img =  os.path.join(cwd, 'IMAGES_BIRLOS')

if not os.path.exists(path):
  os.mkdir(path)

files =  os.listdir(path_img)

for file in files:
  img_name = file
  file = file.split('-')
  file.pop()
  file = '-'.join(file)
  folder = os.path.join(path, file)
  check = os.path.join(path, file)
  check_img = os.path.join(check, 'compressed-'+ img_name)
  if not os.path.exists(check):
    os.mkdir(folder)
  if not os.path.exists(check_img):
    os.chdir(path_img)
    img = Image.open(img_name)
    os.chdir(check)
    img.save('compressed-'+ img_name, optimize=True, quality=30)
