from inspect import currentframe
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from geopy.point import re
import pytz
from tkinter import ttk 
from geopy import Nominatim
from user_authenication import sign_in, register 
from PIL import Image, ImageTk
from fetching_data import fetchweather
from timezonefinder import TimezoneFinder
import tkintermapview


#---------------------------------------------------
root = tk.Tk()
root.title("Sign In")
root.geometry("900x500+300+200")
root.resizable(False,False)
# background images

signin_wallpaper = tk.PhotoImage(file = "image_files/sign_in_wallpaper.png")
canvas = tk.Canvas(root,width = signin_wallpaper.width(),height = signin_wallpaper.height())
root.geometry(f"{signin_wallpaper.width()}x{signin_wallpaper.height()}+300+200")
canvas.create_image(0,0,anchor = tk.NW,image = signin_wallpaper)
canvas.image = signin_wallpaper
canvas.pack(fill= "both", expand= True)

#---------------------------------------------------
# frame for signin section 

frame = tk.Frame(root,width=450,height=600,bg= "#090f18")
frame.place(x= 600,y = 50)

# page heading 
heading = tk.Label(frame,text = "Sign in",width = 25,fg = "white",bg ="#090f18",font = ("Helvetica",28,"bold"))
heading.place(x = -30,y = 50)

#---------------------------------------------------
# Input boxes for username and passwords

# functions to hold the disappearing username 
def on_enter(e):
    username.delete(0,"end")
def on_leave(e):
    name = username.get()
    if name =="":
        username.insert(0,"Username")


username = tk.Entry(frame,width = 30, fg= "white",bg = "#090f18",border = 0,font = ("Helvatica",12))
username.place(x = 90,y = 160)
username.insert(0,"Username")
username.bind('<FocusIn>',on_enter)
username.bind('<FocusOut>',on_leave)

# line frame to hold the username
tk.Frame(frame, width = 430,height = 3, bg = "white").place(x=90,y=190)


#---------------------------------------------------
# password input box and line frame

def on_enter(e):
    password.delete(0,"end")
def on_leave(e):
    name = password.get()
    if name =="":
        password.insert(0,"Password")

password = tk.Entry(frame,width = 30, fg= "white",bg = "#090f18",border = 0,font = ("Helvatica",12))
password.place(x = 90,y = 240)
password.insert(0,"Password")
password.bind('<FocusIn>',on_enter)
password.bind('<FocusOut>',on_leave)

# line frame to hold the username
tk.Frame(frame, width = 430,height = 3, bg = "white").place(x=90,y=270)

#---------------------------------------------------

# sign in button section

message_label = tk.Label(frame,text = "Don't have an account?",fg = "white",bg = "#090f18",font = ("Helvetica",9))
message_label.place(x=180 , y= 400)

#sign_up_label = tk.Button(frame,width = 6,text = "Sign up",border = 0,bg = "#090f18",cursor = "hand2",fg= "#57a1f8")
#sign_up_label.place(x = 320,y =390)

#---------------------------------------------------


def start_weather_app():
     
    #main window for weather app
    root1 = tk.Toplevel(root)
    root1.title("Weather App")
    root1.geometry("900x500+300+200")
    root1.resizable(False,False)



# creating the canvas
    #background_image = tk.PhotoImage(file = "image_files/backgroundnew.png") 
    background_image = tk.PhotoImage(file = "image_files/weather_rainy.png")
    canvas = tk.Canvas(root1, width=background_image.width(), height=background_image.height())
    canvas.pack(fill="both", expand=True)
    root1.geometry(f"{background_image.width()}x{background_image.height()}+300+200")
    # map creation
   

#positioning of rectangle on canvas
    #first we find the screen dimensions
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()
    center_of_screen_x, center_of_screen_y = screen_width/2 , screen_height/2

    #-----------------------------------------------


# Store newly created image
    images=[]

# Define a function to make the transparent rectangle
    def create_rectangle(x,y,a,b,**options):
        if 'alpha' in options:
      # Calculate the alpha transparency for every color(RGB)
            alpha = int(options.pop('alpha') * 255)
      # Use the fill variable to fill the shape with transparent color
            fill = options.pop('fill')
            fill = root1.winfo_rgb(fill) + (alpha,)
            image = Image.new('RGBA', (a-x, b-y), fill)
            images.append(ImageTk.PhotoImage(image))
            canvas.create_image(x, y, image=images[-1], anchor='nw')
        canvas.create_rectangle(x, y,a,b, **options)

# now we want to set the image as the background
    canvas.create_image(0, 0, image=background_image, anchor="nw")

# Create a rectangle in canvas
    #dark_rectangle = create_rectangle(int(center_of_screen_x+(100/2)),int(center_of_screen_y-(400/2)), int(center_of_screen_x+(100/2)), int(center_of_screen_y+(400/2)), outline = "white",fill= "black", alpha= .5)

    dark_rectangle = create_rectangle(int(50),int(50), int(1070), int(650), outline = "white",fill= "black", alpha= .5)

    header_rectangle = create_rectangle(int(75),int(70), int(1050), int(120), outline = "white",fill= "black", alpha= .5)

    #search_rectangle = create_rectangle(int(85),int(140), int(1050), int(210), outline = "white",fill= "grey", alpha= .5)

    weather_rectangle = create_rectangle(int(75),int(center_of_screen_y-(300/2)), int(770), int(635), outline = "white",fill= "black", alpha= .5)

#days
    day1_rectangle = create_rectangle(int(780),int(130), int(1050), int(635), outline = "white",fill= "black", alpha= .5)

#----------------------------------------------------
    # getting the weather data
    def on_search():
        fetchweather(textfield.get())
        pass

#----------------------------------------------------

    def on_enter(e):
        textfield.delete(0,"end")
    def on_leave(e):

        name = textfield.get()
        if name =="":
            textfield.insert(0,"Enter a city")

    textfield = tk.Entry(root1, justify="center",width=40,font = ("Helvatica",14),border = 0 ,fg = "white",bg="#090f18")
    textfield.insert(0,"Enter a city")
    textfield.bind("<FocusIn>",on_enter)
    textfield.bind("<FocusOut>",on_leave)
    textfield.place(x=330,y=80)

     
    def get_weather(event):
        try:
            city = textfield.get()

            weather_result = fetchweather(city)

            geolocator  = Nominatim(user_agent = "abcd")
            location = geolocator.geocode(city)
            obj = TimezoneFinder()
            
            result = obj.timezone_at(lng = location.longitude,lat = location.latitude)

            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            clock.config(text = current_time)
            city_name.config(text = f"{weather_result[0]}")
            name_current.config(text = "Current Weather ☁︎⋅")
            temperature_label.config(text=f"{round(weather_result[3])}°C")
            condition_label.config(text=f"{weather_result[4]}")
            humidity_label.config(text = f"Humidity: {weather_result[7]} ⛈")
            wind_label.config(text = f"Wind Speed: {weather_result[6]}m/s")
            visibility_label.config(text= f"Visibility: {weather_result[5]}")
            


            

        except Exception as e:
            messagebox.showerror("Weather App","Invalid City / Entry.")

        my_label = tk.Frame(root1)
        my_label.place(x=75,y=387)
        map_image = tkintermapview.TkinterMapView(my_label,width= 695,height=250,corner_radius=0)
        # setting coordinates
        map_image.set_address(city)
        map_image.set_position(location.latitude, location.longitude)
        map_image.set_zoom(20)
        map_image.pack()


#-----------------------------------------------------
# Labels to display the data on the screen

    city_name = tk.Label(root1,font = ("Microsoft YaHei",14),bg = "#090f18",fg = "white")
    city_name.place(x= 100,y = 150)
    temperature_label = tk.Label(root1,font =("Microsoft YaHei",18),bg = "#090f18",fg = "white")
    temperature_label.place(x = 100 ,y = 260)
    condition_label = tk.Label(root1,font =("Microsoft YaHei",14),bg = "#090f18",fg = "white")
    condition_label.place(x = 785 ,y = 290)
    weather_label = tk.Label(root1,font =("Microsoft YaHei",14),bg = "#090f18",fg = "white")
    weather_label.place(x = 785 ,y = 310)
    humidity_label = tk.Label(root1,font =("Microsoft YaHei",14),bg = "#090f18",fg = "white")
    humidity_label.place(x = 785 ,y = 230)
    wind_label = tk.Label(root1,font =("Helvatica",14),bg = "#090f18",fg ="white")
    wind_label.place(x = 785 ,y = 355)
    visibility_label = tk.Label(root1,font =("Microsoft YaHei",14),bg = "#090f18",fg = "white")
    visibility_label.place(x = 785 ,y = 430)
    name_current = tk.Label(root1,font=("Microsoft YaHei",14),fg = "white",bg = "#090f18")
    name_current.place(x= 785,y = 150)
    clock = tk.Label(root1,font =("Microsoft YaHei",24))
    textfield.bind("<Return>",get_weather)

    #-------------------------------------------------------------------------------
    



    canvas.pack()

    root1.mainloop()

#----------------------------------------------------------------------------------
# User interface for sign up 

def sign_up_ui():
    root2 = tk.Toplevel(root)
    root2.title("Sign Up")
    root2.resizable(False,False)
# background images

    signup_wallpaper = tk.PhotoImage(file = "image_files/signupbg.png")
    canvas = tk.Canvas(root2,width = signup_wallpaper.width(),height = signup_wallpaper.height())
    root2.geometry(f"{signin_wallpaper.width()-70}x{signin_wallpaper.height()}+300+200")
    canvas.create_image(0,0,anchor = tk.NW,image = signup_wallpaper)
    canvas.image = signup_wallpaper
    canvas.pack(fill= "both", expand= True)

#---------------------------------------------------
# frame for signin section 

    frame = tk.Frame(root2,width=450,height=600,bg= "#090f18")
    frame.place(x= 600,y = 50)

# page heading 
    heading = tk.Label(frame,text = "Sign up",width = 25,fg = "white",bg ="#090f18",font = ("Helvetica",28,"bold"))
    heading.place(x = -30,y = 50)

#---------------------------------------------------
# Input boxes for username and passwords

# functions to hold the disappearing username 
    def on_enter(e):
        username.delete(0,"end")
    def on_leave(e):
        name = username.get()
        if name =="":
            username.insert(0,"Username")


    username = tk.Entry(frame,width = 30, fg= "white",bg = "#090f18",border = 0,font = ("Helvatica",12))
    username.place(x = 90,y = 160)
    username.insert(0,"Username")
    username.bind('<FocusIn>',on_enter)
    username.bind('<FocusOut>',on_leave)

# line frame to hold the username
    tk.Frame(frame, width = 430,height = 3, bg = "white").place(x=90,y=190)


#---------------------------------------------------
# password input box and line frame

    def on_enter(e):
        password.delete(0,"end")
    def on_leave(e):
        name = password.get()
        if name =="":
            password.insert(0,"Password")

    password = tk.Entry(frame,width = 30, fg= "white",bg = "#090f18",border = 0,font = ("Helvatica",12))
    password.place(x = 90,y = 240)
    password.insert(0,"Password")
    password.bind('<FocusIn>',on_enter)
    password.bind('<FocusOut>',on_leave)

# line frame to hold the username
    tk.Frame(frame, width = 430,height = 3, bg = "white").place(x=90,y=270)

    def sign_up_verification():
        uname = username.get()
        pword = password.get()
        
        key_value = register(uname,pword)
        if key_value == True:
            start_weather_app()
        elif key_value == "wrong":
            messagebox.showerror("Invalid","These characters aren't accepted")
        elif key_value == "taken":
            messagebox.showerror("Taken!","Sorry,Username already in use ")
        else:
            messagebox.showerror("Error","An unknown error occurred")

    sign_up_label = tk.Button(frame,width = 20,text = "Sign up",border = 0,bg = "#57a1f8",cursor = "hand2",fg= "white",command = sign_up_verification)
    sign_up_label.place(x = 140,y =320)

    canvas.pack()
    root2.mainloop()

    


# this is the function to sign into the app

def sign_in_prompt():
    uname = username.get()
    pword = password.get()

    if sign_in(uname,pword):
        start_weather_app()

    else:
        messagebox.showerror("Invalid","Username and Password don't match. Try Again!")

tk.Button(frame, width = 20, pady = 7,text = "Sign in",bg= "#57a1f8",border=0,command= sign_in_prompt).place(x = 140,y=320)
#---------------------------------------------------

# this is for the sign up button with its logic

sign_up_label = tk.Button(frame,width = 6,text = "Sign up",border = 0,bg = "#090f18",cursor = "hand2",fg= "#57a1f8",command = sign_up_ui)
sign_up_label.place(x = 320,y =390)

#----------------------------------------------------



root.mainloop()
