from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import numpy as np
import math
def update_image(oa, ab, theta, theta2, theta3, force, result_text):
   beta = math.degrees(theta3 - theta2)
   try:
       base_image = Image.open("diagram.jpg").convert("RGB")
       font = ImageFont.truetype("arial.ttf", 30)
       draw = ImageDraw.Draw(base_image)
       draw.text((340, 373), f"OA: {oa} m", fill="blue", font=font)
       draw.text((865, 409), f"AB: {ab} m", fill="blue", font=font)
       draw.text((1088, 311), f"Theta: {math.degrees(theta):.1f}°", fill="blue", font=font)
       draw.text((409, 209), f"α: {math.degrees(theta2):.1f}°", fill="blue", font=font)
       draw.text((670, 460), f"β: {(beta):.1f}°", fill="blue", font=font)
       draw.text((570, 554), f"λ: {math.degrees(theta3):.1f}°", fill="blue", font=font)
       draw.text((1080, 435), f"Force: {force} kN", fill="blue", font=font)
       base_image = base_image.resize((root.winfo_width()-150, root.winfo_height() - 300), Image.Resampling.LANCZOS)
       annotated_image = ImageTk.PhotoImage(base_image)
       image_label.config(image=annotated_image)
       image_label.image = annotated_image
       result_label.config(text=f"Result: {result_text}")
   except Exception as e:
       result_label.config(text=f"Error updating image: {e}")
def calculate_moment():
   try:
       oa = float(entry_oa.get())
       ab = float(entry_ab.get())
       theta = float(entry_theta.get())
       theta2 = float(entry_theta2.get())
       theta3 = float(entry_theta3.get())
       force = float(entry_force.get())
       choice = choice_var.get()
       if oa <= 0 or ab <= 0 or force <= 0:
           raise ValueError("Lengths and force must be positive values.")
       if theta > 180 or theta2 > 180 or theta2 < 0 or theta3 > 180 or theta3 < 0:
           raise ValueError("Angles (theta, theta2, theta3) must be between 0 and 180 degrees.")
       theta = math.radians(theta)
       theta2 = math.radians(theta2)
       theta3 = math.radians(theta3)
       beta = math.degrees(theta3 - theta2)
       gamma = 90 + beta - math.degrees(theta)
       r_vector = np.array([oa * math.cos(theta2) + ab * math.cos(math.radians(beta)),
                            -oa * math.sin(theta2) + ab * math.sin(math.radians(beta)), 0])
       f_vector = np.array([force * math.sin(math.radians(gamma)),
                            -force * math.cos(math.radians(gamma)), 0])
       mo = np.cross(r_vector, f_vector)
       if choice == "1 - Calculate Moment about O (Mo)":
           result_text = f"The moment about O (Mo) is {mo[2]:.2f} kN·m"
       elif choice == "2 - Calculate Moment about A (Ma)":
           ma = -force * ab * math.sin(theta)
           result_text = f"The moment about A (Ma) is {ma:.2f} kN·m"
       elif choice == "3 - Calculate Theta for Max Mo":
           result_text = "Option 3 calculation is not implemented yet."
       else:
           result_text = "Invalid choice."
       update_image(oa, ab, theta, theta2, theta3, force, result_text)
       calc_frame.pack_forget()
       result_frame.pack(fill=BOTH, expand=True)
   except ValueError as ve:
       messagebox.showerror("Input Error", str(ve))
   except Exception as e:
       messagebox.showerror("Error", str(e))
def calculate():
   result_frame.pack_forget()
   calc_frame.pack(fill=BOTH, expand=True)
root = Tk()
root.title("Statics 2/55 Unit 1 Assignment")
root.geometry("700x500")
calc_frame = Frame(root)
calc_frame.pack(fill=BOTH, expand=True)
initial_image = Image.open("question.png")
root.update_idletasks()
initial_image = initial_image.resize((root.winfo_width(), root.winfo_height() - 200), Image.Resampling.LANCZOS)
initial_photo = ImageTk.PhotoImage(initial_image)
image_label = Label(calc_frame, image=initial_photo)
image_label.image = initial_photo
image_label.pack(pady=10)
Label(calc_frame, text="Enter the length of OA (metres):").pack(anchor=W)
entry_oa = Entry(calc_frame)
entry_oa.pack()
Label(calc_frame, text="Enter the length of AB (metres):").pack(anchor=W)
entry_ab = Entry(calc_frame)
entry_ab.pack()
Label(calc_frame, text="Enter the value of theta (degrees):").pack(anchor=W)
entry_theta = Entry(calc_frame)
entry_theta.pack()
Label(calc_frame, text="Enter angle of OA with Horizontal (degrees):").pack(anchor=W)
entry_theta2 = Entry(calc_frame)
entry_theta2.pack()
Label(calc_frame, text="Enter central angle at A (degrees):").pack(anchor=W)
entry_theta3 = Entry(calc_frame)
entry_theta3.pack()
Label(calc_frame, text="Enter force applied (kN):").pack(anchor=W)
entry_force = Entry(calc_frame)
entry_force.pack()
Label(calc_frame, text="Choose calculation:").pack(anchor=W)
choice_var = StringVar()
choice_dropdown = ttk.Combobox(calc_frame, textvariable=choice_var, width=35)
choice_dropdown['values'] = [
   "1 - Calculate Moment about O (Mo)",
   "2 - Calculate Moment about A (Ma)",
   "3 - Calculate Theta for Max (Mo)"
]
choice_dropdown.pack()
choice_dropdown.current(0)
calculate_button = Button(calc_frame, text="Calculate", command=calculate_moment,font=("Arial", 10), width=10, height=3,bg="green")
calculate_button.place(x=890,y=420)
result_frame = Frame(root)
result_label = Label(result_frame, text="", fg="blue", font=("Arial", 20))
result_label.pack(pady=10)
def onclick():
   calculate()
   update_image()
go_back_button = Button(result_frame, text="Go to diagram", command=onclick, font=("Arial", 14))
go_back_button.pack(pady=5)
root.state('zoomed')
root.mainloop()
