class Student:

    def __init__(self,name:str,age:int,tracks:list,score:float):
        self.name:str=name
        self.age:int=age
        self.tracks:list=tracks
        self.score:float=score
        pass

    def change_name(self,name):
        self.name=name
        print(self.name)

    def change_age(self,age):
        self.age=age
        print(self.age)

    def add_track(self,tracks):
        self.tracks.append(tracks)
        print(self.tracks)

    def get_score(self,score):
        self.score=score
        print(self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(40.90)
