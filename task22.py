# Напишите функцию который будет конвертировать Фаренгейт в Цельсии и .
# (0 °C × 9/5) + 32 = 32 °F
# T(°C) = (T(°F) - 32) / 1.8


cel = int(input('vvedite gradusi po celsiyu'))
def func (cel):
    far = cel*9/5 + 32
    print(f'{cel} gradusov po celsiyu budut ravni', far,'po farenheitu')
func (cel)

far1 = int(input('vvedite farenheiti'))
def func1 (far1):
    cel = (far1-32)*5/9
    print(f'{far1} gradusov po farenheitu ravni', cel, 'po celsiyu')
func1 (far1)