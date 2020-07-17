import sys
from tkinter import *
import tkinter as tk
import numpy as np
import os

#range of values for the visual
#viz_rng = np.arange(1.5,1.7,.02) #option range EUR/USD
viz_rng = np.arange(109,110,.05) #option range USD/JPY

class MyWindow:
	def __init__(self, win):
		#create labels 'lbl' and entry fields 't' for inputs 1-6

		self.lbl1=Label(win, text='Size', bg='black', fg='white') #lbl1
		self.lbl2=Label(win, text='Price', bg='black', fg='white')
		self.lbl3=Label(win, text='Strike', bg='black', fg='white')
		self.lbl4=Label(win, text='Size', bg='black', fg='white')
		self.lbl5=Label(win, text='Price', bg='black', fg='white')
		self.lbl6=Label(win, text='Strike', bg='black', fg='white')

		self.t1=Entry(bd=1, bg='black', fg='white')#t1
		self.t2=Entry(bd=1, bg='black', fg='white')
		self.t3=Entry(bd=1, bg='black', fg='white')
		self.t4=Entry(bd=1, bg='black', fg='white')
		self.t5=Entry(bd=1, bg='black', fg='white')
		self.t6=Entry(bd=1, bg='black', fg='white')

		#simplify spacing adjustments with spacing variables.
		t1x, label1x, label1y, label4y = 335, 295, 95, 325
		
		#spacing for 6 lbl and 6 t.
		self.lbl1.place(x=label1x, y=label1y)
		self.lbl2.place(x=label1x, y=label1y+25)
		self.lbl3.place(x=label1x, y=label1y+50)
		self.t1.place(x=t1x, y=label1y)
		self.t2.place(x=t1x, y=label1y+25)
		self.t3.place(x=t1x, y=label1y+50)
		self.lbl4.place(x=label1x, y=label4y)
		self.lbl5.place(x=label1x, y=label4y+25)
		self.lbl6.place(x=label1x, y=label4y+50)
		self.t4.place(x=t1x, y=label4y)
		self.t5.place(x=t1x, y=label4y+25)
		self.t6.place(x=t1x, y=label4y+50)

		#update buttons
		self.btn1=Button(win, text='Update\nBuy-Side') #create button, add text
		self.b1=Button(win, text='Update\nBuy-Side', width='6', height='4', fg='green', bg='green', command=self.b1rez) #connect w/ command / format
		self.b1.place(x=240, y=97.5) #spacing for buttons

		self.btn2=Button(win, text='Update\nSell-Side')
		self.b2=Button(win, text='Update\nSell-Side', width='6', height='4',  fg='green', bg='green', command=self.s1rez)
		self.b2.place(x=240, y=325)



		#visual buttons
		bx, by = 20, 25

		self.btn3=Button(win, text='BuySell')
		self.b3=Button(win, text='BuySell', width='9', height='3', fg='blue', bg='blue', command=self.buysell)
		self.b3.place(x=bx, y=by)

		self.btn4=Button(win, text='ROI')
		self.b4=Button(win, text='ROI', width='9', height='3', fg='blue', bg='blue', command=self.roi)
		self.b4.place(x=bx, y=by+125)

		self.btn5=Button(win, text='alt-ROI')
		self.b5=Button(win, text='alt-ROI', width='9', height='3', fg='blue', bg='blue', command=self.altROI)
		self.b5.place(x=bx, y=by+250)

		self.btn6=Button(win, text='Overview')
		self.b6=Button(win, text='Overview', width='9', height='3', fg='blue', bg='blue', command=self.overview)
		self.b6.place(x=bx, y=by+375)

		#quit button
		self.btn7=Button(win, text='Quit')
		self.b7=Button(win, text='Quit', width='9', height='3', fg='red', bg='red', command=quit)
		self.b7.place(x=650, y=by+375)

	def buysell(self):
		from charts import bs3
		bs3()
	def roi(self):
		from charts import roi
		roi()
	def overview(self):
		from charts import overview
		overview()
	def altROI(self):
		from charts import altROI
		altROI()

	def quit(self):
		quit()

	def b1rez(self):
		b1sz, b1p, b1stk=float(self.t1.get()), float(self.t2.get()), float(self.t3.get())
		b1r=float(b1p * b1sz)
		b1w=float(100*b1sz + (-b1r))
		b1_rez = [b1w if n > abs(b1stk) else -b1r for n in viz_rng]
		with open('b1results.txt', 'w') as f:
			for n in range(0,len(viz_rng)): print(viz_rng[n], ',', b1_rez[n], file=f)
	
	def s1rez(self):
		s1sz, s1p, s1stk=float(self.t4.get()), float(self.t5.get()), float(self.t6.get())
		s1r= float((100-s1p)*s1sz)
		s1w= float(s1p*(s1sz))
		s1_rez = [s1w if n < abs(s1stk) else -s1r for n in viz_rng]
		with open('s1results.txt', 'w') as f:
			for n in range(0,len(viz_rng)): print(viz_rng[n], ',', s1_rez[n], file=f)

#GUI
window=Tk() #initialize tcl/tk interpreter
window.title('Real-Time Derivative Model v1.6.2')
window.geometry("750x500-1000-1000")
try:	
	logo=tk.PhotoImage(file="sms_logo.png") 
	w1=tk.Label(window, image=logo).pack()
except: pass #open GUI w/out A logo.png

mywin=MyWindow(window) #link MyWindow class and tk interpretter

window.mainloop() #execute infinite loop


