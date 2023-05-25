#This script gets rid of all your images metadata.
#But, can't I do that in Photoshop already?
#Yes, but it is still some metadata there, like your Photoshop version and such, and I'm a paranoic son of a bitch who doesn't like to get tracked down, so I want to get rid of all the metadata
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

def delete_metadata_files():
    try:
        # Opens a dialog to select the files.
        root = tk.Tk()
        root.withdraw()
        file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")])
        
        if file_paths:
            for file_path in file_paths:
                delete_metadata(file_path)
            print("metadata successfully bonked.")
        else:
            print("select some files, come on.")
    except FileNotFoundError as e:
        print("File not found.")
    except IsADirectoryError as e:
        print("get yo folder outta here, I only accept individual files")
    except Exception as e:
        print(f"Error: {e}")

def delete_metadata(image_path):
    try:
        file_size = os.path.getsize(image_path)
        if file_size == 0:
            print(f"Yo files are 0 bytes, stupidhead.")
            return

        image = Image.open(image_path)

        # Creates a copy of the image to work on
        image_without_metadata = image.copy()
        image_without_metadata.info = {}

        # Overwrites the original image with the cleaned one.
        image_without_metadata.save(image_path)

        print(f"Metadata successfully bonked for {image_path}")
    except Exception as e:
        print(f"Error: {e}")

delete_metadata_files()
