import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk
import threading
import os

from main import analyze


def format_report(data):

    risk = data.get("risk_assessment", {})
    risk_score = risk.get("risk_score", 0)
    risk_level = risk.get("risk_level", "UNKNOWN")

    fake_probability = risk_score

    report = ""
    report += "INSTAGRAM FORENSIC INVESTIGATION REPORT\n"
    report += "-" * 45 + "\n\n"

    report += f"Username: {data.get('username')}\n\n"

    report += "ACCOUNT ANALYSIS\n"
    report += "-" * 20 + "\n"

    uname = "Yes" if data.get("username_suspicious") else "No"

    report += f"Suspicious Username Pattern : {uname}\n"
    report += f"Follower / Following Ratio  : {data.get('follower_ratio')}\n"
    report += f"Activity Classification     : {data.get('activity', {}).get('classification')}\n\n"

    report += "IMAGE FORENSIC ANALYSIS\n"
    report += "-" * 20 + "\n"

    meta = "Yes" if data.get("metadata_found") else "No"
    report += f"Metadata Present            : {meta}\n"

    clone = data.get("clone_score")
    if clone is not None:
        report += f"Clone Detection Score       : {clone}\n"

    if data.get("ela_image"):
        report += "ELA Forensic Image Created  : Yes\n"

    report += "\nRISK ASSESSMENT\n"
    report += "-" * 20 + "\n"

    report += f"Risk Score                  : {risk_score}\n"
    report += f"Risk Level                  : {risk_level}\n"
    report += f"Fake Account Probability    : {fake_probability}%\n"

    report += "\nRECOMMENDATION\n"
    report += "-" * 20 + "\n"
    report += "Perform reverse image search using Google Images or TinEye.\n"

    return report, risk_level


def run_analysis():

    username = username_entry.get().strip()

    if not username:
        messagebox.showwarning("Input Error", "Enter Instagram username")
        return

    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, "Running forensic analysis...\n")

    def task():

        try:

            result = analyze(username)

            formatted, risk_level = format_report(result)

            output_box.delete(1.0, tk.END)
            output_box.insert(tk.END, formatted)

            # Risk color indicator
            if risk_level == "LOW RISK":
                risk_label.config(text="LOW RISK", bg="green")
            elif risk_level == "MEDIUM RISK":
                risk_label.config(text="MEDIUM RISK", bg="orange")
            elif risk_level == "HIGH RISK":
                risk_label.config(text="HIGH RISK", bg="red")

            # Show ELA Image
            ela_path = result.get("ela_image")

            if ela_path and os.path.exists(ela_path):

                img = Image.open(ela_path)
                img = img.resize((250, 250))

                img_tk = ImageTk.PhotoImage(img)

                ela_display.config(image=img_tk)
                ela_display.image = img_tk

            messagebox.showinfo(
                "Analysis completed successfully"
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    threading.Thread(target=task).start()


# Window
window = tk.Tk()
window.title("Instagram Digital Forensics Tool")
window.geometry("900x650")

title = tk.Label(
    window,
    text="Instagram Fake Account & Image Forensic Analyzer",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)


# Username input
frame = tk.Frame(window)
frame.pack(pady=10)

label = tk.Label(frame, text="Instagram Username:", font=("Arial", 12))
label.pack(side=tk.LEFT)

username_entry = tk.Entry(frame, width=30, font=("Arial", 12))
username_entry.pack(side=tk.LEFT, padx=10)


analyze_button = tk.Button(
    window,
    text="Start Investigation",
    command=run_analysis,
    bg="#2E8B57",
    fg="white",
    font=("Arial", 12)
)

analyze_button.pack(pady=10)


# Risk indicator
risk_label = tk.Label(
    window,
    text="RISK LEVEL",
    width=20,
    font=("Arial", 12, "bold"),
    bg="gray",
    fg="white"
)

risk_label.pack(pady=5)


# Output box
output_box = scrolledtext.ScrolledText(
    window,
    width=100,
    height=20,
    font=("Courier", 10)
)

output_box.pack(pady=10)


# ELA Image display
ela_title = tk.Label(
    window,
    text="ELA Image Forensic Evidence",
    font=("Arial", 12, "bold")
)

ela_title.pack()

ela_display = tk.Label(window)
ela_display.pack(pady=10)


window.mainloop()