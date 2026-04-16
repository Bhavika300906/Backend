class Student:
    subject = "python" #class attribute

    def __init__(self,name,age):
        self.name= name
        self.age = age


        @classmethod
        def get_subject(cls): #in class method use cls insted of self
            return cls.subject


        @classmethod
        def set_subject(cls,new_subject):
            cls.subject = new_subject

#Class calling mthod
print(Student.get_subject())


Student.set_subject("Flutter")
print(Student.get_subject()) 
            
