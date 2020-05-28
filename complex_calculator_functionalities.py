from math import sqrt, pow, atan2, cos, sin, pi
import tkinter as t

#  to add the complex number
def Add(numeros):
    resposta = []
    resposta.append(numeros[0][0] + numeros[1][0])
    resposta.append(numeros[0][1] + numeros[1][1])
    return resposta

# to subtract the complex number
def Subtract(numeros):
    resposta = []
    resposta.append(numeros[0][0] - numeros[1][0])
    resposta.append(numeros[0][1] - numeros[1][1])
    return resposta

# to multiply the complex number
def Multiply(numeros):
    resposta = []
    resposta.append(numeros[0][0] * numeros[1][0])
    resposta.append(numeros[0][1] + numeros[1][1])
    return resposta
    
# to divide the complex number
def Divide(numeros):
    resposta = []
    resposta.append(numeros[0][0] / numeros[1][0])
    resposta.append(numeros[0][1] - numeros[1][1])
    return resposta

# parse to pol
def ParseToPol(real, imaginario):
    __answerList = []
    __z = sqrt((pow(real, 2) + pow(imaginario, 2)))
    __teta = atan2(imaginario, real) * (180 / pi)

    __answerList.append(round(__z, 3))
    __answerList.append(round(__teta, 3))
    return __answerList
    
# parse to Rec
def ParseToRec(z, teta):
    __answerList = []

    __real = z * cos((teta * (pi / 180)))
    __imaginario = z * sin((teta * (pi / 180))) 

    __answerList.append(round(__real, 3))
    __answerList.append(round(__imaginario, 3))
    return __answerList

# parse the complex number to pol format 
def AnswerRadioButtonPol(EntryR, EntryC):
    real = EntryR.get()
    imaginario = EntryC.get()

    if(real != '' and imaginario != ''):
        real = float(real)
        imaginario = float(imaginario)
        
        z = ParseToPol(real, imaginario)[0]
        teta = ParseToPol(real, imaginario)[1]

        EntryR.delete(0, t.END)
        EntryC.delete(0, t.END)
        EntryR.insert(0, str(z))
        EntryC.insert(0, str(teta))
        return
    else:
        return
    
    
# parse the complex number to rec format
def AnswerRadioButtonRec(EntryR, EntryC):
    z = EntryR.get()
    teta = EntryC.get()

    if(z != '' and teta != ''):
        z = float(z)
        teta = float(teta)
        
        real = ParseToRec(z, teta)[0]
        imaginario = ParseToRec(z, teta)[1]

        EntryR.delete(0, t.END)
        EntryC.delete(0, t.END)
        EntryR.insert(0, str(real))
        EntryC.insert(0, str(imaginario))
        return
    else:
        return
    
# when plus button is clicked
def PlusButtonClk(entries, radios):
    numeros = []
    for entry in entries[0]:
        if(entry.get()==''):
            return
    for i, j in zip([0,1],[0,2]):
        if(radios[i].get()=='P'):         
            recNumber = ParseToRec(float(entries[0][j].get()), float(entries[0][j+1].get()))   
            real = recNumber[0]
            imaginario = recNumber[1]
        else:
            # entry.get()    
            real = float(entries[0][j].get())
            imaginario = float(entries[0][j+1].get())
        numeros.append([real, imaginario])
    Sum = Add(numeros)
    SumPol = ParseToPol(Sum[0], Sum[1])
    radios[2].set('P')
    for i in [0,1]:
        entries[1][i].delete(0, t.END)
        entries[1][i].insert(0, SumPol[i])

    
# when minus button is clicked
def MinusButtonClk(entries, radios):
    numeros = []
    for entry in entries[0]:
        if(entry.get()==''):
            return
    for i, j in zip([0,1],[0,2]):
        if(radios[i].get()=='P'):         
            recNumber = ParseToRec(float(entries[0][j].get()), float(entries[0][j+1].get()))   
            real = recNumber[0]
            imaginario = recNumber[1]
        else:
            # entry.get()    
            real = float(entries[0][j].get())
            imaginario = float(entries[0][j+1].get())
        numeros.append([real, imaginario])
    Diference = Subtract(numeros)
    DiferencePol = ParseToPol(Diference[0], Diference[1])
    radios[2].set('P')
    for i in [0,1]:
        entries[1][i].delete(0, t.END)
        entries[1][i].insert(0, DiferencePol[i])
    
# when timesButton is clicked
def TimesButtonClk(entries, radios):
    numeros = []
    for entry in entries[0]:
        if(entry.get()==''):
            return
    for i, j in zip([0,1],[0,2]):
        if(radios[i].get()=='R'):         
            polNumber = ParseToPol(float(entries[0][j].get()), float(entries[0][j+1].get()))   
            z = polNumber[0]
            teta = polNumber[1]
        else:
            # entry.get()    
            z = float(entries[0][j].get())
            teta = float(entries[0][j+1].get())
        numeros.append([z, teta])
    Product = Multiply(numeros)
    radios[2].set('P')
    for i in [0,1]:
        entries[1][i].delete(0, t.END)
        entries[1][i].insert(0, Product[i])

# when DivideButton is clicked
def DivideButtonClk(entries, radios):
    numeros = []
    for entry in entries[0]:
        if(entry.get()==''):
            return
    for i, j in zip([0,1],[0,2]):
        if(radios[i].get()=='R'):         
            polNumber = ParseToPol(float(entries[0][j].get()), float(entries[0][j+1].get()))   
            z = polNumber[0]
            teta = polNumber[1]
        else:
            # entry.get()    
            z = float(entries[0][j].get())
            teta = float(entries[0][j+1].get())
        numeros.append([z, teta])
    Product = Divide(numeros)
    radios[2].set('P')
    for i in [0,1]:
        entries[1][i].delete(0, t.END)
        entries[1][i].insert(0, Product[i])

