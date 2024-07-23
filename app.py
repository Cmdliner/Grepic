import pytesseract
from PIL import Image

# Example usage
img = Image.open('image.jpg')
text = pytesseract.image_to_string(img)
print(text)

