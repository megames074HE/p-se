# Mitt första Gui projekt med tkinter i Python

### GUI och Layout

Jag tänkte först använda grid för min layout eftersom där kan man dela in allt i 'grids' Så om jag har en grid som är 3x3 stor har jag typ 9 platser. Men i slutet gick jag med pack eftersom det gick lätt att använda med padx och pady. Med padx och pady kan jag ha padding mellan 2 objekter. Det gör allt lite finare

Och pack placerar bara allt i tkinter guin. Och man kan flytta grejer till höger och vänster med side=LEFT/RIGHT. 

### Spara

Vi spara grejer i påsen med en lista. Först har man ett tkinter Entry. Det är en form vars man kan fylla in ett variable. Och man kan spara en variable i listan med list.append({variable}).lower(). Jag gjorde lower() för att då behöver man inte oroa sig över stora bokstaver när man söker till exempel nåt i påsen. 

### Kontroller

Kontroller för tkinter funkar att man ska börja med importera tkinter. 

Sen ska man skapa huvudfönster med root = tkinter.Tk()

och för att skapa en knapp till exempel börja man med att ange en variable: knapp = Button(root, text='knapp', command=def)
med command i en knapp kan man runna en def function.

Sen ska man göra knapp.pack(). Det placerar knappen i din GUI.

### Skillnader mellan GUIn och terminalen

Såklart är guin lite lättare att använda. Den har ju knappar så allt blir lite mer tydligt och man behöver inte skriva in bokstäver hela tiden. Programmet funkar samma som den i terminalen. Men på startskärmen ser man direkt hur mycket plats det finns kvar i påsen.

### Strukturen

I terminalen drivs programen mest af if satser. Men i GUIn drivs mest av def functions. Varje knapp har sin egna def function.

Påsen antal count grejen på startskärmen var först lite knepigt att programera eftersom varje gång när min function update() blev kallad fick jag en ny rad med text istället för en updaterad siffra. Detta var för att .pack adda en ny textdel istället för att uppdatera texten. Så man knan använda .config istället för att bara uppdatera texten. 

### Förbättringar

Det finns några förbättringar med GUIn att det set bättre ut. Men alltså att koden är lite snyggare. allt är lite lättare att läsa. Fast den här gjorden mycket mer rader med kod än jag hade med terminalen. 

Jag tror det är ganska svårt att använda tkinter första gång eftersom man glömma skriva pack med () hela tiden så man undrar bara varför det inte funkar då. Och med tkinter måste man skriva ganska mycket för lite layout och gui. Så det kan ibland bli förvirrade snabbt.
