from justifytext import justify
from PIL import Image, ImageDraw, ImageFont
print('a')
pic=Image.open('comunicadoASSINADO.png')
draw= ImageDraw.Draw(pic)
font=ImageFont.truetype('seguibl', 43)
##Paragrafo
a=input('Referente ao mês:')
b=input('Do ano:')
ano=b
c=input('Data (Exemplo: 01 de março de 2035): ')
paragrafo=('É REQUISITADO DO SR.HIPOTÉTICO JOSÉ DE MENTES, RESPONSÁVEL DO SETOR Y DA  EMPRESA X, A QUANTIA DE  R$ 914,00 (NOVECENTOS E QUATORZE REAIS), REFERENTE A TAXA DO MÊS DE {} DE {} DO SERVIÇO DE MANUTENÇÃO DO ESCRITÓRIO 9 DO PRÉDIO, RUA HIPOTÉTICA, N° 227, LIVRAMENTO, VITÓRIA-PE.'.format(a.upper(), b.upper()))
#
x=justify(paragrafo, 57)
#
listaFrases=[]
for i in x:
    listaFrases.append(i)
# EU NÃO SEI MAIS OQ FZEER
# METHOD 3
#
equalz=[]
#
w0 = font.getsize(listaFrases[0])[0]
equalz.append(w0)
#
w1 = font.getsize(listaFrases[1])[0]
equalz.append(w1)
#
w2 = font.getsize(listaFrases[2])[0]
equalz.append(w2)
#
w3 = font.getsize(listaFrases[3])[0]
#
maior=0
for i in equalz:
    if i>=maior:
        maior=i
equalz.remove(maior)
#
for i in equalz:
    b=maior-i
    c2=round(b/12)
    if i==w0:
        counter=0
        #SO´NUM CANTO???
        while  counter<c2:
            FRASE=listaFrases[0]
            number=FRASE.find(' ')
            listaFrases[0]=FRASE[:number]+' '+FRASE[number:]
            counter+=1
            #
            number=FRASE.rfind(' ')
            listaFrases[0]=FRASE[:number]+' '+FRASE[number:]
            counter+=1
        #
    if i==w1:
        print('ha gotem')
        counter=0
        #SO´NUM CANTO???
        while  counter<c2:
            FRASE=listaFrases[1]
            #
            number1=FRASE.find(' ')
            listaFrases[1]=FRASE[:number1]+' '+FRASE[number1:]
            counter+=1.5
            #
            FRASE=listaFrases[1]
            number2=FRASE.find('REF')
            listaFrases[1]=FRASE[:number2-1]+' '+FRASE[number2-1:]
            counter+=1.5
            #
        #
    if i==w2:
        counter=0
        #SO´NUM CANTO???
        while  counter<c2:
            FRASE=listaFrases[2]
            number=FRASE.find(' ')
            listaFrases[2]=FRASE[:number]+' '+FRASE[number:]
            counter+=1
            #
            number=FRASE.rfind(' ')
            listaFrases[2]=FRASE[:number]+' '+FRASE[number:]
            counter+=1
#
draw.text((90 ,198), listaFrases[0], font=font, fill='black')
#
draw.text((90 ,248), listaFrases[1], font=font, fill='black')
#
if listaFrases[2] in listaFrases:
    draw.text((90 ,298), listaFrases[2], font=font, fill='black')
#
if listaFrases[3] in listaFrases:
    draw.text((90 ,348), listaFrases[3], font=font, fill='black')
#
if listaFrases[4] in listaFrases:
    draw.text((90 ,398), listaFrases[4], font=font, fill='black')

draw.text((90 ,516), (('VITÓRIA-PE, {}'.format(c.upper()))+'.'), font=font, fill='black')
#
pic.show()
result=('Comunicado Mensal de Manutenção- {} - {}.png'.format(a.upper(), ano))
pic.save(result)
