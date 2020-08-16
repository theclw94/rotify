import tkinter as tk
import string

def rotify():
    dk = {}
    ls= []
    alphabet = string.ascii_lowercase
    pun = string.punctuation
    nums = string.digits
    for cnt,ltr in enumerate(alphabet,1):
        if ltr not in dk:
            dk[ltr] = cnt
    for count,punct in enumerate(pun,-33):
        if punct not in dk:
            dk[punct] = count
    for cnt_num,digit in enumerate(nums,-50):
        if digit not in dk:
            dk[digit] = cnt_num
    dk[" "] = -1
    #print(dk)

    txt = ent_txt.get()
    text = txt.lower()
    for chr in text:
        n_ltr = dk.get(chr)
        if n_ltr + 13 < 27 and n_ltr > 0:
            cod = n_ltr + 13
        elif n_ltr + 13 >= 27:
            cod = n_ltr - 13
        else:
            cod = n_ltr
        for key,val in dk.items():
            if val == cod:
                ls.append(key)

    rot = "".join(ls)
    lbl_rot["text"] = rot
    #return rot

win = tk.Tk()
win.title("Rotifier")

frm1 = tk.Frame(master=win)
frm2 = tk.Frame(master=win)

lbl_txt = tk.Label(master=frm1, text="Your text here: ")
ent_txt = tk.Entry(master=frm1, w=50)
btn_rot = tk.Button(master=frm1, text="Rotify the text!", command=rotify)
lbl_rot = tk.Label(master=frm1)

lbl_txt.grid(row=0, column=0, sticky="e")
ent_txt.grid(row=0, column=1, padx=10, sticky="w")
btn_rot.grid(row=1, column=0, pady=10, sticky="e")
lbl_rot.grid(row=1, column=1, padx=10, sticky="w")
frm1.grid(row=0, column=0, padx=10)

win.mainloop()
