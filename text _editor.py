from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
root=Tk()
root.title('untitled')
root.geometry('650x500')
text_scroll=Scrollbar(root)
text_scroll.pack(side=RIGHT,fill=Y)
hor_scroll=Scrollbar(root,orient='horizontal')
hor_scroll.pack(side=BOTTOM,fill=X)
my_text=Text(root,width=95,height=25,font=("helivetica",16),selectbackground="gray",selectforeground="black",undo=True,yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=hor_scroll.set)
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)
my_text.pack()
def browse(e):
    #To open the file
    filetypes=(('All files','*.*'),
               ('text files','*.txt')
    )
    global file_name
    file_name=fd.askopenfilename(initialdir='/',
        filetypes=filetypes)
def help():
    messagebox.showinfo("Any queries!","\n Mail me through arsangavi2002@gmail.com\nContact me:9442498962")
def about():
    #info about this project
    messagebox.showinfo("about us","\nWelcome to the text editor.here u can type anything and you can save it it works like a note pad ")
def new(e):
    #to create a new window
    root=Tk()
    root.geometry('650x500')
    root.title('new file')
    text_scroll = Scrollbar(root)
    text_scroll.pack(side=RIGHT, fill=Y)
    my_text = Text(root, width=95, height=25, font=("helivetica", 16), selectbackground="gray",
                   selectforeground="black", undo=True)
    my_text.pack()

    root.mainloop()
def save(e):
    #to save a file
    global file
    filetypes = (('All files', '*.*'),
                 ('text files', '*.txt')
                 )
    file= fd.asksaveasfile(filetypes=filetypes,defaultextension=filetypes)
def cut(e):
    #to cut text
    global selected
    if my_text.selection_get():
        selected=my_text.selection_get()
        my_text.delete("selected.first","selected.last")
def copy(e):
    #to copy text
    global selected
    if my_text.selection_get():
        selected = my_text.selection_get()
def paste(e):
    #to paste a text
    if selected:
        position=my_text.index(INSERT)
        my_text.insert(position,selected)
menu_bar=Menu(root)
root.config(menu=menu_bar)
sub_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='File',menu=sub_menu)
sub_menu.add_cascade(label='New  ctrl+N',command=lambda :new(0))
sub_menu.add_cascade(label='Open  ctrl+O',command=lambda :browse(0))
sub_menu.add_cascade(label='Save  ctrl+S',command=lambda :save(0))

sub_menu.add_separator()
sub_menu.add_cascade(label='Exit   ctrl+E',command=root.destroy)
sub_menu_1=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='Edit',menu=sub_menu_1)
sub_menu_1.add_cascade(label='Cut   ctrl+X',command=lambda :cut(0))
sub_menu_1.add_cascade(label='Copy  ctrl+C',command=lambda :copy(0))
sub_menu_1.add_cascade(label='Paste  ctrl+V',command=lambda :paste(0))
sub_menu_1.add_separator()
sub_menu_1.add_cascade(label='Undo  ctrl+Z',command=my_text.edit_undo)
sub_menu_1.add_cascade(label='Redo  ctrl+Y',command=my_text.edit_redo)
sub_menu1=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='About',menu=sub_menu1)
sub_menu1.add_cascade(label='about me',command=about)
menu_bar.add_cascade(label='Help',command=help)

root.mainloop()