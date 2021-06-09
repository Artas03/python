class Bird:
    def __init__(self,wingspan):
        self.wingspan = wingspan

Eagle = Bird(104)

len(Eagle)

#this code produces error because len method has no logic assigned to it in the bird class
