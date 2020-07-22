import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
plt.style.use(['ggplot'])
import matplotlib.animation as animation
import time

ro = lambda x : round(x, ndigits=2)


def buysll():
	fig = plt.figure(figsize=(5, 5.5))
	ax1, ax2 = fig.add_subplot(211), fig.add_subplot(212)
	def Anibs(i):
		pullData = open("b1results.txt","r").read()
		pullData1 = open("s1results.txt", "r").read()
		dataArray = pullData.split('\n') 
		dataArray1 = pullData1.split('\n')
		viz_rng, net, b1, s1 = [], [], [], []
		for eachLine in dataArray:
			if len(eachLine)>1: 
				x,y = eachLine.split(',')
				viz_rng.append(float(x))
				b1.append(float(y))
		for eachLine in dataArray1:
			if len(eachLine)>1:
				j,b = eachLine.split(',')
				s1.append(float(b))

		zipped_rez = zip(b1, s1)
		net = [x+y for (x,y) in zipped_rez]
		trisk = abs(min(b1)) + abs(min(s1))
		roi = [(val/trisk)*100 for val in net]
		broi = [(val/trisk)*100 for val in b1]
		sroi = [(val/trisk)*100 for val in s1]
		for ax in [ax1, ax2]: ax.clear()
		ax1.stem(viz_rng,b1, linefmt='None', markerfmt='g+--', use_line_collection=True)
		ax1.plot(viz_rng,b1, 'C7o', alpha=0.5)
		ax1.stem(viz_rng,net, linefmt='None', markerfmt='b.', use_line_collection=True)

		ax2.stem(viz_rng,s1, linefmt='None', markerfmt='r_--', use_line_collection=True)		
		ax2.plot(viz_rng,s1, 'C6o', alpha=0.5)
		ax2.stem(viz_rng,net, linefmt='None', markerfmt='b.', use_line_collection=True)
		
		ax1.set_title("buy($)", fontsize=10)
		ax2.set_title("sell($)", fontsize=10)
		for ax in [ax2]: ax.set_xlabel('Strike Price' , fontsize=10)
	fig.suptitle("buy/sell vs. net ($)", fontsize=12)
	ani = animation.FuncAnimation(fig, Anibs, interval=1000)
	plt.show()





def bs3():
	fig = plt.figure(figsize=(10, 4))
	ax1, ax2, ax3 = fig.add_subplot(131), fig.add_subplot(132), fig.add_subplot(133)

	def Anibs3(i):
		pullData = open("b1results.txt","r").read()
		pullData1 = open("s1results.txt", "r").read()
		dataArray = pullData.split('\n') 
		dataArray1 = pullData1.split('\n')
		viz_rng, net, b1, s1 = [], [], [], []
		for eachLine in dataArray:
			if len(eachLine)>1: 
				x,y = eachLine.split(',')
				viz_rng.append(float(x))
				b1.append(float(y))
		for eachLine in dataArray1:
			if len(eachLine)>1:
				j,b = eachLine.split(',')
				s1.append(float(b))

		zipped_rez = zip(b1, s1)
		net = [x+y for (x,y) in zipped_rez]
		trisk = abs(min(b1)) + abs(min(s1))
		roi = [(val/trisk)*100 for val in net]
		broi = [(val/trisk)*100 for val in b1]
		sroi = [(val/trisk)*100 for val in s1]

		for ax in [ax1, ax2, ax3]: ax.clear()
		ax1.stem(viz_rng,b1, linefmt='green', markerfmt='g-', use_line_collection=True)
		ax2.stem(viz_rng,s1, linefmt='red', markerfmt='r-', use_line_collection=True)
		ax3.stem(viz_rng,net, linefmt='blue', markerfmt='yD--', use_line_collection=True)
		ax1.set_title('buy', fontsize=12)
		ax2.set_title('sell', fontsize=12)
		ax3.set_title('net', fontsize=12)

		for ax in [ax1, ax2, ax3]: ax.set_ylim(min(net), max(net))
		for ax in [ax1, ax2, ax3]: ax.set_xlabel('Strike Price' , fontsize=12)
		for ax in [ax1]: ax.set_ylabel('Return($)', fontsize=12)

	fig.suptitle("buy, sell, & net($)", fontsize=14)
	ani = animation.FuncAnimation(fig, Anibs3, interval=1000)
	plt.show()





def roi():
	fig = plt.figure(figsize=(5, 5.5))
	ax1, ax2 = fig.add_subplot(211), fig.add_subplot(212)
	def AniRoi(i):
		pullData = open("b1results.txt","r").read()
		pullData1 = open("s1results.txt", "r").read()
		dataArray = pullData.split('\n') 
		dataArray1 = pullData1.split('\n')
		viz_rng, net, b1, s1 = [], [], [], []
		for eachLine in dataArray:
			if len(eachLine)>1: 
				x,y = eachLine.split(',')
				viz_rng.append(float(x))
				b1.append(float(y))
		for eachLine in dataArray1:
			if len(eachLine)>1:
				j,b = eachLine.split(',')
				s1.append(float(b))

		zipped_rez = zip(b1, s1)
		net = [x+y for (x,y) in zipped_rez]
		trisk = abs(min(b1)) + abs(min(s1))
		roi = [(val/trisk)*100 for val in net]
		broi = [(val/trisk)*100 for val in b1]
		sroi = [(val/trisk)*100 for val in s1]
		for ax in [ax1, ax2]: ax.clear()
		ax1.stem(viz_rng,sroi, linefmt='None', markerfmt='r_--', use_line_collection=True)		
		ax1.stem(viz_rng,broi, linefmt='None', markerfmt='g+--', use_line_collection=True)
		ax1.plot(viz_rng,broi, 'C7o', alpha=0.5)
		ax1.plot(viz_rng,sroi, 'C6o', alpha=0.5)
		ax2.stem(viz_rng,roi, linefmt='yellow', markerfmt='bv--', use_line_collection=True)
		#ax1.set_title("buy/sell, fontsize=12)
		#ax2.set_title("Net", fontsize=12)
		ax1.set_ylabel("buy/sell ROI(%)", fontsize=12)
		ax2.set_ylabel("net ROI(%)", fontsize=12)
		#ax1.set_xticks([])
		for ax in [ax2]: ax.set_xlabel('Strike Price' , fontsize=10)
	fig.suptitle("buy/sell/net ROI(%)", fontsize=14)
	ani = animation.FuncAnimation(fig, AniRoi, interval=1000)
	plt.show()


def altROI():
	fig = plt.figure(figsize=(5, 5.5))
	ax1, ax2 = fig.add_subplot(211), fig.add_subplot(212)
	def Anialt(i):
		pullData = open("b1results.txt","r").read()
		pullData1 = open("s1results.txt", "r").read()
		dataArray = pullData.split('\n') 
		dataArray1 = pullData1.split('\n')
		viz_rng, net, b1, s1 = [], [], [], []
		for eachLine in dataArray:
			if len(eachLine)>1: 
				x,y = eachLine.split(',')
				viz_rng.append(float(x))
				b1.append(float(y))
		for eachLine in dataArray1:
			if len(eachLine)>1:
				j,b = eachLine.split(',')
				s1.append(float(b))

		zipped_rez = zip(b1, s1)
		net = [x+y for (x,y) in zipped_rez]
		trisk = abs(min(b1)) + abs(min(s1))
		roi = [(val/trisk)*100 for val in net]
		broi = [(val/trisk)*100 for val in b1]
		sroi = [(val/trisk)*100 for val in s1]
		for ax in [ax1, ax2]: ax.clear()
		ax1.stem(viz_rng,broi, linefmt='None', markerfmt='g+--', use_line_collection=True)
		ax1.stem(viz_rng,roi, linefmt='yellow', markerfmt='bv--', use_line_collection=True)
		ax1.plot(viz_rng,broi, 'C7o', alpha=0.5)

		ax2.stem(viz_rng,sroi, linefmt='None', markerfmt='r_--', use_line_collection=True)		
		ax2.plot(viz_rng,sroi, 'C6o', alpha=0.5)
		ax2.stem(viz_rng,roi, linefmt='yellow', markerfmt='bv--', use_line_collection=True)
		#for ax in [ax1, ax2]: ax.set_ylabel("ROI(%)", fontsize=12)
		#ax1.set_title("buy/sell, fontsize=12)
		#ax2.set_title("Net", fontsize=12)
		ax1.set_ylabel("buy/net ROI(%)", fontsize=12)
		ax2.set_ylabel("sell/net ROI(%)", fontsize=12)
		#ax1.set_xticks([])
		for ax in [ax2]: ax.set_xlabel('Strike Price' , fontsize=10)
	fig.suptitle("buy/net sell/net", fontsize=14)
	ani = animation.FuncAnimation(fig, Anialt, interval=1000)
	plt.show()





def overview():
	fig = plt.figure(figsize=(9, 5))
	ax1, ax2 = fig.add_subplot(221), fig.add_subplot(222)
	ax3, ax4 = fig.add_subplot(223), fig.add_subplot(224)
	def AniOverview(i):
		pullData = open("b1results.txt","r").read()
		pullData1 = open("s1results.txt", "r").read()
		dataArray = pullData.split('\n') 
		dataArray1 = pullData1.split('\n')
		viz_rng, net, b1, s1 = [], [], [], []
		for eachLine in dataArray:
			if len(eachLine)>1: 
				x,y = eachLine.split(',')
				viz_rng.append(float(x))
				b1.append(float(y))
		for eachLine in dataArray1:
			if len(eachLine)>1:
				j,b = eachLine.split(',')
				s1.append(float(b))

		zipped_rez = zip(b1, s1)
		net = [x+y for (x,y) in zipped_rez]
		trisk = abs(min(b1)) + abs(min(s1))
		roi = [(val/trisk)*100 for val in net]
		broi = [(val/trisk)*100 for val in b1]
		sroi = [(val/trisk)*100 for val in s1]
		b1r, s1r, b1w, s1w = ro(abs(min(b1))), ro(abs(min(s1))), ro(max(b1)), ro(max(s1))
		ww, wl, lw = ro(b1w+s1w), ro(b1w-s1r), ro(s1w-b1r)
		wwr, wlr, lwr = ro((ww/trisk)*100), ro((wl/trisk)*100), ro((lw/trisk)*100)
		for ax in [ax1, ax2, ax3, ax4]: ax.clear()
		ax1.barh('sell\nrisk\n $' + str(s1r), s1r)		
		ax1.barh('buy\nrisk\n $' + str(b1r), b1r)
		ax2.barh('sell\nreturn\n $' + str(s1w), s1w)
		ax2.barh('buy\nreturn\n $' + str(b1w), b1w)
		ax3.barh('loss-win\n $' + str(lw), lw)
		ax3.barh('win-loss\n $' + str(wl), wl)
		ax3.barh('win-win\n $' + str(ww), ww)
		ax4.barh('loss-win\n %' + str(lwr), lwr)
		ax4.barh('win-loss\n %' + str(wlr), wlr)
		ax4.barh('win-win\n %' + str(wwr), wwr)
		ax1.set_title("Risk($)", fontsize=12)
		ax2.set_title("Return($)", fontsize=12)
		ax3.set_title("Outcomes Net($)", fontsize=12)
		ax4.set_title("Outcomes ROI(%)", fontsize=12)
		for ax in [ax1, ax2]: ax.set_xticks([])
		#for ax in [ax5, ax6]: ax.set_xlabel('Return', fontsize=14)

	fig.suptitle("Derivative Position", fontsize=16)
	ani = animation.FuncAnimation(fig, AniOverview, interval=1000)
	plt.show()


#overview()
#buysell()
#roi()