# class Week:
#     __weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

#     @classmethod
#     def __getitem__(cls, index):
#         return cls.__weekdays[index]
    

# a = Week
# print(a()[0])

class Week:
    def __init__(self) -> None:
        self.weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __getitem__ (self, index):
        return self.weekdays[index]