import tkinter as tk
from tkinter import filedialog
import os

path_of_file_to_upload = tk.filedialog.askopenfilename(title="Select the BitMap(BMP) File to be convereted to ASCII", 
                                                       filetypes= [("Bitmap files", "*.bmp")])

file_to_upload = os.path.basename(path_of_file_to_upload)
print(file_to_upload)

filename, ext = os.path.splitext(file_to_upload)
ext = ext.lower()

output_dir = tk.filedialog.askdirectory(title= "Directory ASCII_IMAGE File to be moved to")
output = os.path.join(output_dir, f"{filename}.txt")