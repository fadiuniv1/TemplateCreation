import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
import os
import random


def create_template(logo_path, phone, instagram, text, photos_list):
    # Open the template image
    img = Image.new('RGB', (1200, 628), color=(255, 255, 255))
    # Create a draw object
    draw = ImageDraw.Draw(img)
    # Draw a rectangle
    draw.rectangle([200, 100, 600, 500], fill=(255, 255, 255), outline=(0, 0, 0))

    # Draw a line
    draw.line([200, 100, 600, 500], fill=(255, 0, 0), width=5)

    try:
        info = Image.new('RGB', (400, 200), color=(255, 255, 255))
        draw = ImageDraw.Draw(info)
        font = ImageFont.truetype("arial.ttf", 15)
        draw.text((10, 10), "Phone: " + phone, (0, 0, 0), font=font)
        draw.text((10, 30), "Instagram: " + instagram, (0, 0, 0), font=font)
        draw.text((10, 50), text, (0, 0, 0), font=font)
        img.paste(info, (25, 500))
    except:
        print("Error adding information to template")

    # Add a random photo from the photos_list to the template
    try:
        random_photo = random.choice(photos_list)
        img_temp = Image.open(random_photo)
        img_temp = img_temp.resize((800, 400))
        img.paste(img_temp, (200, 100))
    except:
        print("Error opening photo files")
        # Add logo and information to templates
    try:
        logo = Image.open(logo_path)
        logo = logo.resize((250, 250))
        img.paste(logo, (50, 50))
    except:
        print("Error opening logo file")
    # save the template
    try:
        file_name = "template_with_information.jpg"
        i = 1
        while os.path.exists(file_name):
            file_name = "template_with_information_" + str(i) + ".jpg"
            i += 1
        img.save(file_name)
        print("Template created successfully and saved as " + file_name)
    except:
        print("Error saving template")


def select_logo():
    logo_path = filedialog.askopenfilename()
    logo_path_label.config(text=logo_path)
    return logo_path


def select_photos():
    photos_path = filedialog.askopenfilenames()  # allows user to select multiple photos
    photos_path_label.config(text=",".join(photos_path))
    return photos_path


def create_template_gui():
    logo_path = logo_path_label.cget("text")
    photos_list = photos_path_label.cget("text").split(',')
    phone = phone_entry.get()
    instagram = instagram_entry.get()
    text = text_entry.get()
    create_template(logo_path, phone, instagram, text, photos_list)
    success_label.config(text="Template created successfully!")

# Move button callback
def move_element(dx, dy):
    # Move the rectangle or line by dx and dy
    draw.move(dx, dy)


root = tk.Tk()
root.title("Image Template Creator")

logo_path_label = tk.Label(root, text="No logo selected.")
logo_path_label.pack()

select_logo_button = tk.Button(root, text="Select logo", command=select_logo)
select_logo_button.pack()


photos_path_label = tk.Label(root, text="No photos selected.")
photos_path_label.pack()

select_photos_button = tk.Button(root, text="Select photos", command=select_photos)
select_photos_button.pack()

phone_label = tk.Label(root, text="Phone number:")
phone_label.pack()

phone_entry = tk.Entry(root)
phone_entry.pack()

instagram_label = tk.Label(root, text="Instagram handle:")
instagram_label.pack()

instagram_entry = tk.Entry(root)
instagram_entry.pack()

text_label = tk.Label(root, text="Text:")
text_label.pack()

text_entry = tk.Entry(root)
text_entry.pack()

# Create move button in the GUI
move_button = tk.Button(root, text="Move", command=lambda: move_element(10, 10))
move_button.pack()

create_template_button = tk.Button(root, text="Create template", command=create_template_gui)
create_template_button.pack()

success_label = tk.Label(root, text="")
success_label.pack()

root.mainloop()
##commit tag
