import tkinter as tk
from tkinter import messagebox


# MAIN WINDOW

root = tk.Tk()
root.title("Smart Student Performance Prediction System")
root.geometry("950x700")
root.configure(bg="#EAF2F8")
root.resizable(False, False)


# COLORS

BG_COLOR = "#EAF2F8"
WHITE = "#FFFFFF"

DARK = "#17202A"
GRAY = "#607D8B"

BLUE = "#1565C0"
LIGHT_BLUE = "#D6EAF8"

PURPLE = "#6A1B9A"
LIGHT_PURPLE = "#E8DAEF"

GREEN = "#2E7D32"
LIGHT_GREEN = "#D5F5E3"

ORANGE = "#EF6C00"
LIGHT_ORANGE = "#FDEBD0"

RED = "#C62828"
LIGHT_RED = "#FADBD8"

BORDER = "#AAB7B8"


# PREDICTION FUNCTION

def submit():

    student_id = entry_student_id.get().strip()
    name = entry_name.get().strip()

    attendance = entry_attendance.get().strip()
    study_hours = entry_study_hours.get().strip()
    internal_marks = entry_internal_marks.get().strip()
    assignment = entry_assignment.get().strip()
    previous_performance = entry_previous_performance.get().strip()

    # Check Empty Fields

    if not student_id or not name or not attendance or not study_hours \
            or not internal_marks or not assignment or not previous_performance:

        messagebox.showerror(
            "Missing Information",
            "Please enter all student and academic details."
        )

        return

    # Convert Values

    try:

        attendance = float(attendance)
        study_hours = float(study_hours)
        internal_marks = float(internal_marks)
        assignment = float(assignment)
        previous_performance = float(previous_performance)

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numeric values."
        )

        return

    # Validation

    if not 0 <= attendance <= 100:

        messagebox.showerror(
            "Invalid Attendance",
            "Attendance must be between 0 and 100."
        )

        return

    if not 0 <= study_hours <= 24:

        messagebox.showerror(
            "Invalid Study Hours",
            "Study Hours must be between 0 and 24."
        )

        return

    if not 0 <= internal_marks <= 100:

        messagebox.showerror(
            "Invalid Internal Marks",
            "Internal Marks must be between 0 and 100."
        )

        return

    if not 0 <= assignment <= 100:

        messagebox.showerror(
            "Invalid Assignment",
            "Assignment Completion must be between 0 and 100."
        )

        return

    if not 0 <= previous_performance <= 100:

        messagebox.showerror(
            "Invalid Performance",
            "Previous Performance must be between 0 and 100."
        )

        return

    # PERFORMANCE CALCULATION

    # Convert study hours into a score.
    # 8 hours/day = 100 score.

    study_hours_score = min(
        (study_hours / 8) * 100,
        100
    )

    # Current performance score

    performance_score = (
        attendance * 0.20
        + study_hours_score * 0.20
        + internal_marks * 0.40
        + assignment * 0.20
    )

    # Final score
    # 80% current performance
    # 20% previous performance

    final_score = (
        performance_score * 0.80
        + previous_performance * 0.20
    )

    # PERFORMANCE PREDICTION

    if final_score >= 80:

        performance = "EXCELLENT"
        risk = "LOW"

        recommendation = (
            "Excellent performance! Maintain your current "
            "study pattern and continue regular practice."
        )

        result_frame.configure(
            bg=LIGHT_GREEN
        )

        output_prediction.configure(
            bg=LIGHT_GREEN,
            fg=GREEN
        )

        output_risk.configure(
            bg=LIGHT_GREEN,
            fg=GREEN
        )

        output_recommendation.configure(
            bg=LIGHT_GREEN,
            fg=DARK
        )

    elif final_score >= 65:

        performance = "GOOD"
        risk = "LOW"

        recommendation = (
            "Good performance. Maintain attendance "
            "and continue regular study."
        )

        result_frame.configure(
            bg=LIGHT_BLUE
        )

        output_prediction.configure(
            bg=LIGHT_BLUE,
            fg=BLUE
        )

        output_risk.configure(
            bg=LIGHT_BLUE,
            fg=BLUE
        )

        output_recommendation.configure(
            bg=LIGHT_BLUE,
            fg=DARK
        )

    elif final_score >= 50:

        performance = "AVERAGE"
        risk = "MEDIUM"

        recommendation = (
            "Increase study hours and improve "
            "assignment completion."
        )

        result_frame.configure(
            bg=LIGHT_ORANGE
        )

        output_prediction.configure(
            bg=LIGHT_ORANGE,
            fg=ORANGE
        )

        output_risk.configure(
            bg=LIGHT_ORANGE,
            fg=ORANGE
        )

        output_recommendation.configure(
            bg=LIGHT_ORANGE,
            fg=DARK
        )

    else:

        performance = "AT RISK"
        risk = "HIGH"

        recommendation = (
            "Improve attendance, study hours, "
            "and assignment completion."
        )

        result_frame.configure(
            bg=LIGHT_RED
        )

        output_prediction.configure(
            bg=LIGHT_RED,
            fg=RED
        )

        output_risk.configure(
            bg=LIGHT_RED,
            fg=RED
        )

        output_recommendation.configure(
            bg=LIGHT_RED,
            fg=DARK
        )

    # DISPLAY RESULT

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


# CLEAR FUNCTION

def clear():

    entry_student_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)

    entry_attendance.delete(0, tk.END)
    entry_study_hours.delete(0, tk.END)
    entry_internal_marks.delete(0, tk.END)
    entry_assignment.delete(0, tk.END)
    entry_previous_performance.delete(0, tk.END)

    result_frame.configure(
        bg=WHITE
    )

    output_prediction.configure(
        text="Prediction: Waiting for input...",
        bg=WHITE,
        fg=DARK
    )

    output_risk.configure(
        text="Risk Level: -",
        bg=WHITE,
        fg=DARK
    )

    output_recommendation.configure(
        text="Recommendation: -",
        bg=WHITE,
        fg=DARK
    )


# EXIT FUNCTION

def exit_app():
    root.destroy()


# HEADER

header_frame = tk.Frame(
    root,
    bg=BLUE,
    height=90
)

header_frame.pack(
    fill="x"
)

header_frame.pack_propagate(False)


heading = tk.Label(
    header_frame,
    text="SMART STUDENT PERFORMANCE",
    font=("Arial", 22, "bold"),
    bg=BLUE,
    fg=WHITE
)

heading.pack(
    pady=(15, 0)
)


subtitle = tk.Label(
    header_frame,
    text="Prediction & Academic Performance Analysis System",
    font=("Arial", 10),
    bg=BLUE,
    fg="#D6EAF8"
)

subtitle.pack(
    pady=3
)


# MAIN CONTENT

content_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

content_frame.pack(
    padx=30,
    pady=20
)


# STUDENT INFORMATION

student_frame = tk.LabelFrame(
    content_frame,
    text="  Student Information  ",
    font=("Arial", 13, "bold"),
    bg=WHITE,
    fg=PURPLE,
    bd=2,
    relief="groove",
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
    font=("Arial", 11, "bold"),
    bg=WHITE,
    fg=DARK
).grid(
    row=0,
    column=0,
    sticky="w",
    pady=10
)


entry_student_id = tk.Entry(
    student_frame,
    width=25,
    font=("Arial", 11),
    relief="solid",
    bd=1
)

entry_student_id.grid(
    row=0,
    column=1,
    padx=(20, 0),
    pady=10
)


# Name

tk.Label(
    student_frame,
    text="Name",
    font=("Arial", 11, "bold"),
    bg=WHITE,
    fg=DARK
).grid(
    row=1,
    column=0,
    sticky="w",
    pady=10
)


entry_name = tk.Entry(
    student_frame,
    width=25,
    font=("Arial", 11),
    relief="solid",
    bd=1
)

entry_name.grid(
    row=1,
    column=1,
    padx=(20, 0),
    pady=10
)


# ACADEMIC INFORMATION

academic_frame = tk.LabelFrame(
    content_frame,
    text="  Academic Information  ",
    font=("Arial", 13, "bold"),
    bg=WHITE,
    fg=BLUE,
    bd=2,
    relief="groove",
    padx=20,
    pady=15
)

academic_frame.grid(
    row=0,
    column=1,
    sticky="nsew"
)


# Academic Field Function

def create_academic_field(row, label_text):

    label = tk.Label(
        academic_frame,
        text=label_text,
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=DARK
    )

    label.grid(
        row=row,
        column=0,
        sticky="w",
        pady=6
    )

    entry = tk.Entry(
        academic_frame,
        width=20,
        font=("Arial", 10),
        relief="solid",
        bd=1
    )

    entry.grid(
        row=row,
        column=1,
        padx=(15, 0),
        pady=6
    )

    return entry


# Academic Inputs

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


# BUTTONS

button_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

button_frame.pack(
    pady=5
)


# Predict Button

submit_btn = tk.Button(
    button_frame,
    text="Predict Performance",
    command=submit,
    bg=BLUE,
    fg=WHITE,
    activebackground="#0D47A1",
    activeforeground=WHITE,
    font=("Arial", 11, "bold"),
    width=20,
    height=2,
    relief="flat",
    cursor="hand2"
)

submit_btn.grid(
    row=0,
    column=0,
    padx=8
)


# Clear Button

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    command=clear,
    bg=ORANGE,
    fg=WHITE,
    activebackground="#E65100",
    activeforeground=WHITE,
    font=("Arial", 11, "bold"),
    width=12,
    height=2,
    relief="flat",
    cursor="hand2"
)

clear_btn.grid(
    row=0,
    column=1,
    padx=8
)


# Exit Button

exit_btn = tk.Button(
    button_frame,
    text="Exit",
    command=exit_app,
    bg=RED,
    fg=WHITE,
    activebackground="#8E0000",
    activeforeground=WHITE,
    font=("Arial", 11, "bold"),
    width=12,
    height=2,
    relief="flat",
    cursor="hand2"
)

exit_btn.grid(
    row=0,
    column=2,
    padx=8
)


# PREDICTION RESULT TITLE

result_title = tk.Label(
    root,
    text="Prediction Result",
    font=("Arial", 15, "bold"),
    bg=BG_COLOR,
    fg=PURPLE
)

result_title.pack(
    pady=(12, 8)
)


# RESULT FRAME

result_frame = tk.Frame(
    root,
    bg=WHITE,
    bd=2,
    relief="groove",
    padx=30,
    pady=12
)

result_frame.pack(
    padx=50,
    fill="x"
)


# Prediction

output_prediction = tk.Label(
    result_frame,
    text="Prediction: Waiting for input...",
    font=("Arial", 13, "bold"),
    bg=WHITE,
    fg=DARK,
    justify="center"
)

output_prediction.pack(
    pady=4
)


# Risk

output_risk = tk.Label(
    result_frame,
    text="Risk Level: -",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    fg=DARK
)

output_risk.pack(
    pady=4
)


# Recommendation

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
    pady=4
)


# FOOTER
footer = tk.Label(
    root,
    text="Smart Academic Analysis System",
    font=("Arial", 9),
    bg=BG_COLOR,
    fg=GRAY
)

footer.pack(
    pady=10
)


# RUN APPLICATION

root.mainloop()
