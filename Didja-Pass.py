from tkinter import *


labs, attendance = 0.45, 0.05
midterm, final = 0.25, 0.25

lab_grade = float(input("Enter your lab average: "))
attendance_grade = float(input("Enter your attendance average: "))
midterm_grade = float(input("Enter your midterm grade: "))
final_grade = float(input("Enter what you hope your final exam grade is: "))
ult_grade = round(((labs * lab_grade) + (attendance_grade * attendance) +
                   (midterm * midterm_grade) + (final * final_grade)), 3)
final_sum = f"Your est. final grade is {ult_grade}%"
root = Tk()
root.title("Didja-Pass v.0.3")
frame = Frame(root, width=100, height=100)
frame.pack()

lab = Label(frame, text=f"Labs: {lab_grade}")
lab.pack()
att = Label(frame, text=f"Attendance: {attendance_grade}")
att.pack()
mid = Label(frame, text=f"Midterm: {midterm_grade}")
mid.pack()
fin = Label(frame, text=f"Rough Est. Final: {final_grade}")
fin.pack()
label_one = Label(frame, text=final_sum)
label_one.pack()
label_two = Label(frame, text="Well, did you pass?")
label_two.pack()

root.mainloop()
