class Deco:
    def __init__(self,func):
        self.func=func
        
    def __call__(self):
        greet=self.func()
        return greet.upper()

@Deco
def greet_person():
    return "Hello Man"


print(greet_person())
