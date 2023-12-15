class SuperList(list):
    def __len__(self):
        return 1000

list1 = list()

list2 = SuperList()
print(list2.append(5))
print(list2)
print(type(list1))

print(issubclass(SuperList, list))

