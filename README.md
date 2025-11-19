## 🌍 Currency Converter – Python Tkinter Project
This Currency Converter project is a desktop application built using Python. It allows users to convert values from one currency to another using live exchange rates fetched through an external API. The application uses a graphical user interface (GUI) created with Tkinter, enhanced with images using Pillow, and displays real-time date and time using the Datetime module.

![image alt](https://github.com/Sujithandra/CURRENCY-CONVERTER/blob/37a51391aea522d1dbde75ac4d19d66276b5b2ce/pictures/WhatsApp%20Image%202025-11-19%20at%2021.25.24%20(1).jpeg)

-------------

## 🧩 Project Overview
This Currency Converter application provides:
- Real-time currency conversion
- Simple and modern Tkinter-based GUI
- API integration using requests
- Clean output with timestamp
- Support for major global currencies
- Error handling for invalid inputs
- Image integration for a more engaging UI

This project is ideal for beginners learning API integration, GUI programming, and Python modules.

----------------------------
## 🧰 Tech Stack

Technology & Usage
----
- Python 3   --    Core programming
- Tkinter	  --   GUI development
- Requests  --	  Fetching API data
- Pillow (PIL)  --	  Displaying images
- Datetime   --   	Showing last updated time

----------------- 
## 📦 Detailed Module Explanation
Below is a detailed explanation of every module used in this project

---------
### 1️. Tkinter – GUI (Graphical User Interface)

Tkinter is Python’s standard GUI (Graphical User Interface) library. It allows developers to create desktop applications using windows, buttons, labels, dropdowns, frames, images, etc.

It comes pre-installed with Python, so no external installation is required.

Tkinter is a wrapper around the Tcl/Tk GUI framework, providing tools to develop:
Windows
- Buttons
- Labels
- Textboxes
- Dropdown menus
- Frames and layouts
- Dialogs
- Images
- Event-driven applications

### Import Tkinter
Tkinter can be imported in three different ways, depending on your requirement.

## Method 1: Import Everything (Most Common)

from tkinter import *

What it does:

  - Imports all Tkinter classes, widgets, and constants
  - Allows you to use widgets directly without module prefix

✔ Best for:
- Beginners
- Small projects
- Quick prototypes
- Clean and short code

##  Method 2: Import Tkinter with Alias (Recommended for Large Apps)

import tkinter as tk

What it does:

- Imports Tkinter as a module
- All widgets must be prefixed with tk.

✔ Best for:

- Large applications
- Avoiding name conflicts
- Professional codebase
- Better readability

##  Method 3: Import ttk Separately (For Modern Widgets)
Tkinter’s modern widgets (Combobox, Treeview, Notebook, etc.) come from the ttk module.

from tkinter import ttk

✔ Best for:

- Modern UI
- Dropdowns
- Tables
- Improved look & feel

Usage in this project:
- Creating the main window (Tk())
- Designing labels, text fields, buttons
- Creating dropdown menus using ttk.Combobox
- Displaying results dynamically
- Styling GUI components
- Handling button click events

Why Tkinter?
- Easy to use
- No external installation required
- Suitable for lightweight desktop apps
- Cross-platform (works on Windows, Mac, Linux)

### 2️. Requests – API Communication
The requests module allows your Python program to communicate with web APIs.
In this project, it is used to fetch live currency exchange rates from the internet.

#### 📌 How to Install & Import Requests
Install (only once)

pip install requests

Import into Python

import requests

### 🧠 How Requests Works in the Project
1️. Define the API URL

      url = "https://api.exchangerate-api.com/v4/latest/USD"

2. Send GET request

    response = requests.get(url)



Usage in the project:
- Fetches real-time currency exchange rates from an online API
- Makes GET requests to URLs like:
    - https://api.exchangerate-api.com/v4/latest/USD
- Extracts currency values from returned JSON data
- Converts the amount using API rates

Why Requests?
- Simple and powerful
- Easy to integrate with REST APIs
- Automatic JSON response handling

### 3️. Datetime – Real-Time Timestamp

The datetime module in Python provides classes for working with dates, times, and timestamps. It is part of Python’s built-in standard library, so no installation is required.

In the Currency Converter project, the datetime module is used to show the exact time when the conversion was performed. This helps users know whether the conversion was done with the latest available rate.

## 📥 Importing Datetime Module
You can import the module in several ways depending on what you need.
In this project, we use:

       from datetime import datetime

Usage in the project:
- Fetch the current system date and time
- Display timestamp on the application
- Format time as:
DD-MM-YYYY HH:MM:SS

Why Datetime?
- Makes the application more informative
- Shows exact time when conversion was performed
- Provides user clarity for live rate updates

📝 Key Benefits of Using Datetime

No installation required
- Highly reliable
- Can format date/time in any style
- Works seamlessly with Tkinter labels
- Improves clarity and user experience

### 4️. Pillow (PIL) – Image Handling

PIL (Python Imaging Library), now known as Pillow, helps load and display images.

Pillow is the upgraded version of PIL (Python Imaging Library).

Tkinter alone cannot handle advanced image formats, so Pillow is required.

✔ How to Install Pillow

    pip install pillow

✔ How to Import Pillow

   from PIL import Image, ImageTk

Usage in the project:
- Load an image (PNG/JPG) into Tkinter
- Resize the image to fit the UI using:
Image.resize()
- Convert it into a Tkinter-compatible photo using ImageTk.PhotoImage
-- Display the image using a label

Why Pillow?
- Tkinter alone does not support advanced image formats
- Enhances UI aesthetics
- Allows resizing and better control over images

------------------------

## 🧠 How the Application Works (Step-by-Step)

1. User enters an amount
1. Selects the “From Currency”
1. Selects the “To Currency”
1. User clicks Convert button
1. Application sends request to API
1. Receives live exchange rates
   - Calculates conversion:
1. Converted Value = Input Amount × API Rate
1. Displays converted output
1. Shows the timestamp of the conversion

## 📚 Currencies Supported
- USD
- INR
- EUR
- GBP
- AED
- CAD
- AUD
- JPY

(we can add more anytime.)

-------------------

## 🎯 Key Highlights

- Responsive and interactive GUI
- Live exchange rate fetching
- Clean and accurate conversion results
- Safe input validation
- Attractive UI with optional images
- Beginner-friendly and extendable

-------------------------

## 🌟 Future Enhancements
- Add dark/light theme
- Add voice command conversion
- Add currency trend graphs
- Add history and save conversion logs
- Add multi-page interface
- Add more APIs for increased accuracy

-------------------

## 📌 Additional Notes

- Fully offline UI with online API-based conversion
- Beginner-friendly code structure
- Can be extended to support more currencies
- Ideal for Python/Tkinter mini-projects










