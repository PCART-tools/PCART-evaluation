from PIL import Image, ImageDraw
image = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(image)
xy = (50, 50, 250, 250)
start = 45
end = 315
fill = 'red'
outline = 'black'
draw.pieslice(xy=xy, start=start, end=end, width=0)
