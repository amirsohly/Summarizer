#Amirreza_Soheili
#https://github.com/amirsohly/
#https://amirrezasoheili.ir
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
from textblob import TextBlob
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def extract_text_from_pdf(file_path):
    text = ""
    try :
        with open(file_path,'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    except Exception as e:
        messagebox.showerror("Error",f"Failed to extract text from PDF:{e}")
    return text

def summarize_text(text):
    parser = PlaintextParser.from_string(text,Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document,5)
    summary_text = " ".join([str(sentence) for sentence in summary])
    return summary_text

def summarize():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files","*.pdf")])
    if not file_path:
        messagebox.showerror("Error","No file selected")
        return
    text = extract_text_from_pdf(file_path)
    if not text:
        messagebox.showerror("Error","No text extracted from pdf")
        return
    summary_text = summarize_text(text)

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0','end')
    title.insert('1.0',"Extracted PDF Tilte")
    author.delete('1.0','end')
    author.insert('1.0',"Unknown Author")
    publication.delete('1.0','end')
    publication.insert('1.0',"Unknown Date")
    summary.delete('1.0','end')
    summary.insert('1.0',summary_text)
    analysis = TextBlob(text)
    sentiment.delete('1.0','end')
    sentiment.insert('1.0'
                     ,f'Polarity:{analysis.polarity},Sentiment:{"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

root = tk.Tk()
root.title("PDF Summarizer")
root.geometry("1200x700")

tlabel = tk.Label(root,text="PDF Tilte",font=("Calibri",15,"bold"))
tlabel.pack()
title = tk.Text(root, height=1, width=140)
title.config(state='disabled',bg="#dddddd")
title.pack()

alabel = tk.Label(root,text="Author",font=("Calibri",15,"bold"))
alabel.pack()
author = tk.Text(root, height=1, width=140)
author.config(state='disabled',bg="#dddddd")
author.pack()


plabel = tk.Label(root,text="publication Date",font=("Calibri",15,"bold"))
plabel.pack()
publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled',bg="#dddddd")
publication.pack()


slabel = tk.Label(root,text="Summary",font=("Calibri",15,"bold"))
slabel.pack()
summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled',bg="#dddddd")
summary.pack()


selabel = tk.Label(root,text="Sentiment",font=("Calibri",15,"bold"))
selabel.pack()
sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled',bg="#dddddd")
sentiment.pack()

ulabel = tk.Label(root,text="Choose a PDF File",font=("Calibri",15,"bold"))
ulabel.pack()

btn = tk.Button(root,text="Summarize",command=summarize)
btn.pack()

root.mainloop()