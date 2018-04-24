
from PIL import Image
#------------Function to Decode the image------------#
def unsteg_image(img):
    width, height = img.size
    msg = ""
    index = 0
    for row in range(height):
        for col in range(width):
            try:
                r, g, b = img.getpixel((col, row))
            except ValueError:
                r, g, b, a = img.getpixel((col, row))
            # first pixel r value is length of message
            if row == 0 and col == 0:
                length = r
            elif index <= length:
                msg += chr(r)
            index += 1
    return msg
#------------End of Decode function-------------#
image_to_be_decoded = "Encoded_test.png"
img2 = Image.open(image_to_be_decoded)
print(img2, img2.mode)  # test
secret_message = unsteg_image(img2)
#printing the Secret message
print("Secret message:\n{}".format(secret_message))
