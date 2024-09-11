#Amirreza_Soheili
#https://github.com/amirsohly/
#https://amirrezasoheili.ir
import tkinter as tk
import subprocess

def run_file(file_name):
    subprocess.run(['python',file_name])

root = tk.Tk()
root.title("Summarizer")
root.geometry("300x200")

main_label = tk.Label(root,text="Choose an Option",
                      font=("Calibri",15,"bold"))
main_label.pack(pady=20)

pdf_button = tk.Button(root,text="Upload PDF",
                       command=lambda:run_file('pdf.py'),
                       font=("Calibri",12))
pdf_button.pack(pady=10)

link_button = tk.Button(root,text="News Link",
                       command=lambda:run_file('link.py'),
                       font=("Calibri",12))
link_button.pack(pady=10)

root.mainloop()