"""
QR Code Generator
Author: Charlie Arua Ikosi
Date created: 17 May 2024
Date modified: 17 July 2024
WorkGroup: Geospatial And Digital Solutions
Organisation: Pattle Delamore Partners
Version: 1.1
"""

#import segno
import qrcode
import tkinter as tk
from tkinter import StringVar
from tkinter import Tk, filedialog
from tkinter import messagebox
import pandas as pd
from tkinter import *
import os
import sys


def sensor_id():
    """Function that takes the text input of sensor ID from the GUI"""
    sensor_id_input = sensor_id_text.get()
    return sensor_id_input

def export_name():
    """Function that takes the text input for the export name from the GUI and adds .png file extension"""    
    sensor_export_name = export_text.get()
    file_extension = '.png'
    return sensor_export_name+file_extension

       
def clear_inputs():
    "Function that clears GUI input after button for generate QR code is clicked"
    sensor_id_entry.delete(0, tk.END)
    export_entry.delete(0, tk.END)
    
def clear_directory():
    "Function that clears directory field input after button for directory is clicked"
    filepath_entry.delete(0,tk.END)


# Prompt - Save path window   
def path_to_save():
    """Function that creates dialogue popup window to select file path to save
    file outputs on system"""
    root = Tk() # pointing root to Tk() to use it as Tk() in program.
    root.withdraw() # Hides small tkinter window.
    root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
    clear_directory()
    open_file = filedialog.askdirectory() # Returns opened path as str
    if not open_file:
        print("Directory selection cancelled")
        open_file = ""
    else:
        print(f"Selected directory: {open_file}")
    return filepath_entry.insert(0,f'{open_file}')

def generateqrcode():
    """Function that generates the QR Code and clears the input fields in the GUI"""
    if len(sensor_id_text.get()) or len(export_text.get()) != 0:
        file_directory = path_to_save()
        qrcode = segno.make_qr(sensor_id())
        qrcode.save(export_name(),scale=10)
        clear_inputs()
        messagebox.showinfo("QR Code","QR Code Generated!")
    else:
        messagebox.showinfo("Input Error!","Input fields must not be empty")
    

def close_window():
    """Function that closes the program window"""
    window.destroy()


# main window settings
window = tk.Tk() 
window.title("QR Code Generator")
window.iconbitmap('C:/Users/Charlie.Ikosi/OneDrive - PDP/Documents/QR Code/pdp_logo2.ico')
window.geometry("500x200") # sets the dimensions of the GUI window
window.config(bg='#0f4b6e')
window.resizable(0,0) # fixes window frame to set geometry

# Input-Unique Sensor ID / Identifier
sensor_id_text = StringVar()
sensor_id_label = tk.Label(master=window, text="Unique ID:", 
                          font=("Calibri", 11, "bold"), padx=20, pady=10,
                          bg='#0f4b6e')
sensor_id_label.grid(row=0, column=0)
sensor_id_entry = tk.Entry(master=window, width = 40, textvariable=sensor_id_text)
sensor_id_entry.grid(row=0, column=1)


# Input-QR Code Export Name
export_text = StringVar()
export_label = tk.Label(master=window, text="Image output name:", 
                          font=("Calibri", 11, "bold"), padx=20, pady=10,
                          bg='#0f4b6e')
export_label.grid(row=1, column=0)
export_entry = tk.Entry(master=window, width = 40, textvariable=export_text)
export_entry.grid(row=1, column=1)


# Input-file path
filepath_text = StringVar()
filepath_label = tk.Label(master=window, text="Directory:",
                         font=("Calibri", 11, "bold"), padx=20,pady=10)
#filepath_label.grid(row=2,column=0)
filepath_entry = tk.Entry(master=window, width = 40, textvariable=filepath_text)
filepath_entry.grid(row=2, column=1)


# Button 1 - Generate QR Code
add_button = tk.Button(master=window, text="Generate QR Code", width=36, command=generateqrcode)
add_button.grid(row=10, column=1)

# Button 2 - Exit
add_button = tk.Button(master=window, text="Close", width=36, command=close_window)
add_button.grid(row=11, column=1)

# Button 3 - Directory
add_button = tk.Button(master=window, text="Directory", width=10, command=path_to_save)
add_button.grid(row=2, column=0)


# run the program
window.mainloop()
