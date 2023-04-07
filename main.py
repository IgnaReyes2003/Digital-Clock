import tkinter as tk
import time

root = tk.Tk()
root.geometry("400x250")
root.title("Digital Clock")
root.tk_setPalette("black")

def update_time():
    hours = time.strftime("%H")
    print(hours)

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
