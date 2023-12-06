class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self, other_pod):
        other_pod.condition = "trashed"

anakin_pod = AnakinsPod(100, "perfect", 500)
sebulba_pod = SebulbasPod(120, "repaired", 600)
print(anakin_pod.max_speed) # 100
anakin_pod.boost()
print(anakin_pod.max_speed) # 200
sebulba_pod.flame_jet(anakin_pod)
print(anakin_pod.condition) # trashed

# Answers to the Object Oriented Prompt Questions:
# 1. Encapsulation: Our classes encapsulate the behavior and state.
#    Abstraction: We abstract the general idea of a podracer with the Podracer class.
#    Inheritance: AnakinsPod and SebulbasPod classes inherit from the Podracer class.
# 2. OOP would be easier for organization and scalability. 
# 3. OOP assisted in the solving of this problem by allowing us to model real-world objects. 