# class Week:
#     def __init__(self) -> None:
#         self.__weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

#     def __getitem__ (self, index):
#         return self.__weekdays[index]
    

class Week:
    __weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    @classmethod
    def get_element(cls, *args):
        # if len(args) == 1:
        #     result = cls.__weekdays[args[0]]
        # elif len(args) == 2:
        #     result = cls.__weekdays[args[0]:args[-1]]
        # elif len(args) == 3:
        #     result = cls.__weekdays[args[0]:args[1]:args[-1]]
        # else:
        #     raise TypeError
        # return result

        match len(args):
            case 1:
                result = cls.__weekdays[args[0]]
            case 2:
                result = cls.__weekdays[args[0]:args[-1]]
            case 3:
                result = cls.__weekdays[args[0]:args[1]:args[-1]]
            case _:
                raise TypeError
        return result