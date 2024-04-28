import tkinter as tk
import unamegettarr

def main():
    #rootウィンドウを作成
    root = tk.Tk()

    w = 640 # 横の長さ
    h = 480 # 縦の長さ
    x = 200 # 座標軸x
    y = 300 # 座標軸y

    root.geometry('%dx%d+%d+%d' % (w,h, x, y))

    def nextpage():
        root.destroy()
        unamegettarr.main()

    button = tk.Button(root, text="次へ、",command=nextpage)
    button.place(x=550,y=400)

    #メインループ
    root.mainloop()
