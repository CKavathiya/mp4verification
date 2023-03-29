import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[('MP4 files', '*.mp4')])
    if file_path:
        selected_file.set(file_path)
        window.quit()  
        return file_path
    

window = tk.Tk()
window.title('Select File')
window.geometry('300x180')  
window.iconbitmap('')


selected_file = tk.StringVar()
selected_file_label = ttk.Label(
window, textvariable=selected_file, font=('Helvetica', 12))
selected_file_label.pack(pady=20)
select_file_btn = ttk.Button(
window, text='Select File', command=select_file)
select_file_btn.pack(pady=10)


style = ttk.Style()
style.map('TButton', background=[('active', '#FFFFFF')])

window.mainloop()



