from PIL import ImageFont
font = ImageFont.load_default()
text = 'Hello, Pillow!'
mask = font.getmask(text=text, mode='1', direction=None, features=None, language=None, start=None)
