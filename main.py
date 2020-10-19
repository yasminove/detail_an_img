from PIL import Image
from PIL import ImageFilter

baby = Image.open('cute-baby.jpg')

detail = baby.filter(ImageFilter.DETAIL)

detail.show()