import pytesseract
from PIL import Image



# Example usage
img = Image.open('./note_sample.jpg')
text = pytesseract.image_to_string(img)
print(text)


# Collect cli arguments
# -> Argument can be full path to file or relative path or . indicating that it should read 
# all the matched files in that path

