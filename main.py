import tkinter as tk

root = tk.Tk()
root.geometry("400x250")
root.title("Digital Clock")
root.tk_setPalette("black")

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

clock_frame.pack()

root.mainloop()
