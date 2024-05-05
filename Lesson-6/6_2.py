# Код Морзе для представления цифр и букв использует тире и точки. Напишите
# функцию для кодирования текстового сообщения в соответствии с кодом Морзе.
# (словари в помощь)

def smpl_func():
    letters = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
    morz_symb = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
    dictionary = dict(zip(letters, morz_symb))
    return dictionary

text = input("Enter text:").upper()

result = (smpl_func().get(letter) for letter in text if smpl_func().get(letter))
print(' '.join(result))