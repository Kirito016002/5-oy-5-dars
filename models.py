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
    

def find_elements(data:list[int])->list:
    # result = list()
    # max_num = max(data)
    # num = min(data)
    # while num < max_num:
    #     if num not in data:
    #         result.append(num)
    #     num += 1
    # return result

    # for i in range(min(data), max(data) +1):
    #     if i not in data:
    #         result.append(i)
    # return result

    return range(data)

print(find_elements(10))