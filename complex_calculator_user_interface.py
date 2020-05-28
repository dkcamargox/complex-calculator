import tkinter as t
import os
import complex_calculator_functionalities as functs

def create_GUI():
    app = t.Tk()
    app.configure(bg="#c8d86d")
    app.geometry('280x285')
    app.title('Complex Calculator')
    icon = './assets/favicon16.png'
    img_icon = t.PhotoImage(file=os.path.join(icon))
    app.tk.call('wm', 'iconphoto', app._w, img_icon)

    # Entries for the complex number 

    EntryR1 = t.Entry(app, border=0)
    EntryC1 = t.Entry(app, border=0)

    EntryR2 = t.Entry(app, border=0)
    EntryC2 = t.Entry(app, border=0)

    EntryRA = t.Entry(app, border=0)
    EntryCA = t.Entry(app, border=0)

    # Entries List
    entriesInput = []
    entriesOutput = []
    entriesList = []
    entriesInput.append(EntryR1)
    entriesInput.append(EntryC1)
    entriesInput.append(EntryR2)
    entriesInput.append(EntryC2)
    entriesOutput.append(EntryRA)
    entriesOutput.append(EntryCA)
    entriesList.append(entriesInput)
    entriesList.append(entriesOutput)

    # Radios for Pol or Rec z1

    PorRZ1 = t.StringVar(value='P')
    CheckRecZ1 = t.Radiobutton(app, var=PorRZ1, value='R', text='Rectangular', bg="#c8d86d", font=('Roboto', 10))
    CheckPolZ1 = t.Radiobutton(app, var=PorRZ1, value='P', text='Polar', bg="#c8d86d", font=('Roboto', 10))

    # Radios for Pol or Rec z2

    PorRZ2 = t.StringVar(value='P')
    CheckRecZ2 = t.Radiobutton(app, var=PorRZ2, value='R', text='Rectangular', bg="#c8d86d", font=('Roboto', 10))
    CheckPolZ2 = t.Radiobutton(app, var=PorRZ2, value='P', text='Polar', bg="#c8d86d", font=('Roboto', 10))

    # Radios for Pol or Rec zA

    PorRZA = t.StringVar(value='P')
    CheckRecZA = t.Radiobutton(app, var=PorRZA, value='R', text='Rectangular', bg="#c8d86d", font=('Roboto', 10))
    CheckPolZA = t.Radiobutton(app, var=PorRZA, value='P', text='Polar', bg="#c8d86d", font=('Roboto', 10))
    
    CheckRecZA['command'] = lambda: functs.AnswerRadioButtonRec(EntryRA, EntryCA)
    CheckPolZA['command'] = lambda: functs.AnswerRadioButtonPol(EntryRA, EntryCA)

    radiosList = []

    radiosList.append(PorRZ1)
    radiosList.append(PorRZ2)
    radiosList.append(PorRZA)
    # Buttons + - * /

    widthButton = 5

    PlusButton = t.Button(app, text='+', width=widthButton, bg="#FFF", border=0)
    MinusButton = t.Button(app, text='-', width=widthButton, bg="#FFF", border=0)
    TimesButton = t.Button(app, text='*', width=widthButton, bg="#FFF", border=0)
    DivideButton = t.Button(app, text='/', width=widthButton, bg="#FFF", border=0)

    PlusButton['command'] = lambda: functs.PlusButtonClk(entriesList, radiosList)
    MinusButton['command'] = lambda: functs.MinusButtonClk(entriesList, radiosList)
    TimesButton['command'] = lambda: functs.TimesButtonClk(entriesList, radiosList)
    DivideButton['command'] = lambda: functs.DivideButtonClk(entriesList, radiosList)


    # Labels

    LabelZ1 = t.Label(app, text='Z1', bg="#c8d86d", font=('Roboto', 10))
    LabelZ2 = t.Label(app, text='Z2', bg="#c8d86d", font=('Roboto', 10))
    LabelZA = t.Label(app, text='Answer', bg="#c8d86d", font=('Roboto', 10))

    # consts for placing

    PlaceYEntries = 25
    PlaceYCRadios = 22
    FirstColumnx = 12
    SecondColumnx = 162
    PlaceYButtons = 170
    PlaceXButtons = 50




    # PLacing the Entriesz1

    EntryR1.place(x=FirstColumnx, y=PlaceYEntries*1)
    EntryC1.place(x=FirstColumnx, y=PlaceYEntries*2)

    # Placing the checkPol and checkRec z1

    CheckRecZ1.place(x=SecondColumnx, y=PlaceYCRadios*1)
    CheckPolZ1.place(x=SecondColumnx, y=PlaceYCRadios*2)

    # PLacing the Entriesz2

    EntryR2.place(x=FirstColumnx, y=PlaceYEntries*4)
    EntryC2.place(x=FirstColumnx, y=PlaceYEntries*5)

    # Placing the checkPol and checkRec z2
    CheckRecZ2.place(x=SecondColumnx, y=PlaceYCRadios*4.5)
    CheckPolZ2.place(x=SecondColumnx, y=PlaceYCRadios*5.5)

    # Placing the Buttons

    PlusButton.place(x=PlaceXButtons*1, y=PlaceYButtons)
    MinusButton.place(x=PlaceXButtons*2, y=PlaceYButtons)
    TimesButton.place(x=PlaceXButtons*3, y=PlaceYButtons)
    DivideButton.place(x=PlaceXButtons*4, y=PlaceYButtons)

    # Placing Answer

    EntryRA.place(x=FirstColumnx, y=PlaceYEntries*9)
    EntryCA.place(x=FirstColumnx, y=PlaceYEntries*10)

    # Placing the checkPol and checkRec for answer

    CheckRecZA.place(x=SecondColumnx, y=PlaceYCRadios*10)
    CheckPolZA.place(x=SecondColumnx, y=PlaceYCRadios*11)
    # Placing the Labels

    LabelZ1.place(x=FirstColumnx, y=PlaceYEntries*0)
    LabelZ2.place(x=FirstColumnx, y=PlaceYEntries*3)
    LabelZA.place(x=FirstColumnx, y=PlaceYEntries*8)
    app.mainloop()

