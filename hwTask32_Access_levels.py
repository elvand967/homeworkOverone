# Домашнее задание Задача №32
# Продемонстрируйте разные уровни доступа на примере любого класса

class AccessLevels():
    attribute1 = 'атрибут класса с "Public" доступом'
    _attribute2 = 'атрибут класса с "Protected" доступом'
    __attribute3 = 'атрибут класса с "Private" доступом'

    def method1(self):
        return print('метод класса с "Public" доступом')

    def _method2(self):
        return print('метод класса с "Protected" доступом')

    def __method3(self):
        return print('метод класса с "Private" доступом')

test = AccessLevels()
print(test.attribute1) # атрибут класса с "Public" доступом
print(test._attribute2) # атрибут класса с "Protected" доступом
#print(test.__attribute3) # AttributeError: 'Access_levels' object has no attribute '__attribute3'
print(test._AccessLevels__attribute3) # атрибут класса с "Private" доступом
test.method1()    # метод класса с "Public" доступом
test._method2()   # метод класса с "Protected" доступом
#test.__method3()  # AttributeError: 'Access_levels' object has no attribute '__method3'
test._AccessLevels__method3() # метод класса с "Private" доступом