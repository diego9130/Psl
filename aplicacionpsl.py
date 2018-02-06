# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 17:20:43 2018

@author: Diego Aragòn
"""

#FUNCION GRAFICAR--------------------------------------------------------------------------------------------------------
def graficar(size,numero,dig):
    
    #se definen puntos fijos para calcular pixeles
    pfijox = ((dig)*(size+2))+((size+2)/2)   # coordenada en x correspondiente al centro del digito
    pfijox = int(pfijox)                     # Se convierte a int
    pfijoy = (size*2+3)/2
    pfijoy = int (pfijoy)                    # mitad del digito en y
    pinicial = ((dig*(size+2)))              # Coordenada x donde inicia el digito   
    pinicial = int(pinicial)
    
    if numero==1:
        for y in range (1, (size*2+2)):
            for x in range (pinicial , pfijox ):
                if x == (pfijox-1):
                    impr[y][x] = '|'
                else: 
                    impr[y][x]= ' '               
        
    elif numero==2:
        for y in range (0, (size*2+3)):
            for x in range (pinicial,(pinicial+size+2)):
                if y == 0 and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif y == pfijoy and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif y == (size*2+2) and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif (y>0 and y<pfijoy)and(x==pinicial+size+1):
                    impr[y][x]='|'
                elif (y>pfijoy and y<(size*2+2))and(x==pinicial):
                    impr[y][x]='|'                     
                else: impr[y][x] = ' '
        
    elif numero==3:
        for y in range (0, (size*2+3)):
            for x in range (pinicial,(pinicial+size+2)):
                if y == 0 and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif y == pfijoy and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif y == (size*2+2) and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif (y>0 and y<pfijoy)and(x==pinicial+size+1):
                    impr[y][x]='|'
                elif (y>pfijoy and y<(size*2+2))and(x==pinicial+size+1):
                    impr[y][x]='|'                     
                else: impr[y][x] = ' '
        
    elif numero==4:
        for y in range (0, (size*2+3)):
            for x in range (pinicial,(pinicial+size+2)):               
                if y == pfijoy and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'  
                elif (y>0 and y<pfijoy)and(x==pinicial):
                    impr[y][x]='|'
                elif (y>0 and y<pfijoy)and(x==pinicial+size+1):
                    impr[y][x]='|'
                elif (y>pfijoy and y<(size*2+2))and(x==pinicial+size+1):
                    impr[y][x]='|'                     
                else: impr[y][x] =' '
        
    elif numero==5:
        for y in range (0, (size*2+3)):
            for x in range (pinicial,(pinicial+size+2)):
                if y == 0 and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif y == pfijoy and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif y == (size*2+2) and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif (y>0 and y<pfijoy)and(x==pinicial):
                    impr[y][x]='|'
                elif (y>pfijoy and y<(size*2+2))and(x==pinicial+size+1):
                    impr[y][x]='|'                     
                else: impr[y][x] = ' '
        
    elif numero==6:
        for y in range (0, (size*2+3)):
            for x in range (pinicial,(pinicial+size+2)):
                if y == pfijoy and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif y == (size*2+2) and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'                    
                elif (y>0 and y<pfijoy)and(x==pinicial):
                    impr[y][x]='|'
                elif (y>pfijoy and y<(size*2+2))and(x==pinicial+size+1):
                    impr[y][x]='|'  
                elif (y>pfijoy and y<(size*2+2))and(x==pinicial):
                    impr[y][x]='|' 
                else: impr[y][x] = ' '
        
    elif numero==7:
        for y in range (0, (size*2+3)):
            for x in range (pinicial,(pinicial+size+2)):
                if y == 0 and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif(y>0 and y<=(size*2+1))and(x==pinicial+size+1):
                    impr[y][x]='|'                                     
                else: impr[y][x] = ' '
        
    elif numero==8:
        for y in range (0, (size*2+3)):
            for x in range (pinicial,(pinicial+size+2)):
                if y == 0 and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif y == pfijoy and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif y == (size*2+2) and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif (y>0 and y<pfijoy)and(x==pinicial):
                    impr[y][x]='|'
                elif (y>0 and y<pfijoy)and(x==pinicial+size+1):
                    impr[y][x]='|'
                elif (y>pfijoy and y<(size*2+2))and(x==pinicial):
                    impr[y][x]='|' 
                elif (y>pfijoy and y<(size*2+2))and(x==pinicial+size+1):
                    impr[y][x]='|'                    
                else: impr[y][x] = ' '
        
    elif numero==9:
        for y in range (0, (size*2+3)):
            for x in range (pinicial,(pinicial+size+2)):
                if y == 0 and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif y == pfijoy and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'  
                elif (y>0 and y<pfijoy)and(x==pinicial):
                    impr[y][x]='|'
                elif (y>0 and y<pfijoy)and(x==pinicial+size+1):
                    impr[y][x]='|'
                elif (y>pfijoy and y<(size*2+2))and(x==pinicial+size+1):
                    impr[y][x]='|'                     
                else: impr[y][x] = ' '
    
        
    elif numero==0:
        for y in range (0, (size*2+3)):
            for x in range (pinicial,(pinicial+size+2)):
                if y == 0 and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif y == size*2+2 and (x>pinicial and x<=(pinicial+size)):
                    impr[y][x]='-'
                elif(y>0 and y<=(size*2+1))and(x==pinicial+size+1):
                    impr[y][x]='|'    
                elif(y>0 and y<=(size*2+1))and(x==pinicial):
                    impr[y][x]='|'                                      
                else: impr[y][x] = ' '
    
      

#PROGRAMA INICIAL----------------------------------------------------------------------------------------------------------------
#El usuario ingresa el dato
x=1

while x==1:
    y=0
    lista = input("Indique el tamaño , digito:  ")      
    if lista: 
        #se crea arreglo del tamaño de los numeros ingresados para graficar
        number = [0]*(len(lista)-2)

        #se convierte el valor ingresado de size a int comprobando que sea numero y no una letra
        try:
            size = int(float(lista[0]))  
        except ValueError:
            y+=1
            print ("Escribe un numero, no una letra.")
            
        #se Crea el arreglo de int a mostrar comprobando que sean numeros y no letras
        if lista[1] == ',':
            for count in range(2,(len(lista))):
                try:
                    number[count-2] = int(float(lista[count]))        
                except ValueError:
                    y+=1
                    print ("Escribe un numero, no una letra.")
                    x=1
            if y==0:
                x=0
        
        #Se compueba que Esten separados por coma
        elif lista[1] != ',':
            print('separe los numeros por coma '',''') 
            
        
            
        else:
            x=0
print (lista) 


      
    
#se crea la matriz del numero completo
impr = [' '] * ((size*2)+3)       #filas
for i in range(2*size+3):       #columnas
    impr[i] = [' '] * (len(number)*(size+2))


#llamo a la funcion graficar por cada numero encontrado en el arreglo
for z in range (0,len(number)):
    graficar(size,number[z],z)
    
a=""
for o in range (0,((size*2)+3)):
    for j in range (0,len(number)*(size+2)):        
        a+=str(impr[o][j])
    print (a)
    a=""
