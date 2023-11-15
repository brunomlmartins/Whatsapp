import pywhatkit
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# define function to select contacts file
def select_contacts_file():
    global contacts_filename
    contacts_filename = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
    contacts_file_label.config(text=contacts_filename)

# define function to select message file
def select_message_file():
    global message_filename
    message_filename = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
    message_file_label.config(text=message_filename)

# define function to select image file
def select_image_file():
    global image_filename
    image_filename = filedialog.askopenfilename(filetypes=[('Image files', '.png .jpg .jpeg')])
    image_file_label.config(text=image_filename)
    # load image preview
    if image_filename:
        image = Image.open(image_filename)
        image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(image)
        image_preview_label.config(image=photo)
        image_preview_label.image = photo
    else:
        image_preview_label.config(image='')

# define function to send message
def send_message():
    # read phone numbers from contacts file
    with open(contacts_filename, 'r') as f:
        phone_numbers = [line.strip() for line in f]

    # read message from message file
    with open(message_filename, 'r', encoding="utf8") as f:
        message = f.read()

    # send message using Pywhatkit to each phone number
    for phone_number in phone_numbers:
        pywhatkit.sendwhats_image(phone_number, image_filename, message, 7, True, 4)

# create window
root = tk.Tk()
root.title('Send Whatsapp')

# create logo image
logo_image = Image.open('logo.png')
logo_image = logo_image.resize((300, 300))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo)
logo_label.pack(pady=20)

# create widgets
contacts_file_button = tk.Button(root, text='CONTACTS', command=select_contacts_file)
contacts_file_label = tk.Label(root, text='Select contact file')
message_file_button = tk.Button(root, text='MESSAGE', command=select_message_file)
message_file_label = tk.Label(root, text='Select message file')
image_file_button = tk.Button(root, text='IMAGE', command=select_image_file)
image_file_label = tk.Label(root, text='Select image')
image_preview_label = tk.Label(root)
send_button = tk.Button(root, text='SEND MESSAGE', command=send_message)


# layout widgets
contacts_file_button.pack(pady=10)
contacts_file_label.pack()
message_file_button.pack(pady=10)
message_file_label.pack()
image_file_button.pack(pady=10)
image_file_label.pack()
image_preview_label.pack(pady=20)
send_button.pack(pady=10)

# run window
root.mainloop()