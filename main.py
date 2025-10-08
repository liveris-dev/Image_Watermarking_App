from tkinter import *
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image, ImageTk, ImageGrab


class WatermarkingApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Image Watermark App")
        self.root.geometry("700x700")
        self.root.configure(bg="#E8E8E8")
        self.image = None
        self.watermark_logo = None
        self.watermarked_image = None
        self.text_watermark = None

        # CREATE BUTTONS
        Button(root, text="Upload a photo", command=self.open_explorer).grid(row=1, column=0, pady=10, padx=20)
        # upload_button.config(font=("Arial", 11))
        Button(root, text="Default Watermark", command=self.watermark).grid(row=1, column=1, pady=10, padx=20)
        Button(root, text="Custom Watermark", command=self.custom_logo).grid(row=1, column=2, pady=10, padx=20)
        Button(root, text="Custom Text Watermark", command=self.text_logo).grid(row=3, column=0, pady=10, padx=20)
        Button(root, text="Save image", command=self.save_image).grid(row=3, column=2, pady=10, padx=20)
        # CREATE LABEL
        self.label = Label(root, text="Put a custom Watermark on your photo!", height=3, bg="#E8E8E8")
        self.label.grid(row=0, column=0, columnspan=3, pady=10,padx=20)
        # label.config(font=("Arial", 14, "bold"))

        # CREATE CANVAS
        self.canvas = Canvas(root, width=600, height=400)
        self.canvas.grid(row=2, column=0, columnspan=3, pady=30, padx=50)

        img = Image.open("sample_transparent_image.png").convert("RGBA")
        img.thumbnail((600,400))
        self.image = ImageTk.PhotoImage(img)
        self.canvas.create_image(300, 200, image=self.image)


    def open_explorer(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                                   title="Select Image",
                                                   filetypes=[("Image File", '.jpg .png .jpeg')]
                                                   )
        img = Image.open(filename)
        img.thumbnail((600,400))
        self.canvas.delete("all")
        self.image = ImageTk.PhotoImage(img)
        self.canvas.create_image(300,200, image=self.image)

    # APPLY THE DEFAULT WATERMARK LOGO
    def watermark(self):
        img = Image.open("logo-web.png").convert("RGBA")
        img.thumbnail((80, 60))
        if self.text_watermark:
            self.canvas.delete(self.text_watermark)
        self.watermark_logo = ImageTk.PhotoImage(img)
        self.canvas.create_image(560, 365, image=self.watermark_logo)

    # APPLY A CUSTOM LOGO
    def custom_logo(self):
        filepath = filedialog.askopenfilename(initialdir="/",
                                                   title="Select Image",
                                                   filetypes=[("Image File", '.jpg .png .jpeg')]
                                                   )
        img=Image.open(filepath)
        img.thumbnail((100,100))
        if self.text_watermark:
            self.canvas.delete(self.text_watermark)
        self.watermark_logo = ImageTk.PhotoImage(img)
        self.canvas.create_image(560, 365, image=self.watermark_logo)

    def text_logo(self):
        text_to_enter = simpledialog.askstring(title="Text Logo", prompt="Please type the text to enter as a logo.")
        if self.text_watermark:
            self.canvas.delete(self.text_watermark)
        self.watermark_logo = None
        self.text_watermark = text_to_enter
        self.text_watermark = self.canvas.create_text(500,360, fill="red", font="Arial 11 italic bold", text=self.text_watermark)

    # SAVE THE FINAL IMAGE
    def save_image(self):
        filelocation = filedialog.asksaveasfilename(defaultextension="jpg")
        x = root.winfo_rootx() + self.canvas.winfo_x()
        y = root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        img=ImageGrab.grab(bbox=(x,y,x1,y1))
        img.show()
        img.save(filelocation)
        messagebox.showinfo("Success", "Image saved.")


if __name__ == "__main__":
    root = Tk()
    app = WatermarkingApp(root)
    root.mainloop()

