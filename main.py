from PIL import Image
import colorama
from colorama import *
import time
import ctypes

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

header_text = "⭐ By as$tukix ❤️"

set_console_title(header_text)

print(Fore.RED + "PLEASE PUT THE IMAGE TO BE RESIZED IN THE FILE!\n\n ")

img = input('Image name with extension: ')
size = input('Size (0, 0): ')

if img.endswith(".png"):
    image = Image.open(img)
else:
    image = Image.open(f'{img}.png')

new_size = tuple(map(int, size.strip().split(',')))

resized_image = image.resize(new_size)

resized_image.save("image_resized.png")


print(Fore.CYAN + "IMAGE RESIZE SUCCESSFULLY")
time.sleep(6)
