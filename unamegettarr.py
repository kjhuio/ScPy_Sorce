import sys
import upassgettorpagepage
from tkinter import *
from tkinter import messagebox

def main():
    root = Tk()

    def nextpagggggg():
        u_nnammennamme = txt.get()
        if txt.get() :
             ret =messagebox.askyesno("確認","ユーザー名は、" + txt.get() + "でよろしいですか？")
             if ret == True :
                 root.destroy()
                 upassgettorpagepage.main(u_nnammennamme)
                 sys.exit()
        else :
            messagebox.showerror("エラー","ユーザー名が入力されていません。")
    w = 640 # 横の長さ
    h=480 # 縦の長さ
    x=200 # 座標軸x
    y=300 # 座標軸y

    root.geometry('%dx%d+%d+%d' % (w,h, x, y))

    button = Button(root, text="次へ、",command=nextpagggggg)
    button.place(x=550,y=400)
    root.geometry("640x480")

    lbl = Label(text="ユーザー名")
    lbl.place(x=300,y=200)
    txt = Entry(width=20)
    txt.place(x=280, y=240)

    root.mainloop()