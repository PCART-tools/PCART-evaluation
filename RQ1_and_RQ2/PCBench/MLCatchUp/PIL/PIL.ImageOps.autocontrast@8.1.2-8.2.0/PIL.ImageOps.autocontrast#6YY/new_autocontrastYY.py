from PIL import ImageOps, Image
image = Image.open('./example.jpg')
result = ImageOps.autocontrast(image, 0, None, preserve_tone=False)
