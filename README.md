# Summarizer
It helps you easily summarize texts in PDF files and web pages
---

# PDF and News Summarizer

This project provides a **Graphical User Interface (GUI)** using **Tkinter** for summarizing both PDF files and online news articles. The application extracts the content from PDF files or URLs, generates a summary using **Natural Language Processing (NLP)** techniques, and performs **sentiment analysis** on the text.

## Features

- **PDF Summarization**: Upload a PDF file, extract its text content, summarize the content using the **LSA (Latent Semantic Analysis)** algorithm, and perform sentiment analysis.
- **News Article Summarization**: Input a news article URL, download the article, summarize it using NLP, and perform sentiment analysis on the article content.
- **Sentiment Analysis**: The app uses **TextBlob** to analyze the sentiment of the extracted or downloaded content and categorizes it as **positive**, **negative**, or **neutral**.

## Technologies Used

- **Python**: Backend logic and GUI.
- **Tkinter**: For building the user interface.
- **PyPDF2**: For extracting text from PDF files.
- **TextBlob**: For sentiment analysis and basic text operations.
- **Sumy**: For summarizing PDF content using **LSA**.
- **Newspaper3k**: For scraping and summarizing online articles.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/amirsohly/Summarizer
   ```
2. Install dependencies:
   ```bash
   pip install pypdf2
   pip install sumy
   ```
3. Run the main GUI program:
   ```bash
   python mainwindow.py
   ```

### PDF Summarization

- Click on **"Upload PDF"** to upload a PDF file.
- The text will be extracted, summarized, and the sentiment analysis will be displayed.

### News Article Summarization

- Click on **"News Link"** to enter a news article URL.
- The article will be downloaded, summarized, and the sentiment analysis will be displayed.

## File Structure

- `mainwindow.py`: Launches the GUI and allows users to choose between PDF and link summarization.
- `pdf.py`: Handles the PDF summarization logic.
- `link.py`: Handles the link summarization logic.

## Dependencies

- **Python 3.x**
- **Tkinter**
- **PyPDF2**
- **TextBlob**
- **Newspaper3k**
- **Sumy**

---
