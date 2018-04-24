
from PIL import Image
#------------Function to Decode the image------------#
def unsteg_image(img):
    width, height = img.size
    msg = ""
    index = 0
    print("Decoding image...")
    print("This may take few seconds. Please wait...")
    for row in range(height):
        for column in range(width):
            try:
                r, g, b = img.getpixel((column, row))
            except ValueError:
                r, g, b, a = img.getpixel((column, row))
            if row == 0 and column == 0:
                length = r
            elif index <= length:
                msg += chr(r)
            index += 1
    list = [msg, length]
    return list
#------------End of Decode function-------------#
image_to_be_decoded = "Encoded_test.png"
img2 = Image.open(image_to_be_decoded)
secret_message = unsteg_image(img2)
#printing the Secret message
print("The length of the text is:", secret_message[1])
print("Secret message: {}".format(secret_message[0]))
