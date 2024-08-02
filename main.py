import sys
from pathlib import Path
from PIL import Image
from pytesseract import image_to_string

file_path = Path(sys.argv[1])

if file_path.exists():
    if file_path.is_dir():
        dir = file_path
        for file in dir.iterdir():
            file_url = str(file.absolute())
            print(image_to_string(Image.open(file_url)))

    print('exists')
else:
    print('Doesn\'t exist')