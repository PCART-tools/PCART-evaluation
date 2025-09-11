from PIL import ImageOps, Image
image = Image.open('./example.jpg')
result = ImageOps.autocontrast(image, 0, preserve_tone=False)
