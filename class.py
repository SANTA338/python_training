class student:
    def __init__(self):
        self.student_roll = int(input("Enter the roll number:"))
        self.subjects = []
        self.total =0
        self.avg=0

    def marks(self):
        print(f"Enter the marks for students")
        for i in range(1,4):
            mark = float(input(f" subject{i}:"))
            self.subjects.append(mark)

    def avrg(self):
        self.total = sum(self.subjects)
        self.avg = self.total/len(self.subjects)
    def display(self):
        print(f"{self.student_roll}")
        print(f"\nfor total 300:{self.total},\n avrage:{self.avg}")
        print("remaing marks:",300-self.total)
s1=student()
s1.marks()
s1.avrg()
s1.display()