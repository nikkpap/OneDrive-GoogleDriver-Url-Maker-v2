"""
This App is an Exersice to learn Python it converts the urls from Onedrive Embended and from Gdrive share...
to direct download links...
by nikkpap @ 2021 ALU DEV TEAM
"""
from tkinter import *
from tkinter import messagebox
import sys
import re


#Right click context menu for all Tk Entry and Text widgets
def rClicker(e):


    try:
        def rClick_Copy(e, apnd=0):
            e.widget.event_generate("<Control-c>")

        def rClick_Cut(e):
            e.widget.event_generate("<Control-x>")

        def rClick_Paste(e):
            e.widget.event_generate("<Control-v>")

        e.widget.focus()

        nclst=[
               (" Cut", lambda e=e: rClick_Cut(e)),
               (" Copy", lambda e=e: rClick_Copy(e)),
               (" Paste", lambda e=e: rClick_Paste(e)),
               ]

        rmenu = Menu(None, tearoff=0, takefocus=0)

        for (txt, cmd) in nclst:
            rmenu.add_command(label=txt, command=cmd)

        rmenu.tk_popup(e.x_root+40, e.y_root+10,entry="0")

    except TclError:
        print (" - rClick menu, something wrong")
        pass

    return "break"

def rClickbinder(r):

    try:
        for b in [ "Text", "Entry", "Listbox", "Label"]: #
            r.bind_class(b, sequence="<Button-3>",
                         func=rClicker, add="")
    except TclError:
        print (" - rClickbinder, something wrong")
        pass

#Convert Onedrive Url
def conv_onedrive():
    try:
        strip_html= re.search("src=\"(.*)\" width", textBox_oem.get() )
        conv_onedrive_html= strip_html[1].replace("embed","download")
        
        textBoxEntry_conv.set(str(conv_onedrive_html))
        
    except: 
        messagebox.showwarning("OneDrive...", "Please check your input")

#Convert GoogleDrive Url
def conv_google():
    try:
        get_html = textBox_oem.get()
        pattern_string = "/file/.*/(.*)/view?"
        sub_string = re.search(pattern_string, get_html).group(1)
        conv_google_html = "https://drive.google.com/uc?export=download&id=" + sub_string

        textBoxEntry_conv.set(str(conv_google_html))

    except: 
        messagebox.showwarning("GoogleDrive...", "Please check your input")

#About Message     
def about():
    lines = ["        This App is an Exersice to learn Python it converts the urls from Onedrive Embended and from Gdrive share... just choose the correct converter and paste the url and press the button OneDrive/Gdrive", "\n                             by nikkpap", "\n           nikkpap@gmail.com | ALU DEV TEAM"]
    messagebox.showinfo("About","\n".join(lines))

#Kill Window
def close_window0(): 
    window0.destroy()

#Windows Parameters 
window0= Tk()
window0.title("Direct Download Url Maker v2.2")
window0.geometry("440x220")
window0.resizable(False, False)

#Buttons
btnConvOnedrive=Button(window0, height=1, width=10, text="OneDrive", command= lambda: conv_onedrive()).place( relx=0.40, rely=0.70, anchor="nw") 
btnAbout=Button(window0, height=1, width=10, text="About", command= lambda: about()).place( relx=0.60, rely=0.70, anchor="nw") 
btnExit=Button(window0, height=1, width=10, text="Exit", command= lambda: close_window0()).place( relx=0.80, rely=0.70, anchor="nw") 

#Var declaring
textBoxEntry_oem= StringVar()
textBoxEntry_conv= StringVar()
var_toggle= IntVar()

#First Texbox Parameters
textBox_oem= Entry(window0, width=50, textvariable= textBoxEntry_oem)
textBox_oem.place(relx=0.25, rely=0.42, anchor="w")
textBox_oem.bind("<Button-3>",rClicker, add="")

#Second Texbox Parameters
textBox_conv= Entry(window0, width=50, textvariable= textBoxEntry_conv)
textBox_conv.place(relx=0.25, rely=0.55, anchor="w")
textBox_conv.bind("<Button-3>",rClicker, add="")

#Label Parameters
lbl_oem = Label(window0, text="Oem URL: ").place(relx=0.22, rely=0.42, anchor="e")
lbl_conv = Label(window0, text="Converted URL: ").place(relx=0.22, rely=0.53, anchor="e")

#RadioButtons
choices = [("OneDrive", 1), ("GoogleDrive", 2)]
var_toggle.set(1)

def ShowChoice():
        def mode_Google():
          textBox_oem.delete("0", END)
          textBox_conv.delete("0", END)

        def mode_Onedrive():
          textBox_oem.delete("0", END)
          textBox_conv.delete("0", END)

        if var_toggle.get() == 1:
            mode_Onedrive()
            btnConvOnedrive=Button(window0, height=1, width=10, text="OneDrive", command= lambda: conv_onedrive()).place( relx=0.40, rely=0.70, anchor="nw")
        else:  
            mode_Google()
            btnConvGoogle=Button(window0, height=1, width=10, text="GoogleDrive", command= lambda: conv_google()).place( relx=0.40, rely=0.70, anchor="nw")

radlb= Label(window0, text="Choose Convertor :", justify = LEFT).pack( padx = 20 )

for choices, val in choices:
    rad= Radiobutton(window0, text=choices, padx = 0.55, pady = 0.10, variable=var_toggle, command=ShowChoice, value=val).pack(anchor="sw")

mainloop()