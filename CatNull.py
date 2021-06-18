from colorama import init
from colorama import Fore, Back, Style

init()

print( Back.BLUE )
print( Fore.YELLOW )
first = (input('Введите первое число : '))
second = 0
print( Fore.WHITE )
try:
  print(first / second)
except:
  print('Поймано исключение Деление по нулю')

print( Fore.RED )
print('Программа завершена!')   

input() 	