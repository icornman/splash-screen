from tkinter import *

# Splash Screen
def center_window(w=300, h=200):
    ws = splash_root.winfo_screenwidth()
    hs = splash_root.winfo_screenheight()

    x = ((ws/2) - (w/2))
    y = ((hs/2) - (h/2))

    splash_root.geometry('%dx%d+%d+%d' % (w, h, x, y))

splash_root = Tk()
splash_root.title("Splash Screen")

center_window(320, 200)

splash_root.overrideredirect(True)

splash_label = Label(splash_root, text="Splash Screen!", font=("Helvetica", 18))
splash_label.pack(pady=20)

# Main Screen
def main_window():
	splash_root.destroy()
	
	root = Tk()
	root.title('App Name')
	root.geometry("500x550")

	main_label = Label(root, text="Main Screen", font=("Helvetica", 18))
	main_label.pack(pady=20)

splash_root.after(5000, main_window)

mainloop()
