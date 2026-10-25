
from PIL import Image

def encode_message(image_path, message, output_path):

    image = Image.open(image_path).convert("RGB")
    pixels = list(image.getdata())

    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '00000000'

    if len(binary_message) > len(pixels) * 3:
        raise ValueError("Message is too large for this image!")

    new_pixels = []
    bit_index = 0

    for pixel in pixels:
        new_pixel = []

        for value in pixel:
            if bit_index < len(binary_message):
                value = (value & 254) | int(binary_message[bit_index])
                bit_index += 1

            new_pixel.append(value)

        new_pixels.append(tuple(new_pixel))

    image.putdata(new_pixels)
    image.save(output_path, format="PNG")


def decode_message(image_path):

    image = Image.open(image_path).convert("RGB")

    binary_message = ""

    for pixel in image.getdata():
        for value in pixel:
            binary_message += str(value & 1)

    message = ""

    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]

        if len(byte) < 8:
            break

        char = chr(int(byte, 2))

        if char == '\0':
            break

        message += char

    return message
