import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
def calculate_forces():
    try:
        mass_value = float(mass_input.get())
        spring_constant_value = float(spring_constant_input.get())
        stretch_length_value = float(stretch_length_input.get())
        if mass_value < 0 or spring_constant_value < 0 or stretch_length_value < 0:
            raise ValueError("Inputs cannot be negative.")
        g = 9.81
        stretch_length_meters = stretch_length_value / 1000
        spring_force = spring_constant_value * stretch_length_meters
        force_without_weight = -((mass_value * g * 0.06) - spring_force * 0.04) / 0.12
        force_with_weight = (spring_force * 0.04) / 0.12
        force_without_weight = max(0, force_without_weight)
        force_with_weight = max(0, force_with_weight)
        result_without_weight_label.config(
            text=f"Force excluding weight: {force_without_weight:.2f} N"
        )
        result_with_weight_label.config(
            text=f"Force including weight: {force_with_weight:.2f} N"
        )
    except ValueError as ve:
        messagebox.showerror("Input Error", "Enter the values correctly")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero occurred. Check input values.")
    except Exception as e:
        messagebox.showerror("Unexpected Error", str(e))
def create_widgets():
    title_label = tk.Label(root, text="Statics Unit2- Question 3/19", font=("Arial", 25, "bold"), fg="#ff0000")
    title_label.grid(row=0, column=0, columnspan=2, pady=20)
    try:
        problem_image = Image.open("question2.png")  # Change to absolute path if needed
        resized_image = problem_image.resize((700, 220), Image.Resampling.LANCZOS)
        photo_image = ImageTk.PhotoImage(resized_image)
        image_label = tk.Label(root, image=photo_image)
        image_label.grid(row=1, column=0, columnspan=2, pady=10)
        image_label.image = photo_image
    except Exception as e:
        messagebox.showerror("Image Error", f"Error loading image: {e}")
    mass_label = tk.Label(root, text="Mass (kg):", font=("Arial", 16))
    mass_label.grid(row=2, column=0, sticky="e", padx=20, pady=10)
    global mass_input
    mass_input = tk.Entry(root, font=("Arial", 14))
    mass_input.grid(row=2, column=1, padx=20)
    spring_constant_label = tk.Label(root, text="Spring Constant (k)(N/m):", font=("Arial", 16))
    spring_constant_label.grid(row=3, column=0, sticky="e", padx=20, pady=10)
    global spring_constant_input
    spring_constant_input = tk.Entry(root, font=("Arial", 14))
    spring_constant_input.grid(row=3, column=1, padx=20)
    stretch_length_label = tk.Label(root, text="Stretched Length (mm):", font=("Arial", 16))
    stretch_length_label.grid(row=4, column=0, sticky="e", padx=20, pady=10)
    global stretch_length_input
    stretch_length_input = tk.Entry(root, font=("Arial", 14))
    stretch_length_input.grid(row=4, column=1, padx=20)
    calculate_button = tk.Button(root, text="Calculate", font=("Arial", 16), command=calculate_forces)
    calculate_button.grid(row=5, column=0, columnspan=2, pady=20)
    global result_without_weight_label, result_with_weight_label
    result_without_weight_label = tk.Label(root, text="", font=("Arial", 16))
    result_without_weight_label.grid(row=6, column=0, columnspan=2, pady=10)
    result_with_weight_label = tk.Label(root, text="", font=("Arial", 16))
    result_with_weight_label.grid(row=7, column=0, columnspan=2, pady=10)
root = tk.Tk()
root.title("Spring Force Unit 2 Statics")
root.geometry("8000x600")
create_widgets()
root.state('zoomed')
root.mainloop()
