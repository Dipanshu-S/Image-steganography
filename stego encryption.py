import cv2
import os

# Load image
img = cv2.imread("mypic.png")

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Create dictionaries for encoding and decoding (full range 0-255)
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

n, m, z = 0, 0, 0

# Embed the secret message into the image
for ch in msg:
    img[n, m, z] = d[ch]
    n += 1
    m += 1
    z = (z + 1) % 3

# Save the encrypted image and open it (Windows-specific)
cv2.imwrite("encryptedImage.png", img)
os.system("explorer encryptedImage.png")

# Store the passcode and the length of the message for decryption
with open("password.txt", "w") as f:
    f.write(password)
with open("length.txt", "w") as f:
    f.write(str(len(msg)))
