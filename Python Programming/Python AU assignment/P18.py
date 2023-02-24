#Write a Python program to read a character from the user and check whether it is a vowel (aeiou) or consonant.
n=input('Enter an alphabet')
if ord(n)==97 or ord(n)==101  or ord(n)==105  or ord(n)==111  or ord(n)==117  or ord(n)==65 or ord(n)==69 or ord(n)==73 or ord(n)==79 or ord(n)==85:
    print('ITS A VOWEL')
else:
    print('ITS A CONSONANT')