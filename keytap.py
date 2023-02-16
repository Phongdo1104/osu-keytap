from tkinter import *
# from system_hotkey import SystemHotkey
from pynput import keyboard


main = Tk()
main.title("keytap")
main.geometry("400x170")

main_w = 400
main_h = 170

postiion_main_x = (main.winfo_screenwidth() - (main.winfo_screenwidth()//5)) - (main_w//2)
position_main_y = (main.winfo_screenheight() - (main.winfo_screenheight()//5)) - (main_h//2)

main.geometry(f"{main_w}x{main_h}+{postiion_main_x}+{position_main_y}")

main.resizable(0, 0)
# main.wm_attributes("-topmost", 1)

main.config(bg="#303841")

# Frame
frame = Frame(main, width=370, height=100, bg="#03ff01")
frame.place(x=15, y=15)

frameIn = Frame(frame, width=400, height=100, bg="#03ff01")
frameIn.place(x=10, y=10)

countX = 0
countY = 0
holdX = False
holdY = False

Key1 = "v"
Key2 = "b"

# Button


def changeColor(event):
	global countX, countY, holdX, holdY

	try:
		if (event.char == Key1):
			if (holdX == False):
				holdX = True
				ButtonX.config(bg="#FFFFFF")
				countX = countX + 1
				CountingText.config(text=countX)
		elif (event.char == Key2):
			if (holdY == False):
				holdY = True
				ButtonY.config(bg="#FFFFFF")
				countY = countY + 1
				CountingText2.config(text=countY)
	except AttributeError:
		return

def changeColorDefault(event):
	global holdX, holdY

	try:
		if (event.char == Key1):
			holdX = False
			ButtonX.config(bg = "#303841")
		elif (event.char == Key2):
			holdY = False
			ButtonY.config(bg = "#303841")
	except AttributeError:
		return

def ChangeKey():
	def SaveChange():
		global Key1, Key2, countX, countY
		Key1 = KeyOneEntry.get()
		Key2 = KeyTwoEntry.get()

		KeyOneCurrent.config(text = "Key 1: %s" %(Key1))
		KeyTwoCurrent.config(text = "Key 2: %s" %(Key2))

		countX = 0
		CountingText.config(text=countX)
		countY = 0
		CountingText2.config(text=countY)

		customMenu.destroy()

	customMenu = Toplevel()

	customMenu_w = 200
	customMenu_h = 200

	postiion_customMenu_x = (customMenu.winfo_screenwidth()//2) - (customMenu_w//2)
	position_customMenu_y = (customMenu.winfo_screenheight()//2) - (customMenu_h//2)

	customMenu.geometry(f"{customMenu_w}x{customMenu_h}+{postiion_customMenu_x}+{position_customMenu_y}")

	# customMenu.geometry("200x200")
	customMenu.resizable(0, 0)
	customMenu.config(bg="#303841")

	CustomKeyLabel = Label(customMenu, text = "Custom Key", font = ("Consolas", 15, "bold"), bg="#303841", fg="#FFFFFF")
	CustomKeyLabel.place(x = 15, y = 20)

	# Key 1
	KeyOneLabel = Label(customMenu, text = "Key 1", font = ("Consolas", 15), bg="#303841", fg="#FFFFFF")
	KeyOneLabel.place(x = 20, y = 60)

	KeyOneEntry = Entry(customMenu, width = 5, font = ("Consolas", 15))
	KeyOneEntry.place(x = 100, y = 60)

	# Key 2
	KeyTwoLabel = Label(customMenu, text = "Key 2", font = ("Consolas", 15), bg="#303841", fg="#FFFFFF")
	KeyTwoLabel.place(x = 20, y = 95)

	KeyTwoEntry = Entry(customMenu, width = 5, font = ("Consolas", 15))
	KeyTwoEntry.place(x = 100, y = 95)

	SaveButtonCustom = Button(customMenu, text = "Save", font=("Tahoma", 15, "bold"), bg="#22b11a", fg="#FFFFFF", command=SaveChange)
	SaveButtonCustom.place(x=60, y=145)



ButtonX = Button(frameIn, text=" K1 ", font=("Tahoma", 13),
                 bd=2, relief="solid", bg="#303841", fg="#FFFFFF")
# ButtonX.bind("<KeyPress>", changeColor)
# ButtonX.bind("<KeyRelease>", changeColorDefault)
ButtonX.place(x=0, y=0)

ButtonY = Button(frameIn, text=" K2 ", font=("Tahoma", 13),
                 bd=2, relief="solid", bg="#303841", fg="#FFFFFF")
ButtonY.place(x=0, y=40)


CountingText = Label(frameIn, text=countX, font=(
    "Tahoma", 13), bg="#03ff01", fg="#FFFFFF", justify=RIGHT)
# CountingText.place(x = 18, y = 40)
CountingText.place(x=50, y=5)

CountingText2 = Label(frameIn, text=countY, font=(
    "Tahoma", 13), bg="#03ff01", fg="#FFFFFF")
CountingText2.place(x=50, y=45)

# Current Key use
KeyOneCurrent = Button(frameIn, text = "Key 1: %s" %(Key1), bd=2, relief="solid", font=("Tahoma", 13), bg="#303841", fg="#FFFFFF")
KeyOneCurrent.place(x = 275, y = 0)

KeyTwoCurrent = Button(frameIn, text = "Key 2: %s" %(Key2), bd=2, relief="solid", font=("Tahoma", 13), bg="#303841", fg="#FFFFFF")
KeyTwoCurrent.place(x = 275, y = 40)


# Custom key
CustomButton = Button(main, text = "Custom Key", font=(
    "Tahoma", 13, "bold"), bg="#3f48cc", fg="#FFFFFF", command = ChangeKey)
CustomButton.place(x = 20, y = 125)

# Save Profile
SaveButton = Button(main, text = "Save", font=(
    "Tahoma", 13, "bold"), bg="#22b11a", fg="#FFFFFF")
SaveButton.place(x = 150, y = 125)

# Open Profile
OpenButton = Button(main, text = "Open", font=(
    "Tahoma", 13, "bold"), bg="#303841", fg="#FFFFFF")
OpenButton.place(x = 220, y = 125)


# Use for listening to key without making app to be focus
listener = keyboard.Listener(
    on_press=changeColor,
    on_release=changeColorDefault)
listener.start()


# main.bind("<KeyPress>", changeColor)
# main.bind("<KeyRelease>", changeColorDefault)


main.mainloop()
