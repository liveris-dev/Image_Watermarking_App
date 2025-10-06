import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Watermark")
root.geometry("700x700")
root.configure(bg="#E8E8E8")

def open_explorer():
    filename =  filedialog.askopenfilename(initialdir="/",
                                           title="Select Image",
                                           filetypes=[("Image File", '.jpg .png .jpeg')]
                                           )
    print("You pressed the upload button")
    img = Image.open(filename)
    img=img.resize((600,400))
    photo = ImageTk.PhotoImage(img)
    canvas.itemconfig(image_on_canvas, image=photo)
    canvas.image = photo


#CREATE CANVAS
canvas = tk.Canvas(root, width=600,height=400)
canvas.grid(row=2, column=0, columnspan=2, pady=30, padx=50)
img = Image.open("sample_transparent_image.png")
photo = ImageTk.PhotoImage(img)
image_on_canvas = canvas.create_image(300,200, image=photo)
canvas.image = photo

#CREATE LABEL
label = tk.Label(root, text="Put a custom Watermark on your photo!", height=3)
label.grid(row=0, column=0, columnspan=2, pady=10, padx=20)

#CREATE BUTTONS
upload_button = tk.Button(root,
                   text="Upload a photo",
                   command=open_explorer
                   )
upload_button.grid(row=1, column=0, pady=10, padx=20)

watermark_button = tk.Button(root,
                   text="Watermark your image",
                   )
watermark_button.grid(row=1, column=1, pady=10, padx=20)


# image_label = tk.Label(root,
#                  height=100,
#                  width=100)
# image_label.grid(row=2, column=0, columnspan=2, pady=10, padx=20)

save_button = tk.Button(root,
                   text="Save image",
                   )
save_button.grid(row=3, column=1, pady=10, padx=20)


root.mainloop()