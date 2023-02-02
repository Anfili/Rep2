# coding=utf-8
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    txt = "еще раз здрасте"
    print('Hi, {name1} ttt {t1}'.format(name1=name, t1=txt))  # Press Ctrl+F8 to toggle the breakpoint.
    print('Hi, {} ttt222 {}'.format(name, txt))
    animal = 'fish'
    animal = animal[0].upper() + animal[1:-1] + animal[-1].upper()
    print('{}'.format(animal))