# Stegnagrophy
Name : Fares alfowzan
Description : There are two functions, one to steg the image and one to unsteg the image.
the function to steg the image first checks if the length is less than 255, and then it checks if the image mode is RBG,
  if its not, it throws an error message. and then it uses a copy of the image to hide the secret image in it.
the unsteg function takes the image as an input and displays the secret message.

How to Execute : change the string "image_to_be_encoded" to the image you wish to hide the secret message in it and execute steg.py.
and to display the secret message, change the string "image_to_be_encoded" in unsteg.py to the image with hidden secret message, and execute it.
                
