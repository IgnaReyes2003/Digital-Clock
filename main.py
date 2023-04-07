import tkinter as tk
import time

root = tk.Tk()
root.geometry("400x250")
root.title("Digital Clock")
root.tk_setPalette("black")

def clear_days():
    mon_day_lb.config(fg="#c3c3c3")
    tue_day_lb.config(fg="#c3c3c3")
    wed_day_lb.config(fg="#c3c3c3")
    thu_day_lb.config(fg="#c3c3c3")
    fri_day_lb.config(fg="#c3c3c3")
    sat_day_lb.config(fg="#c3c3c3")
    sun_day_lb.config(fg="#c3c3c3")

def update_time():
    hours = time.strftime("%H")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    
    time_lb.config(text=f"{hours}:{minutes}:{seconds}")

    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%Y")

    am_pm = time.strftime("%p")

    date_lb.config(text=f"{date}-{month}-{year}")
    am_pm_lb.config(text=am_pm)

    day = time.strftime("%a")

    clear_days()
    days[day].config(fg="white",font=("bold",12))

    root.after(1000, update_time)

clock_frame = tk.Frame(root)

days_frame=tk.Frame(clock_frame)

mon_day_lb = tk.Label(days_frame, text="MON")
mon_day_lb.pack(side=tk.LEFT,padx=10)
tue_day_lb = tk.Label(days_frame, text="TUE")
tue_day_lb.pack(side=tk.LEFT,padx=10)
wed_day_lb = tk.Label(days_frame, text="WED")
wed_day_lb.pack(side=tk.LEFT,padx=10)
thu_day_lb = tk.Label(days_frame, text="THU")
thu_day_lb.pack(side=tk.LEFT,padx=10)
fri_day_lb = tk.Label(days_frame, text="FRI")
fri_day_lb.pack(side=tk.LEFT,padx=10)
sat_day_lb = tk.Label(days_frame, text="SAT")
sat_day_lb.pack(side=tk.LEFT,padx=10)
sun_day_lb = tk.Label(days_frame, text="SUN")
sun_day_lb.pack(side=tk.LEFT,padx=10)

days_frame.pack(pady=10)

days = {"Mon": mon_day_lb,
        "Tue": tue_day_lb,
        "Wed": wed_day_lb,
        "Thu": thu_day_lb,
        "Fri": fri_day_lb,
        "Sat": sat_day_lb,
        "Sun": sun_day_lb}

time_lb = tk.Label(clock_frame, font=("DS-Digital",50))
time_lb.pack(pady=10)

date_frame = tk.Frame(clock_frame)

date_lb = tk.Label(date_frame, font=("DS-Digital",15))
date_lb.pack(side=tk.LEFT)

am_pm_lb = tk.Label(date_frame, font=("DS-Digital",15))
am_pm_lb.pack(side=tk.RIGHT)

date_frame.pack(pady=10, fill=tk.X)

clock_frame.pack()

update_time()
root.mainloop()
