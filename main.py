from tkinter import *
from tkinter.font import Font

def decimal_to_binary(decimal):
  bin_list = []
  while decimal != 0:
      bin = decimal % 2
      bin_list.insert(0,bin) 
      decimal = decimal // 2
  text_binary = Label(janela, font=main_font, fg="#090019",bg='white',text='')
  text_binary['text'] = bin_list
  text_binary.place(width=435, height=80, x=25, y=383 )
  return bin_list


def binary_to_decimal(binary):
  dec_list = []
  sum_list = []
  prohibit_numbers = [2,3,4,5,6,7,8,9]
  while binary > 0:
    binary_resto = binary % 10
    binary = binary // 10
    dec_list.insert(0,binary_resto)
    binary_convert = (binary_resto*2**(len(dec_list)-1))
    sum_list.insert(0, binary_convert)
  if any(item in prohibit_numbers for item in dec_list):
    binary = int(input("\nO número digitado não corresponde a um número binário! Digite novamente\n >>> "))
    binary = binary_to_decimal(binary)
    return binary
    
  else:
    text_decimal= Label(
    janela,font=main_font,
    fg="#090019",
    bg='white',
    text='')
    text_decimal['text'] = sum(sum_list)
    text_decimal.place(width=435, height=80, x=25, y=383 )
    return sum(sum_list)

def decimal_to_octal(decimal):
  octal_list = []
  while decimal != 0:
      octal = decimal % 8
      octal_list.insert(0,octal) 
      decimal = decimal // 8
  text_octal = Label(janela, font=main_font, fg="#090019",bg='white',text='')
  text_octal['text'] = octal_list
  text_octal.place(width=435, height=80, x=25, y=383 )
  return octal_list

def octal_to_decimal(octal):
  dec_list = []
  sum_list = []
  prohibit_numbers = [8,9] 
  while octal > 0:
    octal_resto = octal % 10   
    octal = octal // 10
    dec_list.insert(0,octal_resto)
    octal_convert= (octal_resto*(8**(len(dec_list)-1)))
    sum_list.insert(0, octal_convert)
  if any(item in prohibit_numbers for item in dec_list):
    octal = int(input("\nO número digitado não corresponde a um número octal! Digite novamente\n >>> "))
    octal = octal_to_decimal(octal)
    return octal
  else:
    text_decimal= Label(
    janela,font=main_font,
    fg="#090019",
    bg='white',
    text='')
    text_decimal['text'] = sum(sum_list)
    text_decimal.place(width=435, height=80, x=25, y=383 )
    return sum(sum_list)


def decimal_to_hexadecimal(decimal):
  hexa_list = []
  while decimal != 0:
      hexa = decimal % 16
      hexa_list.insert(0,hexa) 
      decimal = decimal // 16
      replacements = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
      replacer = replacements.get
  hexa = [replacer(n, n) for n in hexa_list]
  text_hexadecimal = Label(janela,font=main_font,fg="#090019",bg='white',text='')
  text_hexadecimal['text'] = hexa
  text_hexadecimal.place(width=435, height=80, x=25, y=383 )
  return hexa
  
def hexadecimal_to_decimal(hexa):
  hexa_original = hexa
  hexa_list = []
  sum_list = []
  len_hexa = len(hexa)
  while len_hexa > 0:
    hexa_list.insert(0,hexa[len_hexa-1])
    len_hexa -= 1
  replacements = {'A':10, 'B':11 , 'C':12, 'D':13, 'E':14, 'F':15, 'a':10, 'b':11 , 'c':12, 'd':13, 'e':14, 'f':15}
  replacer = replacements.get
  hexa = [replacer(n, n) for n in hexa_list]
  hexa = [int(i) for i in hexa]
  len_hexa = len(hexa_original)
  hexa.reverse()
  while len_hexa > 0:
    hexa_convert = hexa[len_hexa-1] * (16 **(len_hexa-1))
    sum_list.insert(0,hexa_convert)
    len_hexa -= 1
  decimal = sum(sum_list)
  text_decimal = Label(janela,font=main_font,fg="#090019",bg='white',text='')
  text_decimal['text'] = decimal
  text_decimal.place(width=435, height=80, x=25, y=383 )
  return decimal
  


    
def clear_frame():
    # destroy all widgets from frame
    for widget in janela.winfo_children():
       widget.destroy()
def decimal_to_binary_tkinter():
  text_decimal_to_binary = Label(janela ,highlightthickness=0,borderwidth = 0,image = img_dec_to_bin_bg)
  text_decimal_to_binary.grid()
  
  num_decimal = Entry(janela, justify=CENTER,font=main_font, fg='#090019')
  num_decimal.place(width=424, height=90, x=35, y=125)

  button_convert = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_convert,command=lambda: decimal_to_binary(int(num_decimal.get())))
  button_convert.place(width=330, height=57, x=75, y=268 )

  
  button_back = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_back,command=lambda: [clear_frame(),main_janela()])
  button_back.place(width=40, height=40, x=230, y=495 )




  
def binary_to_decimal_tkinter():
  text_binary_to_decimal = Label(janela ,highlightthickness=0,borderwidth = 0,image = img_bin_to_dec_bg)
  text_binary_to_decimal.grid()
  
  num_binary = Entry(janela, justify=CENTER,font=main_font, fg='#090019')
  num_binary.place(width=424, height=90, x=35, y=125)

  button_convert = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_convert,command=lambda: binary_to_decimal(int(num_binary.get())))
  button_convert.place(width=330, height=57, x=75, y=268 )

  button_back = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_back,command=lambda: [clear_frame(),main_janela()])
  button_back.place(width=40, height=40, x=230, y=495 )



def decimal_to_octal_tkinter():
  text_decimal_to_octal = Label(janela ,highlightthickness=0,borderwidth = 0,image = img_dec_to_oct_bg)
  text_decimal_to_octal.grid()
  
  num_decimal = Entry(janela, justify=CENTER,font=main_font, fg='#090019')
  num_decimal .place(width=424, height=90, x=35, y=125)

  button_convert = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_convert,command=lambda: decimal_to_octal(int(num_decimal.get())))
  button_convert.place(width=330, height=57, x=75, y=268 )

  button_back = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_back,command=lambda: [clear_frame(),main_janela()])
  button_back.place(width=40, height=40, x=230, y=495 )
  
def octal_to_decimal_tkinter():
  text_octal_to_decimal = Label(janela ,highlightthickness=0,borderwidth = 0,image = img_oct_to_dec_bg)
  text_octal_to_decimal.grid()
  
  num_octal = Entry(janela, justify=CENTER,font=main_font, fg='#090019')
  num_octal.place(width=424, height=90, x=35, y=125)

  button_convert = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_convert,command=lambda: octal_to_decimal(int(num_octal.get())))
  button_convert.place(width=330, height=57, x=75, y=268 )

  button_back = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_back,command=lambda: [clear_frame(),main_janela()])
  button_back.place(width=40, height=40, x=230, y=495 )
  
def decimal_to_hexadecimal_tkinter():
  text_decimal_to_hexa = Label(janela ,highlightthickness=0,borderwidth = 0,image = img_dec_to_hex_bg)
  text_decimal_to_hexa.grid()
  
  num_decimal = Entry(janela, justify=CENTER,font=main_font, fg='#090019')
  num_decimal .place(width=424, height=90, x=35, y=125)

  button_convert = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_convert,command=lambda: decimal_to_hexadecimal(int(num_decimal.get())))
  button_convert.place(width=330, height=57, x=75, y=268 )
  button_back = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_back,command=lambda: [clear_frame(),main_janela()])
  button_back.place(width=40, height=40, x=230, y=495 )
  
def hexadecimal_to_decimal_tkinter():
  text_hexa_to_decimal = Label(janela ,highlightthickness=0,borderwidth = 0,image = img_hex_to_dec_bg)
  text_hexa_to_decimal.grid()
  
  num_decimal = Entry(janela, justify=CENTER,font=main_font, fg='#090019')
  num_decimal.place(width=424, height=90, x=35, y=125)

  button_convert = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_convert,command=lambda: hexadecimal_to_decimal(num_decimal.get()))
  button_convert.place(width=330, height=57, x=75, y=268 )

  button_back = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_back,command=lambda: [clear_frame(),main_janela()])
  button_back.place(width=40, height=40, x=230, y=495 )


janela = Tk()
janela.title('Conversor de Sistemas Numéricos')
janela.geometry('490x560+610+153')
photo = PhotoImage(file = 'icones//icon.png')
janela.wm_iconphoto(False, photo)
janela.resizable(0,0)



# images
img_main_bg = PhotoImage(file='img//main.png')
img_button_dec_to_bin = PhotoImage(file='img//button//dec_to_bin_button.png')
img_button_bin_to_dec = PhotoImage(file='img//button//bin_to_dec_button.png')
img_button_dec_to_oct = PhotoImage(file='img//button//dec_to_oct_button.png')
img_button_oct_to_dec = PhotoImage(file='img//button//oct_to_dec_button.png')
img_button_dec_to_hex = PhotoImage(file='img//button//dec_to_hex_button.png')
img_button_hex_to_dec = PhotoImage(file='img//button//hex_to_dec_button.png')
img_button_convert = PhotoImage(file='img//button//convert_button.png')
img_button_back = PhotoImage(file='img//button//back_button.png')

img_dec_to_bin_bg = PhotoImage(file='img//bg//dec_to_bin_bg.png')
img_bin_to_dec_bg = PhotoImage(file='img//bg//bin_to_dec_bg.png')
img_dec_to_oct_bg = PhotoImage(file='img//bg//dec_to_oct_bg.png')
img_oct_to_dec_bg = PhotoImage(file='img//bg//oct_to_dec_bg.png')
img_dec_to_hex_bg = PhotoImage(file='img//bg//dec_to_hex_bg.png')
img_hex_to_dec_bg = PhotoImage(file='img//bg//hex_to_dec_bg.png')

def main_janela():

  main_bg = Label(janela, image = img_main_bg)
  main_bg.grid()
  
  img_button1 = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_dec_to_bin,command=lambda: [clear_frame(),decimal_to_binary_tkinter()])
  img_button1.place(width=457, height=59, x=16, y=82 )

  img_button2 = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_bin_to_dec,command=lambda: [clear_frame(),binary_to_decimal_tkinter()])
  img_button2.place(width=457, height=59, x=16, y=155 )

  img_button3 = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_dec_to_oct,command=lambda: [clear_frame(),decimal_to_octal_tkinter()])
  img_button3.place(width=457, height=59, x=16, y=228 )

  img_button4 = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_oct_to_dec,command=lambda: [clear_frame(),octal_to_decimal_tkinter()])
  img_button4.place(width=457, height=59, x=16, y=301 )

  img_button5 = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_dec_to_hex,command=lambda: [clear_frame(),decimal_to_hexadecimal_tkinter()])
  img_button5.place(width=457, height=59, x=16, y=374 )

  img_button6 = Button(janela,highlightthickness=0,borderwidth = 0,image=img_button_hex_to_dec,command=lambda: [clear_frame(),hexadecimal_to_decimal_tkinter()])
  img_button6.place(width=457, height=59, x=16, y=447 )




main_font = Font(
  family='Arial', 
  size= 12, 
  weight= 'normal', 
  slant='roman',
  underline= 0, 
  overstrike= 0)

main_janela()
janela.mainloop()

