import tkinter as tk

win = tk.Tk()

win.geometry('240x260+100+200')
win['bg'] = '#F5DEB3'
win.title('Калькулятор')

calc = tk.Entry(win)
calc.grid(column=0, row=0, columnspan=2)

tk.Button(text='1').grid(row=1, column=0)
tk.Button(text='2').grid(row=1, column=1)
tk.Button(text='3').grid(row=1, column=2)
tk.Button(text='4').grid(row=2, column=0)
tk.Button(text='5').grid(row=2, column=1)
tk.Button(text='6').grid(row=2, column=2)
tk.Button(text='7').grid(row=3, column=0)
tk.Button(text='8').grid(row=3, column=1)
tk.Button(text='9').grid(row=3, column=2)
tk.Button(text='0').grid(row=4, column=0)


win.mainloop()

