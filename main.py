# ---------------------------------------------
# OCD & Anxiety Detection System
# Dark Theme + Popup Result + ML Logic
# Author: Khushi Patil
# Educational Purpose Only – Not Medical Diagnosis
# ---------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox
import math

# -----------------------------
# Calculate Percentage
# -----------------------------
def calculate_percentage(responses):
    total = sum(responses)
    max_score = len(responses) * 5
    return round((total / max_score) * 100, 2)

# -----------------------------
# ML Probability (Sigmoid Logic)
# -----------------------------
def ml_probability(score):
    probability = 1 / (1 + math.exp(-0.08 * (score - 50)))
    return round(probability * 100, 2)

# -----------------------------
# Classify Severity
# -----------------------------
def classify(score):
    if score <= 33:
        return "Mild"
    elif score <= 66:
        return "Moderate"
    else:
        return "Severe"

# -----------------------------
# Popup Result Window
# -----------------------------
def show_result_popup(ocd_score, ocd_level, anxiety_score, anxiety_level, ocd_prob, anxiety_prob):
    popup = tk.Toplevel(root)
    popup.title("Assessment Result")
    popup.geometry("420x380")
    popup.configure(bg="#1e1e2f")

    tk.Label(popup,
             text="Assessment Summary",
             font=("Helvetica", 18, "bold"),
             bg="#1e1e2f",
             fg="#00ffcc").pack(pady=20)

    tk.Label(popup,
             text=f"OCD Score: {ocd_score}%",
             font=("Arial", 14),
             bg="#1e1e2f",
             fg="white").pack(pady=5)

    tk.Label(popup,
             text=f"OCD Severity: {ocd_level}",
             font=("Arial", 14),
             bg="#1e1e2f",
             fg="#ffcc00").pack(pady=5)

    tk.Label(popup,
             text=f"OCD Risk Probability: {ocd_prob}%",
             font=("Arial", 13),
             bg="#1e1e2f",
             fg="#00ffcc").pack(pady=5)

    tk.Label(popup,
             text="----------------------------------",
             bg="#1e1e2f",
             fg="gray").pack(pady=5)

    tk.Label(popup,
             text=f"Anxiety Score: {anxiety_score}%",
             font=("Arial", 14),
             bg="#1e1e2f",
             fg="white").pack(pady=5)

    tk.Label(popup,
             text=f"Anxiety Severity: {anxiety_level}",
             font=("Arial", 14),
             bg="#1e1e2f",
             fg="#ff4d4d").pack(pady=5)

    tk.Label(popup,
             text=f"Anxiety Risk Probability: {anxiety_prob}%",
             font=("Arial", 13),
             bg="#1e1e2f",
             fg="#00ffcc").pack(pady=5)

    tk.Button(popup,
              text="Close",
              command=popup.destroy,
              bg="#00ffcc",
              fg="black",
              width=12).pack(pady=20)

# -----------------------------
# Predict Function
# -----------------------------
def predict():
    try:
        ocd_responses = []
        anxiety_responses = []

        for i in range(5):
            val = int(ocd_entries[i].get())
            if not 0 <= val <= 5:
                raise ValueError
            ocd_responses.append(val)

        for i in range(5):
            val = int(anxiety_entries[i].get())
            if not 0 <= val <= 5:
                raise ValueError
            anxiety_responses.append(val)

        ocd_percent = calculate_percentage(ocd_responses)
        anxiety_percent = calculate_percentage(anxiety_responses)

        ocd_level = classify(ocd_percent)
        anxiety_level = classify(anxiety_percent)

        ocd_prob = ml_probability(ocd_percent)
        anxiety_prob = ml_probability(anxiety_percent)

        # Update progress bars
        ocd_bar["value"] = ocd_percent
        anxiety_bar["value"] = anxiety_percent

        # Show popup
        show_result_popup(ocd_percent, ocd_level,
                          anxiety_percent, anxiety_level,
                          ocd_prob, anxiety_prob)

    except:
        messagebox.showerror("Error", "Enter numbers between 0 and 5 only.")

# -----------------------------
# Clear Fields
# -----------------------------
def clear():
    for e in ocd_entries + anxiety_entries:
        e.delete(0, tk.END)
    ocd_bar["value"] = 0
    anxiety_bar["value"] = 0

# -----------------------------
# GUI Setup (Dark Theme)
# -----------------------------
root = tk.Tk()
root.title("Mental Health ML Analyzer")
root.geometry("750x820")
root.configure(bg="#1e1e2f")

style = ttk.Style()
style.theme_use('default')
style.configure("TProgressbar",
                thickness=20,
                troughcolor="#2b2b3c",
                background="#00ffcc")

tk.Label(root,
         text="Mental Health Analyzer",
         font=("Helvetica", 22, "bold"),
         bg="#1e1e2f",
         fg="#00ffcc").pack(pady=20)

tk.Label(root,
         text="Rate each from 0 (Never) to 5 (Always)",
         font=("Arial", 14),
         bg="#1e1e2f",
         fg="white").pack()

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=20)

ocd_questions = [
    "Repetitive unwanted thoughts",
    "Repeated checking behavior",
    "Compulsive rituals",
    "Anxiety if rituals skipped",
    "Thoughts affect daily life"
]

anxiety_questions = [
    "Feel nervous or on edge",
    "Trouble relaxing",
    "Frequent restlessness",
    "Excessive worrying",
    "Easily irritated"
]

ocd_entries = []
anxiety_entries = []

tk.Label(frame, text="OCD Assessment",
         font=("Arial", 16, "bold"),
         bg="#1e1e2f",
         fg="#00ffcc").grid(row=0, column=0, pady=10)

for i, q in enumerate(ocd_questions):
    tk.Label(frame, text=q,
             bg="#1e1e2f",
             fg="white").grid(row=i+1, column=0, sticky="w", pady=5)
    e = tk.Entry(frame, width=5, bg="#2b2b3c", fg="white", insertbackground="white")
    e.grid(row=i+1, column=1)
    ocd_entries.append(e)

start = len(ocd_questions) + 2

tk.Label(frame, text="Anxiety Assessment",
         font=("Arial", 16, "bold"),
         bg="#1e1e2f",
         fg="#00ffcc").grid(row=start, column=0, pady=10)

for i, q in enumerate(anxiety_questions):
    tk.Label(frame, text=q,
             bg="#1e1e2f",
             fg="white").grid(row=start+i+1, column=0, sticky="w", pady=5)
    e = tk.Entry(frame, width=5, bg="#2b2b3c", fg="white", insertbackground="white")
    e.grid(row=start+i+1, column=1)
    anxiety_entries.append(e)

btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Analyze", command=predict,
          bg="#00ffcc", fg="black",
          font=("Arial", 14, "bold"), width=15).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Clear", command=clear,
          bg="#ff4d4d", fg="white",
          font=("Arial", 14), width=15).grid(row=0, column=1, padx=10)

tk.Label(root, text="OCD Percentage",
         bg="#1e1e2f", fg="white").pack()
ocd_bar = ttk.Progressbar(root, length=500, maximum=100)
ocd_bar.pack(pady=10)

tk.Label(root, text="Anxiety Percentage",
         bg="#1e1e2f", fg="white").pack()
anxiety_bar = ttk.Progressbar(root, length=500, maximum=100)
anxiety_bar.pack(pady=10)

tk.Label(root,
         text="Educational Use Only | Not Medical Diagnosis",
         bg="#1e1e2f",
         fg="gray").pack(side="bottom", pady=10)

root.mainloop()


