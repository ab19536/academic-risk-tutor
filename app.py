import tkinter as tk
from tkinter import messagebox

from tutor.integrated_tutor import run_integrated_tutor


def generate():
    try:
        result = run_integrated_tutor(
            name_entry.get(),
            float(ia1_entry.get()),
            float(ia2_entry.get()),
            float(assignment_entry.get()),
            float(attendance_entry.get()),
            "Data Structures",
            topic_entry.get()
        )

        output.delete("1.0", tk.END)
        output.insert(
            tk.END,
            f"Academic Score: {result['risk']['academic_score']}\n"
            f"Risk Level: {result['risk']['risk_level']}\n\n"
            f"Resources:\n"
            + "\n".join(
                f"- {r}" for r in result["resources"]
            )
            + "\n\nTutor Response:\n"
            + result["response"]
        )

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter valid numeric scores."
        )


root = tk.Tk()
root.title("Academic Risk Virtual Tutor")
root.geometry("750x650")

tk.Label(root, text="Student Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="IA1 Score").pack()
ia1_entry = tk.Entry(root)
ia1_entry.pack()

tk.Label(root, text="IA2 Score").pack()
ia2_entry = tk.Entry(root)
ia2_entry.pack()

tk.Label(root, text="Assignment Score").pack()
assignment_entry = tk.Entry(root)
assignment_entry.pack()

tk.Label(root, text="Attendance").pack()
attendance_entry = tk.Entry(root)
attendance_entry.pack()

tk.Label(root, text="Weak Topic").pack()
topic_entry = tk.Entry(root)
topic_entry.insert(0, "Arrays")
topic_entry.pack()

tk.Button(
    root,
    text="Generate Tutor Recommendation",
    command=generate
).pack(pady=10)

output = tk.Text(root, height=25, width=90)
output.pack()

root.mainloop()
