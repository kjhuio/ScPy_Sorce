path = 'u_infobox/u_nana.txt'
path2 = 'u_infobox/u_papa.txt'
from scpmain import main
import sys
import scpyhomescr as hhh
import scratchattach as scratch3
import tkinter as tk
import time

startscr = tk.Tk()

def passkey_remove():
    import upassgettorpagepage
    upassgettorpagepage.main(s)

startscr_lab = tk.Label(startscr,text="ScPyをスタートしています。\nStarting ScPy")
startscr_lab.place(x=1,y=10)

time.sleep(5)

try :
    with open(path) as f:
        s = f.read()
    with open(path2) as f2:
        s2 = f2.read()
except:
    print("none pass or username")
else:
    bata_ = tk.Button(startscr,text="パスワードを変更しました。",command=passkey_remove)
    bata_.place(x=1,y=20)
try :
    with open(path) as f:
        s = f.read()
        print(s)
    with open(path2) as f:
        s = f.read()
        print(s)
except :
    with open(path,mode="w") as f:
        print("Starting ScPy...\n(session1)")
    with open(path2,mode="w") as f:
        print("starting ScPy... \n (session2)")
    main()
else:
    with open(path) as namae:
        nana = namae.read()
    with open(path2) as namae2:
        passwa_do = namae2.read()
    try:
        scratch3.login(password=passwa_do,username=nana)
    except:
        from tkinter import messagebox
        messagebox.showerror("エラー","ユーザー名またはパスワードが間違っています。\n 最初からやり直してください。")
        import unamegettarr
        startscr.destroy()
        unamegettarr.main()
        sys.exit()
    else:
        startscr.destroy()
        hhh.main()
        sys.exit()