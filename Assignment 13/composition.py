class Engine:
    def start(self):
        return "Engine started!"

class Car:
    def __init__(self, engine):
        self.engine = engine  # Car object contains an Engine object

    def start_car(self):
        return f"Car is starting... {self.engine.start()}"
    
   
engine = Engine()

car = Car(engine)

print(car.start_car())

