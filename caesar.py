from helpers import alphabet_position, rotate_character

def encrypt(text,rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in text:
      encrypted = encrypted + rotate_character(char,rot)
    return encrypted




def main():
   text= input ("type a message")
   rotate= int(input("Rotate by :"))
   print(encrypt(text,rotate))


if __name__ == "__main__":
    main()

