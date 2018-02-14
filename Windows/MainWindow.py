from tkinter import *
from nilearn import plotting
from PIL import Image, ImageTk

#Create & Configure root
root = Tk()
root.geometry("800x600")

#Load file
file_path = 'Data-I/LS4025 WM/unprocessed/3T/tfMRI_WM_LR/LS4025_3T_tfMRI_WM_LR_SBRef_gdc.nii.gz'
plotting.plot_anat(file_path, output_file='Conversions/test_conversions.png')
new_file_path = 'Conversions/test_conversions.png'

#Replace images with embedded matplotlibs for easier image manipulation
left_image = Image.open('Conversions/Front View.png')
left_photo = ImageTk.PhotoImage(left_image)

center_image = Image.open('Conversions/Side View.png')
center_photo = ImageTk.PhotoImage(center_image)

right_image = Image.open('Conversions/Top View.png')
right_photo = ImageTk.PhotoImage(right_image)

#Create & Configure frame
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.rowconfigure(0, weight=1)

#Create the Images
Label1 = Label(frame, image=left_photo)
Label1.grid(column=0, row=0, sticky=N+S+E+W)

Label2 = Label(frame, image=center_photo)
Label2.grid(column=5, row=0, sticky=N+S+E+W)

Label3 = Label(frame, image=right_photo)
Label3.grid(column=10, row=0, sticky=N+S+E+W)

#Create Horizantal Scrollbars
Scrollbar1 = Scrollbar(frame)
Scrollbar1.grid(column=0, row=1, sticky=N+S+E+W)

Scrollbar2 = Scrollbar(frame)
Scrollbar2.grid(column=5, row=1, sticky=N+S+E+W)

Scrollbar3 = Scrollbar(frame)
Scrollbar3.grid(column=10, row=1, sticky=N+S+E+W)

ReportTextField = Label(frame, text="This is a test")
ReportTextField.grid(column=0, row=3)

root.mainloop()