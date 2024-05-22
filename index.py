from rembg import remove
from PIL import Image

input_path = 'static/images/input.png'
output_path = 'static/images/output.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)