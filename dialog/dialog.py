import tkinter.messagebox as mb 
import tkinter.filedialog as fd

ans = mb.askyesno("question", "are you satisfied?")

if ans == True:
    mb.showinfo("agree", "moi aussi")
else:
    mb.showinfo("are you kidding?", "you suck")

path = fd.askopenfilename(
        title  = "specify files you want to delete",
        filetypes = [("PDF",".pdf")])
print(path)
        
