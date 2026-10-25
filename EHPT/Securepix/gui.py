
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from Stegano import encode_message, decode_message
import os

selected_image = ""

# Main window
root = tk.Tk()
root.title("SecurePix")
root.geometry("700x600")
root.configure(bg="#151925")
root.resizable(False, False)

# Select image
def select_image():
    global selected_image

    path = filedialog.askopenfilename(
        filetypes=[("PNG Images", "*.png")]
    )

    if path:
        selected_image = path
        image_label.config(text=os.path.basename(path))

        img = Image.open(path)
        img.thumbnail((250, 180))

        photo = ImageTk.PhotoImage(img)
        preview_label.config(image=photo)
        preview_label.image = photo

# Hide message
def hide_message():
    if not selected_image:
        messagebox.showerror("Error", "Please select an image!")
        return

    message = message_entry.get("1.0", tk.END).strip()

    if not message:
        messagebox.showerror("Error", "Please enter a message!")
        return

    output = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Images", "*.png")],
        initialfile="secret_image.png"
    )

    if output:
        try:
            encode_message(selected_image, message, output)
            messagebox.showinfo(
                "Success",
                "Message hidden successfully!"
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Extract message
def extract_message():
    if not selected_image:
        messagebox.showerror("Error", "Please select an image!")
        return

    try:
        message = decode_message(selected_image)

        messagebox.showinfo(
            "Extracted Message",
            message if message else "No message found!"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Heading
title = tk.Label(
    root,
    text="SECUREPIX",
    font=("Arial", 28, "bold"),
    bg="#151925",
    fg="#00D4FF"
)
title.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Image Steganography Using LSB Technique",
    font=("Arial", 11),
    bg="#151925",
    fg="white"
)
subtitle.pack()

# Image selection
select_btn = tk.Button(
    root,
    text="Select Image",
    command=select_image,
    font=("Arial", 11, "bold"),
    bg="#007BFF",
    fg="white",
    width=20
)
select_btn.pack(pady=15)

image_label = tk.Label(
    root,
    text="No image selected",
    bg="#151925",
    fg="#AAAAAA"
)
image_label.pack()

preview_label = tk.Label(root, bg="#151925")
preview_label.pack(pady=10)

# Message input
message_label = tk.Label(
    root,
    text="Enter Your Secret Message",
    font=("Arial", 12, "bold"),
    bg="#151925",
    fg="white"
)
message_label.pack(pady=5)

message_entry = tk.Text(
    root,
    height=4,
    width=55,
    font=("Arial", 11)
)
message_entry.pack(pady=5)

# Buttons
hide_btn = tk.Button(
    root,
    text="HIDE MESSAGE",
    command=hide_message,
    font=("Arial", 11, "bold"),
    bg="#00A878",
    fg="white",
    width=22
)
hide_btn.pack(pady=10)

extract_btn = tk.Button(
    root,
    text="EXTRACT MESSAGE",
    command=extract_message,
    font=("Arial", 11, "bold"),
    bg="#E67E22",
    fg="white",
    width=22
)
extract_btn.pack(pady=5)

# Footer
footer = tk.Label(
    root,
    text="Cybersecurity Project | SecurePix",
    bg="#151925",
    fg="#777777",
    font=("Arial", 9)
)
footer.pack(side="bottom", pady=12)

root.mainloop()
