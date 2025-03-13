import tkinter as tk
from tkinter import ttk, messagebox
import joblib
import numpy as np

# Load the trained Random Forest model
model = joblib.load('random_forest_model.pkl')

# Function to predict grade based on user inputs
def predict_grade():
    try:
        # Get input values from entry fields
        p1 = float(entry_p1.get())
        c1 = float(entry_c1.get())
        p2 = float(entry_p2.get())
        c2 = float(entry_c2.get())
        p3 = float(entry_p3.get())
        c3 = float(entry_c3.get())
        r1 = float(entry_r1.get())
        t1 = float(entry_t1.get())
        p3t = float(entry_p3t.get())

        # Prepare input array for prediction
        input_features = np.array([[p1, c1, p2, c2, p3, c3, r1, t1, p3t]])
        
        # Make prediction
        prediction = model.predict(input_features)
        
        # Display the predicted grade
        result_label.config(text=f"Predicted Grade: {prediction[0]}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numerical values.")

# Create the main application window
root = tk.Tk()
root.title("Grade Prediction App")
root.geometry("400x400")

# Input labels and entry fields
ttk.Label(root, text="P1 (Marks):").grid(row=0, column=0, padx=10, pady=5)
entry_p1 = ttk.Entry(root)
entry_p1.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="C1 (Credits):").grid(row=1, column=0, padx=10, pady=5)
entry_c1 = ttk.Entry(root)
entry_c1.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="P2 (Marks):").grid(row=2, column=0, padx=10, pady=5)
entry_p2 = ttk.Entry(root)
entry_p2.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="C2 (Credits):").grid(row=3, column=0, padx=10, pady=5)
entry_c2 = ttk.Entry(root)
entry_c2.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(root, text="P3 (Marks):").grid(row=4, column=0, padx=10, pady=5)
entry_p3 = ttk.Entry(root)
entry_p3.grid(row=4, column=1, padx=10, pady=5)

ttk.Label(root, text="C3 (Credits):").grid(row=5, column=0, padx=10, pady=5)
entry_c3 = ttk.Entry(root)
entry_c3.grid(row=5, column=1, padx=10, pady=5)

ttk.Label(root, text="R1 (Report Marks):").grid(row=6, column=0, padx=10, pady=5)
entry_r1 = ttk.Entry(root)
entry_r1.grid(row=6, column=1, padx=10, pady=5)

ttk.Label(root, text="T1 (Thesis Marks):").grid(row=7, column=0, padx=10, pady=5)
entry_t1 = ttk.Entry(root)
entry_t1.grid(row=7, column=1, padx=10, pady=5)

ttk.Label(root, text="P3T (Project 3 Total):").grid(row=8, column=0, padx=10, pady=5)
entry_p3t = ttk.Entry(root)
entry_p3t.grid(row=8,column =  1,padx =  10,pady

