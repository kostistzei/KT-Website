# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 22:12:14 2025

@author: kotsi

KT Website

"""

from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__, static_folder="static", static_url_path="/static")

# --- Routes ---

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Notes page: list all PDFs starting with "CEE" from /static
@app.route("/notes")
def notes():
    try:
        note_files = [
            f for f in os.listdir(app.static_folder)
            if f.startswith("CEE") and f.endswith(".pdf")
        ]
        note_files.sort(key=str.lower)
    except FileNotFoundError:
        note_files = []
    return render_template("notes.html", notes=note_files)

# Generator page (static HTML with hardcoded links to files in /static)
@app.route("/Generator")
def generator():
    return render_template("Generator.html")

# Optional: force download route (useful if you ever link /download/<file>)
@app.route("/download/<path:filename>")
def download_file(filename):
    try:
        return send_from_directory(app.static_folder, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)

# --- Main ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

