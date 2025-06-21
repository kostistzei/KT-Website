# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 22:12:14 2025

@author: kotsi

KT Website

"""

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Notes page
@app.route("/notes")
def notes():
    # Automatically list all PDFs starting with "CEE" from the static folder
    note_files = [f for f in os.listdir("static") if f.startswith("CEE") and f.endswith(".pdf")]
    return render_template("notes.html", notes=note_files)

# File download route
@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory("static", filename, as_attachment=True)

if __name__ == "__main__":
    import sys
    if not hasattr(sys, 'ps1'):
        app.run(debug=True, use_reloader=False)
