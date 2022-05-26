class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track,score):
        self.name=name
        self.age=age
        self.track=track
        self.score=score

    
Peter = Student(name="Peter", age=34, track="UI/UX",score=21)

# Expected methods
print(Peter.name)
print(Peter.age)
print(Peter.track)
print(Peter.score)
