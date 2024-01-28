import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor")

        self.image_path = None
        self.original_image = None

        # Widgets
        self.canvas = tk.Canvas(root)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Save", command=self.save_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.destroy)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Blur", command=self.apply_blur_filter)

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_path = file_path
            self.original_image = Image.open(self.image_path)
            self.display_image()

    def save_image(self):
        if self.original_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                self.original_image.save(file_path)

    def display_image(self):
        if self.original_image:
            img_tk = ImageTk.PhotoImage(self.original_image)
            self.canvas.config(width=img_tk.width(), height=img_tk.height())
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
            self.canvas.image = img_tk

    def apply_blur_filter(self):
        if self.original_image:
            blurred_image = self.original_image.filter(ImageFilter.BLUR)
            self.original_image = blurred_image
            self.display_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()
