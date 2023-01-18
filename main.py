import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog

def create_template(logo_path, phone, instagram, text):
    # Open the template image
    img = Image.new('RGB', (1200, 628), color=(255, 255, 255))
    # Add logo and information to templates
    with open(logo_path, 'rb') as f:
        logo = Image.open(f)
    logo = logo.resize((250, 250))
    img.paste(logo, (950, 25))
