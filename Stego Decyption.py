import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.png")

# Retrieve the stored password and message length
with open("password.txt", "r") as f:
    stored_password = f.read().strip()
with open("length.txt", "r") as f:
    msg_length = int(f.read().strip())

# Create the decoding dictionary (full range 0-255)
c = {i: chr(i) for i in range(256)}

# Get the passcode input from the user
pas = input("Enter passcode for Decryption: ")

if stored_password == pas:
    message = ""
    n, m, z = 0, 0, 0
    # Only read the number of pixels equal to the length of the message
    for i in range(msg_length):
        char_value = img[n, m, z]
        message += c[char_value]
        n += 1
        m += 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
