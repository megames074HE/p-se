run = True
print('vällkommen till påsen')
bag = []

while run:
    print('Visa innehållet i påsen [V]')
    print('Spara i påsen [S]')
    print('Avsluta [Q]')
    choice = input('Välj: ').lower()
    if choice == 'q':
        run = False
    elif choice == 'v':
        for thing in bag:
            print(thing)
    elif choice == 's':
        bag.append(input('skriv vad du vill spara: '))
    else:
        print('Fel kommando, testa igen')
    