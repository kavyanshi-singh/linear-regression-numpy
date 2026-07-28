class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def avg(self):
        return sum(self.marks)/3
        

    def grade(self):
        avg=self.avg()

        if avg>=90:
            return("Grade A+")
        elif avg>=80:
            return("Grade A")
        elif avg>=70:
            return("Grade B+")
        elif avg>=60:
            return("Grade B")
        elif avg>=50:
            return("Grade C")
        else:
            return("Fail")


    def __str__(self):
        return(f"{self.name} has average {self.avg(): .2f} and {self.grade()}")

def get_student():
        name=input("What's your name? ")
        marks1=int(input("Calculus marks? "))
        marks2=int(input("Electrical marks? "))
        marks3=int(input("Mechanics marks? "))

        marks=[marks1, marks2, marks3]

        return Student(name, marks)



def main():
        
        student=get_student()
        print(student)
    
if __name__=="__main__":
    main()


