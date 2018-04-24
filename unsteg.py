''' PIL_HideText_decode.py
get the hidden text back from an encoded image
'''
from PIL import Image
def decode_image(img):
    """
    check the red portion of an image (r, g, b) tuple for
    hidden message characters (ASCII values)
    """
    width, height = img.size
    msg = ""
    index = 0
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = img.getpixel((col, row))
            except ValueError:
                # need to add transparency a for some .png files
                r, g, b, a = img.getpixel((col, row))
            # first pixel r value is length of message
            if row == 0 and col == 0:
                length = r
            elif index <= length:
                msg += chr(r)
            index += 1
    return msg
# downloaded from internet web page
image_to_be_decoded = "Encoded_test.png"
# get the hidden text back ...
img2 = Image.open(image_to_be_decoded)
print(img2, img2.mode)  # test
hidden_text = decode_image(img2)
print("Hidden text:\n{}".format(hidden_text))
''' my result -->
Hidden text:
this is a secret message added to the image
'''
