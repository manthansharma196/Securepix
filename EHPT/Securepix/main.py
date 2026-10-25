import os
from Stegano import encode_message, decode_message

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

image = os.path.join(BASE_DIR, "images", "sample.png")
output = os.path.join(BASE_DIR, "images", "secret_image.png")

message = input("Enter your secret message: ")

encode_message(image, message, output)

print("Message hidden successfully!")

extracted = decode_message(output)

print("Extracted message:", extracted)