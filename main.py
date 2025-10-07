from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageGrab

root = Tk()
root.title("Watermark")
root.geometry("700x700")
root.configure(bg="#E8E8E8")

watermark_image=Image.open("sample_transparent_image.png")
watermark_image=watermark_image.resize((100,80))
watermark_logo = ImageTk.PhotoImage(watermark_image)

#CREATE CANVAS
canvas = Canvas(root, width=600,height=400)
canvas.grid(row=2, column=0, columnspan=2, pady=30, padx=50)

photo = ImageTk.PhotoImage(Image.open("sample_transparent_image.png"))
image_on_canvas = canvas.create_image(300,200, image=photo)
canvas.image = photo


#APPLY THE DEFAULT WATERMARK TO THE PHOTO
def watermark():
    watermarked_image=canvas.create_image(500,320, image=watermark_logo, tag="watermark")
    print("You pressed the watermark button.")
    root.update()


#UPLOAD A PHOTO
def open_explorer():
    filename =  filedialog.askopenfilename(initialdir="/",
                                           title="Select Image",
                                           filetypes=[("Image File", '.jpg .png .jpeg')]
                                           )
    print("You pressed the upload button")
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


#CREATE LABEL
label = Label(root, text="Put a custom Watermark on your photo!", height=3)
label.grid(row=0, column=0, columnspan=2, pady=10, padx=20)

#CREATE BUTTONS
upload_button = Button(root,text="Upload a photo",command=open_explorer)
upload_button.grid(row=1, column=0, pady=10, padx=20)

watermark_button = Button(root,text="Watermark your image",command=watermark)
watermark_button.grid(row=1, column=1, pady=10, padx=20)

save_button = Button(root,text="Save image",command=save_image)
save_button.grid(row=3, column=1, pady=10, padx=20)


root.mainloop()