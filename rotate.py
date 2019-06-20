alphabet = "abcdefghijklmnopqrstuvwxyz"
def alphabet_position(letter):
    if not(letter.isalpha()):
       return letter
    position = alphabet.index(letter.lower())
    return position
    
    
def rotate_character(char, rot):
    if not(char.isalpha()):
       return char
    position = alphabet_position(char)
    new_position = (position + rot) % 26
    if char.isalpha():
        if char.islower():
            new_character = new_position + 97
            return chr(new_character)
        else:
            new_character = new_position + 65
            return chr(new_character)
    else:
        return char

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
    