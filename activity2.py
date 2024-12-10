class vehicle:
    def __init__(self,max_speed,miliage,engine):
        self.max_speed=max_speed
        self.miliage=miliage
        self.engine=engine

car1=vehicle(200,89,"V8")
car2=vehicle(190,53,"V5")
car3=vehicle(145,32,"AMG")
print("Car 1 has a speed of {} and miliage of {} and its engine is {}".format(car1.max_speed,car1.miliage,car1.engine))
print("Car 2 has a speed of {} and miliage of {} and its engine is {}".format(car2.max_speed,car2.miliage,car2.engine))
print("Car 3 has a speed of {} and miliage of {} and its engine is {}".format(car3.max_speed,car3.miliage,car3.engine))