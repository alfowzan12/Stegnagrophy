
from PIL import Image
#-------------Function to Encode the image------------#
def steg_image(img, msg):

    length = len(msg)
    # if the length of the text is more than 255 characters, return False
    #with error message.
    if length > 255:
        print("text must be less than 255 characters")
        return False
    #if message is not RGB, return false and print error message.
    if img.mode != 'RGB':
        print("image need to be RGB")
        return False
    # use a copy of image to hide the text in
    encoded = img.copy()
    width, height = img.size
    index = 0
    print("Encoding the message...")
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            # first value is length of msg
            if row == 0 and col == 0 and index < length:
                asc = length
            elif index <= length:
                c = msg[index -1]
                asc = ord(c)
            else:
                asc = r
            encoded.putpixel((col, row), (asc, g , b))
            index += 1
    return encoded
#------------End of Encoding Function----------#
image_to_be_encoded = "test.png"
img = Image.open(image_to_be_encoded)
encoded_image_file = "Encoded_" + image_to_be_encoded
secret_msg = "Hello world, i am hiding inside the IMAGE!!! you cant see me!"
img_encoded = steg_image(img, secret_msg)
if img_encoded:
    print("Saving the new image with the text in it...")
    img_encoded.save(encoded_image_file)
    print("Congrats! You encoded the image!")
