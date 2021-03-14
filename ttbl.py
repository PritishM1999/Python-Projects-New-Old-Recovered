
from preview_generator.manager import PreviewManager

cache_path = '/tmp/preview_cache'
file_to_preview_path = 'C:/Users/PRITESH/Desktop/STUDY MATERIALS.docx'

manager = PreviewManager(cache_path, create_folder= True)
path_to_preview_image = manager.get_jpeg_preview(file_to_preview_path, width=1000, height=500)










'''import tkinter as tk
import tkintertable


root = tk.Tk()
table = tkintertable.table(root, rows=10, cols=4)
table.pack(side="top", fill="both", expand=True)
root.mainloop()'''
