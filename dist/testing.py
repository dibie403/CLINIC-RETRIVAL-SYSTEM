import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk



class App:
    def __init__(self):
        self.messagebox = None
        self.Splashwindow = tk.Tk()
        self.Splashwindow.title('School Management System')
        self.Splashwindow.geometry('1000x650')

        # Center the window on the screen
        window_width = 700
        window_height = 550
        screen_width = self.Splashwindow.winfo_screenwidth()
        screen_height = self.Splashwindow.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.Splashwindow.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')
        self.Splashwindow.config(bg='white')

        # Load and set icon photo
        self.image2 = tk.PhotoImage(file='pngwing.com.png')
        self.label2 = tk.Label(self.Splashwindow, image=self.image2, bg='white')
        self.label2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.label3 = ctk.CTkLabel(self.Splashwindow, text='HOSPITAL MANAGEMENT SYSTEM ILARO',
                                   text_color='#173662', fg_color='white', font=('Times', 30))
        self.label3.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        self.Splashwindow.after(1000, self.loginwindow)

    def loginwindow(self):
        # Destroy the splash window
        if self.Splashwindow:
            self.Splashwindow.destroy()

        self.login_window = tk.Tk()
        self.login_window.title('School Management System')
        self.login_window.geometry('1000x600')
        self.login_window.config(bg='white')

        window_width = 1000
        window_height = 600
        screen_width = self.login_window.winfo_screenwidth()
        screen_height = self.login_window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.login_window.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')
        self.login_window.resizable(False, False)

        self.image_icon2 = Image.open('pngwing.com.png')
        self.image_icon2 = ImageTk.PhotoImage(self.image_icon2)
        self.login_window.iconphoto(False, self.image_icon2)

        self.frame1 = ctk.CTkFrame(self.login_window, fg_color='red', width=450,
                                   height=600, corner_radius=10)
        self.frame1.place(relx=0.67, rely=0.1)

        self.image3 = Image.open('pngwing.com.png')
        self.image3 = ImageTk.PhotoImage(self.image3)
        self.label4 = tk.Label(self.login_window, image=self.image3, bg='white')
        self.label4.pack(side=tk.LEFT, padx=60, pady=10)

    def capture_frame(self):
        # Hide the button temporarily to not include it in the screenshot
        self.downloadbut.grid_forget()

        # Update the window to reflect changes
        self.Splashwindow.update()

        # Get the dimensions of the main_frame
        x = self.Splashwindow.winfo_rootx() + self.mainframe1.winfo_x()
        y = self.Splashwindow.winfo_rooty() + self.mainframe1.winfo_y()
        width = x + self.mainframe1.winfo_width()
        height = y + self.mainframe1.winfo_height()

        # Capture the screenshot of the frame
        screenshot = ImageGrab.grab(bbox=(x, y, width, height))

        # Restore the button
        self.downloadbut.grid(pady=10)

        # Save the screenshot as an image file
        self.save_as_pdf(screenshot)

    def save_as_pdf(self, image):
        # Open the file dialog to choose where to save the PDF
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                 filetypes=[("PDF files", "*.pdf")])
        if file_path:
            # Convert the image to RGB mode and save it as a PDF
            image = image.convert("RGB")
            image.save(file_path)
            print(f"Saved as {file_path}")

    def start(self):
        self.Splashwindow.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()
