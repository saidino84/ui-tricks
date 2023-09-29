from tkinter import Tk
from tkinter.filedialog import askopenfilename

root = Tk()
root.withdraw()

file_path = askopenfilename(filetypes=[("Database Files", "*.db")])
print(file_path)