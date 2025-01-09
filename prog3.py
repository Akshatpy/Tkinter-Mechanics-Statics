from PIL import Image, ImageTk, ImageDraw, ImageFont
import tkinter as tk
from tkinter import messagebox, Toplevel
def calculate_moi_rectangle(b, h):
    iz_rect = (1/12)*(b*h*(b**2+h**2))
    return(calc_radius_gyration(b, h, iz_rect))
def calc_radius_gyration(b, h, iz_rect):
    iz_triangle = 1/2 * iz_rect
    area = b*h/2
    radius = (iz_triangle/(area))**0.5
    return radius
def show_solution():
    try:
        b_value = abs(float(base_length_input.get()))
        h_value = abs(float(height_input.get()))
        if b_value < 0 or h_value < 0:
            messagebox.showerror("Input Error", "Base and Height must be positive integers.")
        elif b_value ==0 or h_value == 0:
            messagebox.showerror("Ans","The moment of Inertia is 0")
            return
        radius = calculate_moi_rectangle(b_value, h_value)
        solution_image = Image.open("solution.jpg")
        draw = ImageDraw.Draw(solution_image)
        font = ImageFont.truetype("arial.ttf", 50)
        draw.text((450, 70), f"Breadth: {b_value} mm", fill="black", font=font)
        draw.text((750, 350), f"Height: {h_value} mm", fill="black", font=font)
        solution_image_resized = solution_image.resize((400, 200), Image.Resampling.LANCZOS)
        solution_photo = ImageTk.PhotoImage(solution_image_resized)
        solution_window = Toplevel(root)
        solution_window.title("Solution")
        solution_image_label = tk.Label(solution_window, image=solution_photo)
        solution_image_label.pack(pady=20)
        solution_image_label.image = solution_photo
        result_label = tk.Label(solution_window, text=f"Radius of Gyration: {radius:.2f} mm", font=("Arial", 16))
        result_label.pack(pady=10)
        back_button = tk.Button(solution_window, text="Back to Main", command=solution_window.destroy, font=("Arial", 14))
        back_button.pack(pady=10)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for base and height.")
def create_main_window():
    global root
    root = tk.Tk()
    root.title("Statics Unit3 Question A/16 ")
    root.geometry("800x600")
    question_image = Image.open("question3.png")
    question_image_resized = question_image.resize((400, 200), Image.Resampling.LANCZOS)
    question_photo = ImageTk.PhotoImage(question_image_resized)
    question_image_label = tk.Label(root, image=question_photo)
    question_image_label.pack(pady=20)
    question_image_label.image = question_photo
    title_label = tk.Label(root, text="Moment of Inertia of a Triangle", font=("Arial", 24, "bold"))
    title_label.pack(pady=10)
    base_label = tk.Label(root, text="Base Length (mm):", font=("Arial", 16))
    base_label.pack(pady=5)
    global base_length_input
    base_length_input = tk.Entry(root, font=("Arial", 14))
    base_length_input.pack(pady=5)
    height_label = tk.Label(root, text="Height (mm):", font=("Arial", 16))
    height_label.pack(pady=5)
    global height_input
    height_input = tk.Entry(root, font=("Arial", 14))
    height_input.pack(pady=5)
    calculate_button = tk.Button(root, text="Calculate", command=show_solution, font=("Arial", 16))
    calculate_button.pack(pady=20)
    root.mainloop()
create_main_window()
