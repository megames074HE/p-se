run = True
print('vällkommen till påsen')
bag = []

while run:
    print('Visa innehållet i påsen [V]')
    print('Spara i påsen [S]')
    print('Ta bort nåt ur påsen [D]')
    print('Avsluta [Q]')
    choice = input('Välj: ').lower()
    if choice == 'q':
        run = False
    elif choice == 'v':
        for thing in bag:
            print(thing)
    elif choice == 's':
        
        if len(bag) > 10:
            print('Du har inte en sånt stor påse')
        else:
            bag.append(input('skriv vad du vill spara: '))
            print(f'du har {10 - len(bag)} platser kvar')
        
    elif choice == 'd':
        for thing in bag:
            print(thing)
        try:
            bag.remove(input('skriv vad du vill ta bort: '))
        except ValueError:
            print('Naah den finns inte i listan testa igen.')
    else:
        print('Fel kommando, testa igen')
    