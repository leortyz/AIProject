from tkinter import Tk, Frame, Label, PhotoImage, Button
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from predecir import predict
filename=''
tipo=''
pos1=200
def ask():
    label3=Label(root,text=" "*40)
    label3.place(x=pos1,y=40)
    label5=Label(root,text=" "*40)
    label5.place(x=pos1,y=80)
    filename = askopenfilename() 
    f=filename.split('/')
    label3=Label(root,text=f[-1])
    label3.place(x=pos1,y=40)
    tipo=predict(filename)
    label5=Label(root,text=tipo)
    label5.place(x=pos1,y=80)
    im=Image.open(filename)
    im = im.resize((250, 250), Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(im)
    photoimg=Label(root,image=photo)
    photoimg.image=photo
    photoimg.place(x=175,y=150)

root=Tk()
root.title("Clasificador de Desechos")
root.resizable(True,True)
root.geometry("650x500")
width=650
height=400
Button(root, text="Seleccionar imagen", command=ask).place(x=500,y=40)
label1=Label(root,text='Clasificador de Desechos')
label1.place(x=325,y=10)
label2=Label(root,text='Imagen seleccionada:')
label2.place(x=40,y=40)
label4=Label(root,text="La imagen corresponde a:")
label4.place(x=40,y=80)

root.mainloop()
