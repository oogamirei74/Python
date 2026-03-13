class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        return sum/3
    
s1 = student("Karim", [98, 100, 95])
print("Hi",s1.name,"\nYour avg score is:",s1.get_avg())