import tkinter as tk
import sys
import pyglet, os
from pyglet import font
from PIL import Image, ImageTk

# FONT HANDLING

BOLD = 'CircularStd-Bold'
THIN = 'CircularStd-Book'

# END FONT HANDLING

window = tk.Tk()
window.attributes('-fullscreen', True)
window.configure(bg='black')

#Close on escape key
def close(event):
    window.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing

weatherFrame = tk.Frame(window, background='black', borderwidth=1, relief='sunken')
weatherFrame.grid(column=0, row=0)

schoolFrame = tk.Frame(window, background='black', borderwidth=1, relief='sunken')
schoolFrame.grid(column=1, row=1)

emailFrame = tk.Frame(window, background='black', borderwidth=1, relief='sunken')
emailFrame.grid(column=0, row=1)

quoteFrame = tk.Frame(window, background='black', borderwidth=1, relief='sunken')
quoteFrame.grid(column=1, row=0)

def buildWeatherFrame():
    # results = [temp, temp_max, temp_min, feels_like, temp_kf, clouds, status, sunrise, sunset]
    # temp = #CHANGE
    # tempString = str(currTemp) + u'\N{DEGREE SIGN}'
    
    # temp_max = #CHANGE
    # temp_maxString = str(temp_max) + u'\N{DEGREE SIGN}'

    # temp_min = #CHANGE
    # temp_minString = str(temp_min) + u'\N{DEGREE SIGN}'

    # feels_like = #CHANGE
    # feels_likeString = str(feels_like) + u'\N{DEGREE SIGN}'

    # temp_kf = #CHANGE
    # temp_kfString = str(temp_kf) + u'\N{DEGREE SIGN}'

    weatherDisplay = tk.Frame(weatherFrame, background='black')
    
    tempLabel = tk.Label(weatherDisplay, text='temp', font=(BOLD, 36), foreground='white', background='black').grid(row=0, column=0)
    temp_maxLabel = tk.Label(weatherDisplay, text='max', font=THIN, foreground='white', background='black').grid(row=1, column=0)
    temp_minLabel = tk.Label(weatherDisplay, text='min', font=THIN, foreground='white', background='black').grid(row=2, column=0)
    feels_likeLabel = tk.Label(weatherDisplay, text='feelslike', font=THIN, foreground='white', background='black').grid(row=3, column=0) #fl

    cloudsLabel = tk.Label(weatherDisplay, text='clouds', font=THIN, foreground='white', background='black').grid(row=, column=1) #clouds
    statusLabel = tk.Label(weatherDisplay, text='detailedstatus', font=THIN, foreground='white', background='black').grid(row=1, column=1) #ds
    sunriseLabel = tk.Label(weatherDisplay, text='sunriselabel', font=THIN, foreground='white', background='black').grid(row=4, column=0) #sunrise
    sunsetLabel = tk.Label(weatherDisplay, text='sunsetlabel', font=THIN, foreground='white', background='black').grid(row=4, column=1) #sunset
    

    cloud = Image.open('assets/Cloud.png')
    cloud = cloud.resize((100, 100), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(cloud)
    img = tk.Label(weatherFrame, image=render, borderwidth=0, highlightthickness=0)
    img.image = render
    img.pack()



    tempLabel.pack()
    temp_maxLabel.pack()
    temp_minLabel.pack()
    feels_likeLabel.pack()
    temp_kfLabel.pack()
    cloudsLabel.pack()
    statusLabel.pack()
    sunriseLabel.pack()
    sunsetLabel.pack()

buildWeatherFrame()
window.bind('<Escape>', close)
window.mainloop()