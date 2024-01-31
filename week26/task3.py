class Student:

    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    
    def setAge(self, age):
        self.age = age
    
    def getAge(self):
        return self.age

    def setMarks(self, marks):
        self.marks = marks
    
    def getMarks(self):
        return self.marks
    
    def display(self):
        return ("The student: "+ str(self.name)+ ", ID Number: "+ str(self.ID)+ ", Age: "+ str(self.getAge())+ ", Mark: "+ str(self.getMarks()))
    
#main
student = Student("Adam", "ID123")
student.setAge(19)
student.setMarks(100)
print(student.display())
