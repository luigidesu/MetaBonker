#This script gets rid of all your images metadata.
#But, can't I do that in Photoshop already?
#Yes, but it is still some metadata there, like your Photoshop version and such, and I'm a paranoic son of a bitch who doesn't like to get tracked down, so I want to get rid of all the metadata.
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os
import math

def delete_metadata_files():
    try:
        # Opens a dialog to select the files.
        root = tk.Tk()
        root.withdraw()
        file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")]) #Supported file formats, feel free to add some more.
        
        if file_paths:
            total_space_saved = 0
            for file_path in file_paths:
                space_saved = delete_metadata(file_path)
                total_space_saved += space_saved
                print(f"Metadata successfully bonked for {file_path}")
                print(f"Space saved: {format_size(space_saved)}")

            print(f"Total space saved: {format_size(total_space_saved)}")
        else:
            print("Select some files, come on.")
    except FileNotFoundError as e:
        print("File not found.")
    except IsADirectoryError as e:
        print("Get yo folder outta here, I only accept individual files.") #The script only works with files, not complete folders, to prevent mistakes.
    except Exception as e:
        print(f"Error: {e}")

def delete_metadata(image_path):
    try:
        file_size = os.path.getsize(image_path)
        if file_size == 0:
            print(f"Yo files are 0 bytes, stupidhead.")
            return 0

        image = Image.open(image_path)

        # Creates a copy of the image to work on
        image_without_metadata = image.copy()
        image_without_metadata.info = {}

        # Overwrites the original image with the cleaned one.
        image_without_metadata.save(image_path)

        space_saved = file_size - os.path.getsize(image_path)
        return space_saved
    except Exception as e:
        print(f"Error: {e}")
        return 0

#Filesize formatting, I highly doubt you'll ever clean more than 1GB, damn, maybe not even 1MB, but if you'll do, just edit this.
def format_size(size):
    if size < 1024:
        return f"{size} Bytes"
    elif size < 1024 * 1024:
        return f"{size / 1024:.2f} KB"
    elif size < 1024 * 1024 * 1024:
        return f"{size / (1024 * 1024):.2f} MB"
    else:
        return f"{size / (1024 * 1024 * 1024):.2f} GB"

delete_metadata_files()

# When running this trough the CMD, it closes automatically, so I can't see how much space I saved, so this thing prevents that.
input("Press Enter to exit...")
