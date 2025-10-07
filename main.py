from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageGrab

root = Tk()
root.title("Watermark")
root.geometry("700x700")
root.configure(bg="#E8E8E8")

watermark_image=Image.open("logo-web.png").convert("RGBA")
watermark_image=watermark_image.resize((80,60))
watermark_logo = ImageTk.PhotoImage(watermark_image)


#APPLY THE DEFAULT WATERMARK LOGO
def watermark():
    global watermark_logo
    watermark_image = Image.open("logo-web.png").convert("RGBA")
    watermark_image = watermark_image.resize((80, 60))
    watermark_logo = ImageTk.PhotoImage(watermark_image)
    final_image = canvas.create_image(560, 365, image=watermark_logo)
    root.update()

#APPLY CUSTOM WATERMARK LOGO
def custom_logo():
    global  watermark_logo
    filepath = filedialog.askopenfilename(initialdir="/",
                                           title="Select Image",
                                           filetypes=[("Image File", '.jpg .png .jpeg')]
                                           )
    logo_image=Image.open(filepath)
    logo_image = logo_image.resize((100,100))
    watermark_logo = ImageTk.PhotoImage(logo_image)
    final_image=canvas.create_image(560, 365, image=watermark_logo)
    root.update()


#UPLOAD A PHOTO
def open_explorer():
    filename =  filedialog.askopenfilename(initialdir="/",
                                           title="Select Image",
                                           filetypes=[("Image File", '.jpg .png .jpeg')]
                                           )
    canvas.delete(image_on_canvas)
    img2 = Image.open(filename)
    img2=img2.resize((600,400))
    background = ImageTk.PhotoImage(img2)
    canvas.create_image(300,200, image=background)
    canvas.image = background


#SAVE THE WATERMARKED IMAGE ON FILE
def save_image():
    root.update()
    filelocation = filedialog.asksaveasfilename(defaultextension="jpg")
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    img=ImageGrab.grab(bbox=(x,y,x1,y1))
    img.show()    # root.update_idletasks()
    img.save(filelocation)



#CREATE CANVAS
canvas = Canvas(root, width=600,height=400)
canvas.grid(row=2, column=0, columnspan=3, pady=30, padx=50)

photo = ImageTk.PhotoImage(Image.open("sample_transparent_image.png").convert("RGBA"))
image_on_canvas = canvas.create_image(300,200, image=photo)
canvas.image = photo

#CREATE LABEL
label = Label(root, text="Put a custom Watermark on your photo!", height=3, bg="#E8E8E8")
label.config(font = ("Arial", 14, "bold"))
label.grid(row=0, column=0, columnspan=3, pady=10, padx=20)

#CREATE BUTTONS
upload_button = Button(root,text="Upload a photo",command=open_explorer)
upload_button.config(font=("Arial", 11))
upload_button.grid(row=1, column=0, pady=10, padx=20)

watermark_button = Button(root,text="Default Watermark",command=watermark)
watermark_button.config(font=("Arial", 11))
watermark_button.grid(row=1, column=1, pady=10, padx=20)

custom_watermark_button = Button(root,text="Custom Watermark",command=custom_logo)
custom_watermark_button.config(font=("Arial", 11))
custom_watermark_button.grid(row=1, column=2, pady=10, padx=20)

save_button = Button(root,text="Save image",command=save_image)
save_button.config(font=("Arial", 11))
save_button.grid(row=3, column=2, pady=10, padx=20)


root.mainloop()