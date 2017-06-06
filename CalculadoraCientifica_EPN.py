#eval() and exec() funciones predefinidas
#v1=Toplevel(root) Ventana Hija #v1.withdraw()  # oculta v1
#https://answers.microsoft.com/es-es/windows/forum/windows_7-windows_programs/funcion-de-los-botones-ms-m-m-mr-mc-ce-y-c-de-la/5caaf4b2-385a-e011-8dfc-68b599b31bf5
#=========================================================================
from distutils import command
from tkinter import *
from math import*

root = Tk()
root.config(bg = "black")#bg = "lavender"
root.geometry("443x323+280+200")#Tamaño ventada + Coordenadas de posicion X,Y
root.maxsize(440, 320)
root.minsize(440, 320)
root.title('Calculadora Científica - EPN')
                                #PANELES
#==========================================================================================
frame = Frame(root, bd=4, relief="groove",bg = "black")#gray, dark red, black
frame.pack(fill=BOTH, padx=5, pady=5) #side = BOTTOM

calTop = Frame(frame, bd=4, relief="groove",bg = "black")
calTop.pack(fill=BOTH, padx=5, pady=5)

calLeft = Frame(frame, bd=4, width=500, height=300, relief="groove",bg = "black")
calLeft.pack(fill=BOTH, padx=5, pady=5, ipadx=1, ipady=1, side = LEFT)

calRight = Frame(frame, bd=4, width=500, height=300, relief="groove",bg = "black")
calRight.pack(fill=BOTH, padx=5, pady=5, ipadx=1, ipady=1,side = RIGHT)
#==========================================================================================

operador = ''
text_Input = StringVar()
p = 0
validar = False
evaluarFun = False
validarMemoria = False
memoria = ''

def btnClick(tecla):
    global operador
    global validar
    if validar:
        if tecla != '+' and tecla != '-' and tecla != '*' and tecla != '/'\
                and tecla != '**2' and tecla != '**3':
            btnClearDisplay()
    operador += str(tecla)#Forma una cadena de caracteres
    text_Input.set(operador)
    validar = False


def btnClearDisplay():
    global operador
    operador = ''
    text_Input.set('')



#==========================================================================================
                                #FUNCIONES ALTERNATIVAS
#==========================================================================================

def btnEliminarChar():
    global operador
    if operador !='':
        operador = operador.rstrip(operador[-1])#validar
        text_Input.set(operador)

def btnParentesis(paren):
    global p
    global operador
    p = operador.count('(')
    if paren=='(':
        btnClick('(')
        p += 1
    else:
        if p > operador.count(')'):
            btnClick(')')
            p -= 1

def btnFactorial():
    global operador
    try:
        aux = int(operador)
        operador +='!'
        text_Input.set(operador)
        operador =str(factorial(aux))
    except SyntaxError:
        text_Input.set("Syntax Error")
        operador = ''
    except ValueError:
        text_Input.set("Value Error")
        operador = ''


def btnFunTrigonometrica(tecla):
    global evaluarFun
    btnClick(tecla)
    evaluarFun=True

def btnPorcentaje(tecla):
    global operador
    global validar
    try:
        aux = int(operador)/100
        operador -= str(tecla)
        text_I
        














#==========================================================================================
#==========================================================================================
def btnResultado():
    global validar
    global evaluarFun
    validar = True
    try:
        global operador
        if operador == "":
            btnClearDisplay()
        else:
            print(evaluarFun)
            npa = operador.count('(')
            npc = operador.count(')')
            np = npa-npc
            if np !=0:
                if evaluarFun == False:
                    char = '*('
                    operador = operador.split('(')
                    operador = char.join(operador)
                    if operador[0] == '*':
                        operador = operador.lstrip(operador[0])
                    for i in range(np):
                        operador +=')'
                else:
                    for i in range(np):
                        operador +=')'
            resultado = str(eval(operador))
            if resultado == "()":
                resultado = ""
            text_Input.set(resultado)
            operador = resultado
            evaluarFun = False

    except ZeroDivisionError:
        text_Input.set("Error.!!No Se Puede Dividir Entre Cero...")
        operador = ''
    except SyntaxError:
        text_Input.set("Syntax Error")
        operador = ''
    except TypeError:
        text_Input.set("Type Error")
        operador = ''
    except ValueError:
        text_Input.set("Mathematical Error")
        operador = ''
    except Exception:
        text_Input.set("Error")
        operador = ''



#==========================================================================================
                                #BOTONES
#==========================================================================================
#DISPLAY
txt_Display = Entry(calTop, font=('arial',14,'bold'), textvariable=text_Input, bd=15, insertwidth=4,
                    state = DISABLED, width=34, justify=RIGHT).grid(columnspan=4)
#BOTONES NUMEROS
btn = Button(calLeft, bd=10, text='7', width=2, command=lambda: btnClick('7')).grid(row=0, column=0)
btn = Button(calLeft, bd=10, text='8', width=2, command=lambda: btnClick('8')).grid(row=0, column=1)
btn = Button(calLeft, bd=10, text='9', width=2, command=lambda: btnClick('9')).grid(row=0, column=2)
btn = Button(calLeft, bd=10, text='4', width=2, command=lambda: btnClick('4')).grid(row=1, column=0)
btn = Button(calLeft, bd=10, text='5', width=2, command=lambda: btnClick('5')).grid(row=1, column=1)
btn = Button(calLeft, bd=10, text='6', width=2, command=lambda: btnClick('6')).grid(row=1, column=2)
btn = Button(calLeft, bd=10, text='3', width=2, command=lambda: btnClick('3')).grid(row=2, column=0)
btn = Button(calLeft, bd=10, text='2', width=2, command=lambda: btnClick('2')).grid(row=2, column=1)
btn = Button(calLeft, bd=10, text='1', width=2, command=lambda: btnClick('1')).grid(row=2, column=2)
btn = Button(calLeft, bd=10, text='0', width=2, command=lambda: btnClick('0')).grid(row=3, column=0)
btn = Button(calLeft, bd=10, text='.', width=2, command=lambda: btnClick('.')).grid(row=3, column=1)
btn = Button(calLeft, bd=10, text='√', width=2, command=lambda: btnClick('sqrt(')).grid(row=3, column=2)
#BOTONES OPERADORES
btn = Button(calLeft, bd=10, text='/', width=2, command=lambda: btnClick('/')).grid(row=0, column=3)
btn = Button(calLeft, bd=10, text='*', width=2, command=lambda: btnClick('*')).grid(row=1, column=3)
btn = Button(calLeft, bd=10, text='-', width=2, command=lambda: btnClick('-')).grid(row=2, column=3)
btn = Button(calLeft, bd=10, text='+', width=2, command=lambda: btnClick('+')).grid(row=3, column=3)
btn = Button(calLeft, bd=10, text='⌫', width=2, command=lambda: btnEliminarChar()).grid(row=4, column=0)
btn = Button(calLeft, bd=10, text='CE', width=2, command=lambda: btnEliminarChar()).grid(row=4, column=1)
btn = Button(calLeft, bd=10, text='C', width=2, command=lambda: btnClearDisplay()).grid(row=4, column=2)
btn = Button(calLeft, bd=10, text='=', width=2, command=lambda: btnResultado()).grid(row=4, column=3)
#==========================================================================================
                                #BOTONES TRIGONOMETRICOS
#==========================================================================================
#BOTONES TRIGONOMETRICOS
btn = Button(calRight, bd=10, text='(', width=4, command=lambda: btnParentesis('(')).grid(row=0, column=0)
btn = Button(calRight, bd=10, text=')', width=4, command=lambda: btnParentesis(')')).grid(row=0, column=1)
btn = Button(calRight, bd=10, text='%', width=4, command=lambda: btnPorcentaje('%')).grid(row=0, column=2)

btn = Button(calRight, bd=10, text='Sin', width=4, command=lambda: btnFunTrigonometrica('sin(radians(')).grid(row=1, column=0)
btn = Button(calRight, bd=10, text='aSin', width=4, command=lambda: btnFunTrigonometrica('degrees(asin(')).grid(row=1, column=1)
btn = Button(calRight, bd=10, text='X²', width=4, command=lambda: btnClick('**2')).grid(row=1, column=2)

btn = Button(calRight, bd=10, text='Cos', width=4, command=lambda: btnFunTrigonometrica('cos(radians(')).grid(row=2, column=0)
btn = Button(calRight, bd=10, text='aCos', width=4, command=lambda: btnFunTrigonometrica('degrees(acos(')).grid(row=2, column=1)
btn = Button(calRight, bd=10, text='X³', width=4, command=lambda: btnClick('**3')).grid(row=2, column=2)

btn = Button(calRight, bd=10, text='Tan', width=4, command=lambda: btnFunTrigonometrica('tan(radians(')).grid(row=3, column=0)
btn = Button(calRight, bd=10, text='aTan', width=4, command=lambda: btnFunTrigonometrica('degrees(atan(')).grid(row=3, column=1)
btn = Button(calRight, bd=10, text='X^y', width=4, command=lambda: btnClick('**')).grid(row=3, column=2)

#BOTONES CONFIG
btn = Button(calRight, bd=10, text='MC', width=4, command=lambda: btnMemoria('MC')).grid(row=0, column=3)
btn = Button(calRight, bd=10, text='MR', width=4, command=lambda: btnMemoria('MR')).grid(row=1, column=3)
btn = Button(calRight, bd=10, text='MS', width=4, command=lambda: btnMemoria('MS')).grid(row=2, column=3)
btn = Button(calRight, bd=10, text='M+', width=4, command=lambda: btnMemoria('M+')).grid(row=3, column=3)

btn = Button(calRight, bd=10, text='Log', width=4, command=lambda: btnFunTrigonometrica('log10(')).grid(row=4, column=0)
btn = Button(calRight, bd=10, text='π', command=lambda: btnClick(pi), width=4).grid(row=4, column=1)
btn = Button(calRight, bd=10, text='n!', width=4, command=lambda: btnFactorial()).grid(row=4, column=2)
btn = Button(calRight, bd=10, text='M-', width=4, command=lambda: btnMemoria('M-')).grid(row=4, column=3)




root.mainloop()












#LAS FUNCIONES SEN, COS, TAN, YA SE CALCULAN HAY QUE VALIDAR CUANDO CADA FUNCION TOMA VALOR DE
#0,90,180,270,360 PARA CADA UNA DE ELLAS, Y ADEMAS FALTA LA VALIDADCION DE QUE DESPUES DE INGRESAR
#UNA FUNCION TRIGONOMETRICA Y QUE DE EL RESULTADO, AL MOMETNO DE APLASTAR UN NUMERO NO MARQUE NUEVAMENETE LA FUNCION
#PARA QUE ENTIENDAN MEJOR PRIMERO EJECUTEN UNA FUNCION TRIGONOMETRICA, LUEGO UNA SUMA Y VERAN LO QUE PASA


