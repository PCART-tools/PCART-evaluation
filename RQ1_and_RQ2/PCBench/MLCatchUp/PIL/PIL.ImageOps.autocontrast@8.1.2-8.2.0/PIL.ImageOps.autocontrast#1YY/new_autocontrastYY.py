from PIL import ImageOps, Image
image = Image.open('/home/zhang/example.jpg')
result = ImageOps.autocontrast(image, preserve_tone=False)
