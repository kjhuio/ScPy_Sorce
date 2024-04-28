import sys
from tkinter import *
from tkinter import messagebox
import scratchattach as scratch3
path = 'u_infobox/u_nana.txt'
path2 = 'u_infobox/u_papa.txt'

def main():
    root = Tk()

    def projectidestart():
        if txt.get() :
             ret =messagebox.askyesno("確認","IDは、" + txt.get() + "でよろしいですか？")
             if ret :
                 try :
                     mmtxter = txt.get()
                     int(mmtxter)
                 except :
                     messagebox.showerror("エラー", "入力された文字は数字ではありません。\n 数字が全角になっているか、または間違えて文を入れていないかを確認してください。")
                     txt.delete(0,END)
                 else:
                     protab = Tk()
                     def protabend():
                         endpagprot = messagebox.askyesno("確認","このウィンドウを閉じますか？")
                         if endpagprot:
                            protab.destroy()
                     def connect_cloudhenn():
                         with open(path) as f:
                             with open(path2) as f2:
                                 u_naname = f.read()
                                 u_papasa = f2.read()
                                 try :
                                     session = scratch3.login(username=u_naname, password=u_papasa)
                                 except :
                                     messagebox.showerror("エラー","ログインに失敗しました。")
                                 else:
                                     pada = txt.get()
                                     pada = int(pada)
                                     try:
                                        connection = session.connect_cloud(project_id=pada)
                                     except:
                                         messagebox.showerror("エラー","クラウド変数への接続に失敗しました。")
                                     else:
                                         chennana = protabtxt2.get()
                                         cvaru = int(protabtxt.get())
                                         connection.set_var(chennana,cvaru )
                                         messagebox.showinfo("成功!","クラウド変数のセットに成功しました。")
                     protab.geometry('%dx%d+%d+%d' % (subw,subh,x,y))
                     endbtnpta = Button(protab, text="終了", command=protabend)
                     endbtnpta.place(x=220,y=250)
                     protablbl1 = Label(protab, text="変数値変更")
                     protablbl1.place(x=10,y=20)
                     protabtxt = Entry(protab,width=20)
                     protabtxt.place(x=30,y=40)
                     protablblh = Label(protab, text="変数名")
                     protablblh.place(x=10,y=60)
                     protabtxt2 = Entry(protab,width=20)
                     protabtxt2.place(x=60,y=60)
                     protabbutton = Button(protab, text="実行",command=connect_cloudhenn)
                     protabbutton.place(x=0, y=80)
                     protablbl2 = Label(protab,text="コメント(この動作は推奨されていません)")
                     protablbl2.place(x=10,y=100)
        else :
            messagebox.showerror("エラー","IDが入力されていません。")
    w = 640 # 横の長さ
    h=480 # 縦の長さ
    x=200 # 座標軸x
    y=300 # 座標軸y

    subw = 250
    subh = 300

    root.geometry('%dx%d+%d+%d' % (w,h, x, y))

    button = Button(root, text="実行",command=projectidestart)
    button.place(x=550,y=25)
    lbl = Label(text="プロジェクトID")
    lbl.place(x=240,y=15)
    txt = Entry(width=20)
    txt.place(x=280, y=40)

    root.mainloop()