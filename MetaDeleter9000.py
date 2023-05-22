#This script gets rid of all your images metadata.
#But, can't I do that in Photoshop already?
#Yes, but it is still some metadata there, like your Photoshop version and such, and I'm a paranoic son of a bitch who doesn't like to get tracked down, so I want to get rid of ALL MY IMAGES METADATA
#So yeah, it gets rid of the meta.
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

def delete_metadata_file():
    try:
        # Opens a dialog to select the files.
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")])
        
        if file_path:
            delete_metadata(file_path)
            print("All metadata extermined.")
        else:
            print("No file selected.")
    except FileNotFoundError as e:
        print("File not found.")
    except IsADirectoryError as e:
        print("Selected path is a directory. Please select an image file.")
    except Exception as e:
        print(f"Error: {e}")

def delete_metadata(image_path):
    try:
        file_size = os.path.getsize(image_path)
        if file_size == 0:
            print("Empty file. Metadata cannot be extermined.")
            return

        image = Image.open(image_path)

        # Creates a copy of the image without metadata
        image_without_metadata = image.copy()
        image_without_metadata.info = {}

        # Overwrites the original image with the cleaned one.
        image_without_metadata.save(image_path)

        print(f"Metadata successfully deleted for {image_path}")
    except Exception as e:
        print(f"Error: {e}")

delete_metadata_file()
