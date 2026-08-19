import tkinter as tk
from tkinter import messagebox


# =========================
# Main Window
# =========================

root = tk.Tk()
root.title("Smart Student Performance Prediction System")
root.geometry("950x700")
root.configure(bg="#f2f4f7")
root.resizable(False, False)


# =========================
# Colors
# =========================

BG_COLOR = "#f2f4f7"
WHITE = "#ffffff"
DARK = "#263238"
BLUE = "#1976d2"
GREEN = "#2e7d32"
RED = "#d32f2f"
LIGHT_BLUE = "#e3f2fd"
LIGHT_GREEN = "#e8f5e9"
LIGHT_RED = "#ffebee"
BORDER = "#d0d7de"


# =========================
# Functions
# =========================

def submit():
    student_id = entry_student_id.get().strip()
    name = entry_name.get().strip()
    attendance = entry_attendance.get().strip()
    study_hours = entry_study_hours.get().strip()
    internal_marks = entry_internal_marks.get().strip()
    assignment = entry_assignment.get().strip()
    previous_performance = entry_previous_performance.get().strip()

    # Check empty fields
    if not all([
        student_id,
        name,
        attendance,
        study_hours,
        internal_marks,
        assignment,
        previous_performance
    ]):
        messagebox.showerror(
            "Missing Information",
            "Please enter all student and academic details."
        )
        return

    try:
        attendance = float(attendance)
        study_hours = float(study_hours)
        internal_marks = float(internal_marks)
        assignment = float(assignment)
        previous_performance = float(previous_performance)

        # Validation
        if not 0 <= attendance <= 100:
            messagebox.showerror(
                "Invalid Input",
                "Attendance must be between 0 and 100."
            )
            return

        if not 0 <= study_hours <= 24:
            messagebox.showerror(
                "Invalid Input",
                "Study Hours must be between 0 and 24."
            )
            return

        if not 0 <= internal_marks <= 100:
            messagebox.showerror(
                "Invalid Input",
                "Internal Marks must be between 0 and 100."
            )
            return

        if not 0 <= assignment <= 100:
            messagebox.showerror(
                "Invalid Input",
                "Assignment Completion must be between 0 and 100."
            )
            return

        if not 0 <= previous_performance <= 100:
            messagebox.showerror(
                "Invalid Input",
                "Previous Performance must be between 0 and 100."
            )
            return

        # =========================
        # Prediction Calculation
        # =========================

        study_hours_score = min((study_hours / 8) * 100, 100)

        performance_score = (
            attendance * 0.20
            + study_hours_score * 0.20
            + internal_marks * 0.40
            + assignment * 0.20
        )

        final_score = (
            performance_score * 0.80
            + previous_performance * 0.20
        )

        # =========================
        # Prediction
        # =========================

        if final_score >= 80:
            performance = "EXCELLENT"
            risk = "LOW"
            recommendation = (
                "Maintain your current study pattern "
                "and continue regular practice."
            )

            result_frame.configure(bg=LIGHT_GREEN)
            output_prediction.configure(bg=LIGHT_GREEN, fg=GREEN)
            output_risk.configure(bg=LIGHT_GREEN, fg=GREEN)
            output_recommendation.configure(bg=LIGHT_GREEN, fg=DARK)

        elif final_score >= 65:
            performance = "GOOD"
            risk = "LOW"
            recommendation = (
                "Maintain good attendance and continue "
                "regular study."
            )

            result_frame.configure(bg=LIGHT_BLUE)
            output_prediction.configure(bg=LIGHT_BLUE, fg=BLUE)
            output_risk.configure(bg=LIGHT_BLUE, fg=BLUE)
            output_recommendation.configure(bg=LIGHT_BLUE, fg=DARK)

        elif final_score >= 50:
            performance = "AVERAGE"
            risk = "MEDIUM"
            recommendation = (
                "Increase study hours and improve "
                "assignment completion."
            )

            result_frame.configure(bg="#fff8e1")
            output_prediction.configure(bg="#fff8e1", fg="#f57c00")
            output_risk.configure(bg="#fff8e1", fg="#f57c00")
            output_recommendation.configure(bg="#fff8e1", fg=DARK)

        else:
            performance = "AT RISK"
            risk = "HIGH"
            recommendation = (
                "Improve attendance, study hours, "
                "and assignment completion."
            )

            result_frame.configure(bg=LIGHT_RED)
            output_prediction.configure(bg=LIGHT_RED, fg=RED)
            output_risk.configure(bg=LIGHT_RED, fg=RED)
            output_recommendation.configure(bg=LIGHT_RED, fg=DARK)

        # =========================
        # Display Result
        # =========================

        output_prediction.config(
            text=f"Prediction: {performance}\n"
                 f"Performance Score: {final_score:.2f}%"
        )

        output_risk.config(
            text=f"Risk Level: {risk}"
        )

        output_recommendation.config(
            text=f"Recommendation:\n{recommendation}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numeric values."
        )


def clear():
    entry_student_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_attendance.delete(0, tk.END)
    entry_study_hours.delete(0, tk.END)
    entry_internal_marks.delete(0, tk.END)
    entry_assignment.delete(0, tk.END)
    entry_previous_performance.delete(0, tk.END)

    output_prediction.config(
        text="Prediction: Waiting for input...",
        fg=DARK,
        bg=WHITE
    )

    output_risk.config(
        text="Risk Level: -",
        fg=DARK,
        bg=WHITE
    )

    output_recommendation.config(
        text="Recommendation: -",
        fg=DARK,
        bg=WHITE
    )

    result_frame.configure(bg=WHITE)


def exit_app():
    root.destroy()


# =========================
# Main Heading
# =========================

heading = tk.Label(
    root,
    text="SMART STUDENT PERFORMANCE PREDICTION SYSTEM",
    font=("Arial", 22, "bold"),
    bg=BG_COLOR,
    fg=DARK
)

heading.pack(pady=(20, 5))


subtitle = tk.Label(
    root,
    text="Student Academic Performance Analysis",
    font=("Arial", 11),
    bg=BG_COLOR,
    fg="#607d8b"
)

subtitle.pack(pady=(0, 15))


# =========================
# Main Content
# =========================

content_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

content_frame.pack(
    padx=30,
    fill="x"
)


# =========================
# Student Information Frame
# =========================

student_frame = tk.LabelFrame(
    content_frame,
    text="  Student Information  ",
    font=("Arial", 13, "bold"),
    bg=WHITE,
    fg=BLUE,
    bd=1,
    relief="solid",
    padx=20,
    pady=15
)

student_frame.grid(
    row=0,
    column=0,
    padx=(0, 15),
    sticky="nsew"
)


# Student ID
tk.Label(
    student_frame,
    text="Student ID",
    font=("Arial", 11),
    bg=WHITE,
    fg=DARK
).grid(
    row=0,
    column=0,
    sticky="w",
    pady=8
)

entry_student_id = tk.Entry(
    student_frame,
    width=28,
    font=("Arial", 11),
    relief="solid",
    bd=1
)

entry_student_id.grid(
    row=0,
    column=1,
    padx=(20, 0),
    pady=8
)


# Name
tk.Label(
    student_frame,
    text="Name",
    font=("Arial", 11),
    bg=WHITE,
    fg=DARK
).grid(
    row=1,
    column=0,
    sticky="w",
    pady=8
)

entry_name = tk.Entry(
    student_frame,
    width=28,
    font=("Arial", 11),
    relief="solid",
    bd=1
)

entry_name.grid(
    row=1,
    column=1,
    padx=(20, 0),
    pady=8
)


# =========================
# Academic Information Frame
# =========================

academic_frame = tk.LabelFrame(
    content_frame,
    text="  Academic Information  ",
    font=("Arial", 13, "bold"),
    bg=WHITE,
    fg=BLUE,
    bd=1,
    relief="solid",
    padx=20,
    pady=15
)

academic_frame.grid(
    row=0,
    column=1,
    sticky="nsew"
)


def create_academic_field(row, label_text):
    tk.Label(
        academic_frame,
        text=label_text,
        font=("Arial", 11),
        bg=WHITE,
        fg=DARK
    ).grid(
        row=row,
        column=0,
        sticky="w",
        pady=6
    )

    entry = tk.Entry(
        academic_frame,
        width=22,
        font=("Arial", 11),
        relief="solid",
        bd=1
    )

    entry.grid(
        row=row,
        column=1,
        padx=(20, 0),
        pady=6
    )

    return entry


entry_attendance = create_academic_field(
    0,
    "Attendance (%)"
)

entry_study_hours = create_academic_field(
    1,
    "Study Hours / Day"
)

entry_internal_marks = create_academic_field(
    2,
    "Internal Marks (%)"
)

entry_assignment = create_academic_field(
    3,
    "Assignment (%)"
)

entry_previous_performance = create_academic_field(
    4,
    "Previous Performance (%)"
)


# =========================
# Buttons
# =========================

button_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

button_frame.pack(pady=18)


submit_btn = tk.Button(
    button_frame,
    text="Predict Performance",
    command=submit,
    bg=BLUE,
    fg="white",
    activebackground="#1565c0",
    activeforeground="white",
    font=("Arial", 11, "bold"),
    width=20,
    height=1,
    relief="flat",
    cursor="hand2"
)

submit_btn.grid(
    row=0,
    column=0,
    padx=8
)


clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear,
    bg=GREEN,
    fg="white",
    activebackground="#1b5e20",
    activeforeground="white",
    font=("Arial", 11, "bold"),
    width=12,
    height=1,
    relief="flat",
    cursor="hand2"
)

clear_btn.grid(
    row=0,
    column=1,
    padx=8
)


exit_btn = tk.Button(
    button_frame,
    text="Exit",
    command=exit_app,
    bg=RED,
    fg="white",
    activebackground="#b71c1c",
    activeforeground="white",
    font=("Arial", 11, "bold"),
    width=12,
    height=1,
    relief="flat",
    cursor="hand2"
)

exit_btn.grid(
    row=0,
    column=2,
    padx=8
)


# =========================
# Prediction Result
# =========================

result_title = tk.Label(
    root,
    text="Prediction Result",
    font=("Arial", 15, "bold"),
    bg=BG_COLOR,
    fg=DARK
)

result_title.pack(pady=(5, 8))


result_frame = tk.Frame(
    root,
    bg=WHITE,
    bd=1,
    relief="solid",
    padx=25,
    pady=15
)

result_frame.pack(
    padx=50,
    fill="x"
)


output_prediction = tk.Label(
    result_frame,
    text="Prediction: Waiting for input...",
    font=("Arial", 13, "bold"),
    bg=WHITE,
    fg=DARK,
    justify="center"
)

output_prediction.pack(
    pady=5
)


output_risk = tk.Label(
    result_frame,
    text="Risk Level: -",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    fg=DARK
)

output_risk.pack(
    pady=5
)


output_recommendation = tk.Label(
    result_frame,
    text="Recommendation: -",
    font=("Arial", 11),
    bg=WHITE,
    fg=DARK,
    justify="center",
    wraplength=750
)

output_recommendation.pack(
    pady=5
)


# =========================
# Footer
# =========================

footer = tk.Label(
    root,
    text="Smart Academic Analysis System",
    font=("Arial", 9),
    bg=BG_COLOR,
    fg="#78909c"
)

footer.pack(
    pady=12
)


# =========================
# Start Application
# =========================

root.mainloop()

