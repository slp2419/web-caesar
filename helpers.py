def alphabet_position(letter):
  cap_letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  lowercase_letter="abcdefghijklmnopqrstuvwxyz"
  letter[0]
  position=0
  if letter[0] in lowercase_letter:
    position=lowercase_letter.index(letter[0])
  else:
    position=cap_letter.index(letter[0])
  return position


def rotate_character(char,rot):
  cap_letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  lowercase_letter="abcdefghijklmnopqrstuvwxyz"
  if char.isalpha():
    initial_char = alphabet_position(char)
    final_char = initial_char + rot
    if final_char>25:
      final_char=final_char%26
  if char[0] in lowercase_letter:
    return lowercase_letter[final_char]
  elif char[0] in cap_letter:
    return cap_letter[final_char]    
  else:
    return char 
