import sys
from tkinter import *
from tkinter import messagebox
import scratchattach as scratch3
import scpyhomescr as hoho
path = 'u_infobox/u_papa.txt'
path2 = 'u_infobox/u_nana.txt'


def main(u_namename):
    root = Tk()

    def nextpagggggg():
        if txt2.get() :
             u_passapaasa = txt2.get()
             mojifuse = ""
             upakazu = len(u_passapaasa)
             for i in range(upakazu):
                if i == 1 or i == 2 :
                    mojifuse = mojifuse + str(u_passapaasa[i:i])
                else:
                    mojifuse = mojifuse + "*"

             ret =messagebox.askyesno("確認","パスワードは、" + mojifuse + "でよろしいですか？")
             if ret == True :
                 try:
                     scratch3.login(username=u_namename,password=u_passapaasa)
                 except:
                     messagebox.showerror("エラー","ユーザー名またはパスワードが有効ではありません。")
                 else:
                    messagebox.showinfo("成功!","ログインできました。")
                    with open(path,mode="w") as f:
                        f.write(u_passapaasa)
                    with open(path2,mode="w") as f:
                        f.write(u_namename)
                    root.destroy()
                    hoho.main()
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

    lbl2 = Label(text="パスワード")
    lbl2.place(x=300,y=200)
    uporlbl = Label(text="(こちらはhttps://scratch.mit.edu に送信され、一切qwe0412/Kjhuioには送信されません。)")
    uporlbl.place(x=0,y=445)
    txt2 = Entry(width=20,show="*")
    txt2.place(x=280, y=240)
    root.mainloop()