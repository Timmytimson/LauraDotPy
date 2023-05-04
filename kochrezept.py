def hello_world():
    print('Hello World')

def hello_you(name):
    print('Hello ' + str(name))

def wort_kürzer_als_4(wort):
    länge = len(wort)
    print(wort, länge)
    if länge < 4:
        return True
    else:
        return False

def tausend_pimmel():
    for i in range(0, 1000):
        print("Pimmel", i)

def viele_pimmel(start, stop):
    for i in range(start, stop+1):
        print("Pimmel", i)

def zeichen_für_zeichen(wort):
    for char in wort:
        print(char)

def zeichen_für_zeichen_rückwärts(wort):
    länge = len(wort)
    for i in range(länge-1, -1, -1):
        print(wort[i])

def zeichen_für_zeichen_while(wort):
    länge = len(wort)
    position = 0
    while position < länge:
        print(wort[position])
        position += 1 #position = position + 1


'''Datentypen'''
b = False # Ja/Nein "Boolean"
i = 2312314 # Ganze Zahlen "Integer"
f = 3.1413 # Fließkommazahlen "Float"
c = 'A' # Buchstaben/Zeichen "Characters"
s = "Blafasel" # Wörter/Texte "Strings"

laenge_wort = 4
laengeWort = 5

'''Ausgeführter Code'''

'''hello_world()
hello_you('Laura')
hello_you('Ratzupaltuff')
hello_you(5)

wort_1 = "awserfgwer"
wort_2 = "sda"
print(wort_kürzer_als_4(wort_1))
print(wort_kürzer_als_4(wort_2))

tausend_pimmel()'''

# viele_pimmel(4, 120000)

wort = "abcdeFG"
länge = len(wort)
'''
print(wort, länge)
print(wort[0])
print(wort[länge-1])

zeichen_für_zeichen(wort)
zeichen_für_zeichen_rückwärts(wort)'''

zeichen_für_zeichen_while(wort)