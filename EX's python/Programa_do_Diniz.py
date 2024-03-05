#Linguagens de programação: Projeto
#Cálculo área/volume de figuras, ou conversão de medidas de comprimento

#Bibliotecas
import math as m
#Funções
def valid(min,max,msg,msgerro,tp = 0):
  import math as m
  while True:
    if min == "s":
      min = -m.inf
    if max == "s":
      max = m.inf
    if tp == 0:
      try:
        x = float(input(msg))
      except:
        print(msgerro)
      else:
        if x >= min and x <= max:
          return x
        else:
          print(msgerro)
    else:
      try:
        x = int(input(msg))
      except:
          print(msgerro)
      else:
        if x >= min and x <= max:
          return x
        else:
          print(msgerro)

def convert(n,u1,u2 = 4,d = 1): #Converter medidas
  if u1 == 1:
    b = 3
  elif u1 == 2:
    b = 2
  elif u1 == 3:
    b = 1
  elif u1 == 4:
    b = 0
  elif u1 == 5:
    b = -1
  elif u1 == 6:
    b = -2
  else:
    b = -3
  d2 = ""
  if d == 2:
    d2 = "^2"
  elif d == 3:
    d2 = "^3"
  if u2 == 1:
    c = -3
    un = "km" + d2
  elif u2 == 2:
    c = -2
    un = "hm" + d2
  elif u2 == 3:
    c = -1
    un = "dam" + d2
  elif u2 == 4:
    c = 0
    un = "m" + d2
  elif u2 == 5:
    c = 1
    un = "dm" + d2
  elif u2 == 6:
    c = 2
    un = "cm" + d2
  else:
    c = 3
    un = "mm" + d2
  conv = n*10**(d*b + d*c)
  if notacient(conv) == "":
    print(f"\nO valor equivale a: {round(conv,14)} " + un) 
  else:
    print(f"\nO valor equivale a: {round(conv,14)} " + un, f"   {notacient(conv)} {un}")

def notacient(v): #Notação científica
  cont = 0
  while v >= 10 or v < 1:
    if v >= 10:
      cont += 1
      v = v/10
    else:
      cont -= 1
      v = v*10
  if cont == 0:
    return ""
  else:
    return f"ou   {round(v,3)} x 10^{cont}"
  
#MENU
while True:
  op = valid(0,3,"Selecione a opção desejada:\n 0 - Encerrar Programa\n 1 - Conversão de Medidas\n 2 - Cálculo Área\n 3 - Cálculo Volume\n: ", "Se è Burro né irmão?",1)
  if op == 0:
    break
  elif op == 1:           #Conversão de medidas     
    while True:
      print("\n(1) CONVERSÃO DE MEDIDAS")
      d = valid(0,3,"Selecione a dimensão dos valores desejados:\n 0 - Voltar\n 1 - Comprimento (m)\n 2 - Área (m^2)\n 3 - Volume (m^3)\n: ","Opção inválida",1)
      if d == 0:
        break
      d2 = ""
      Selec = "Comprimento"
      if d == 2:
        d2 ="^2"
        Selec = "Área"
      elif d == 3:
        d2 ="^3"
        Selec = "Volume"
      while True:
        print(f"\n(1)>({d}) CONVERSÃO DE MEDIDAS: {Selec}")
        numero = valid("s","s","0 = Voltar\nInsira o valor a ser convertido: ", "Valor Inválido")
        if numero == 0:
          break
        while True:
          u1 = valid(0,7,f"\nEscolha a unidade de medida do valor a ser convertido:\n 0 - Voltar\n 1 - km{d2}\n 2 - hm{d2}\n 3 - dam{d2}\n 4 - m{d2}\n 5 - dm{d2}\n 6 - cm{d2}\n 7 - mm{d2}\n: ","Opção Inválida",1)
          if u1 == 0:
            break
          while True:
            u2 = valid(0,7,f"\nEscolha a unidade final desejada para a conversão:\n 0 - Voltar\n 1 - km{d2}\n 2 - hm{d2}\n 3 - dam{d2}\n 4 - m{d2}\n 5 - dm{d2}\n 6 - cm{d2}\n 7 - mm{d2}\n: ","Opção Inválida",1)
            break
          if u2 != 0:
            break
        if u1 == 0:
          continue
        k = convert(numero,u1,u2,d)         #Conversão de medidas-
#########################################################################################
  elif op == 2:           #Cálculo de Área
    while True:
      print("\n(2) CÁLCULO ÁREA") 
      op2 = valid(0,7,"Selecione o formato da figura:\n 0 - Voltar\n 1 - Triângulo\n 2 - Retângulos\n 3 - Losango\n 4 - Trapézio\n 5 - Paralelogramos\n 6 - Círculo\n 7 - Polígonos Equiláteros\n: ","Opção Inválida",1)
      if op2 == 0:
        break
      elif op2 == 1: #Triângulo
        while True:
          base = valid(0,"s",f"\n(2)>({op2}) CÁLCULO ÁREA: Triângulo\n0 = Voltar\nInsira o valor da base do triângulo: ", "Valor inválido")
          if base == 0:
            break
          while True:
            altura = valid(0,"s","\n0 = Voltar\nInsira o valor da altura do triângulo: ", "Valor inválido")
            if altura == 0:
              break
            area1 = (base * altura)/2
            print(f"\nÁrea = {round(area1,6)}   {notacient(area1)}")
            while True:
              convarea1 = valid(0,2,f"\nDigite a opção desejada:\n 0 - Voltar\n 1 - Continuar\n 2 - Converter resultado\n: ","Opção Inválida",1)
              if convarea1 == 0:
                break
              elif convarea1 == 1:
                break
              elif convarea1 == 2:
                while True:
                  unid_area_i1 = valid(0,7,f"\nEscolha a unidade de medida do valor a ser convertido:\n 0 - Voltar\n 1 - km^2\n 2 - hm^2\n 3 - dam^2\n 4 - m^2\n 5 - dm^2\n 6 - cm^2\n 7 - mm^2\n: ","Opção Inválida",1)
                  if unid_area_i1 == 0:
                    break
                  unid_area_f1 = valid(0,7,f"\nEscolha a unidade final desejada para a conversão:\n 0 - Voltar\n 1 - km^2\n 2 - hm^2\n 3 - dam^2\n 4 - m^2\n 5 - dm^2\n 6 - cm^2\n 7 - mm^2\n: ","Opção Inválida",1)
                  if unid_area_f1 == 0:
                    continue
                  convert(area1,unid_area_i1,unid_area_f1,2)
                  break 
              if unid_area_i1 == 0:
                continue
            if convarea1 == 0:
              continue
            break 
      elif op2 == 2: #Retângulos
        while True:
          lado_A = valid(0,"s",f"\n(2)>({op2}) CÁLCULO ÁREA: Retângulos\n0 = Voltar\nInsira o valor do lado A do retângulo: ", "Valor inválido")
          if lado_A == 0:
            break
          while True:
            lado_B = valid(0,"s","\n0 = Voltar\nInsira o valor do lado B do retângulo: ", "Valor inválido")
            if lado_B == 0:
              break
            area2 = lado_A * lado_B
            print(f"\nÁrea = {round(area2,6)}   {notacient(area2)}")
            while True:
              convarea2 = valid(0,2,f"\nDigite a opção desejada:\n 0 - Voltar\n 1 - Continuar\n 2 - Converter resultado\n: ","Opção Inválida",1)
              if convarea2 == 0:
                break
              elif convarea2 == 1:
                break
              elif convarea2 == 2:
                while True:
                  unid_area_i2 = valid(0,7,f"\nEscolha a unidade de medida do valor a ser convertido:\n 0 - Voltar\n 1 - km^2\n 2 - hm^2\n 3 - dam^2\n 4 - m^2\n 5 - dm^2\n 6 - cm^2\n 7 - mm^2\n: ","Opção Inválida",1)
                  if unid_area_i2 == 0:
                    break
                  unid_area_f2 = valid(0,7,f"\nEscolha a unidade final desejada para a conversão:\n 0 - Voltar\n 1 - km^2\n 2 - hm^2\n 3 - dam^2\n 4 - m^2\n 5 - dm^2\n 6 - cm^2\n 7 - mm^2\n: ","Opção Inválida",1)
                  if unid_area_f2 == 0:
                    continue
                  convert(area2,unid_area_i2,unid_area_f2,2)
                  break 
              if unid_area_i2 == 0:
                continue
            if convarea2 == 0:
              continue
            break 
      elif op2 == 3: #Losango
        while True:
          diag_MA = valid(0,"s",f"\n(2)>({op2}) CÁLCULO ÁREA: Losango\n0 = Voltar\nInsira o valor da Diagonal Maior do losango: ", "Valor inválido")
          if diag_MA == 0:
            break
          while True:
            diag_MN = valid(0,"s","\n0 = Voltar\nInsira o valor da Diagonal Menor do losango: ", "Valor inválido")
            if diag_MN == 0:
              break
            area3 = (diag_MA * diag_MN)/2
            print(f"\nÁrea = {round(area3,6)}   {notacient(area3)}")
            while True:
              convarea3 = valid(0,2,f"\nDigite a opção desejada:\n 0 - Voltar\n 1 - Continuar\n 2 - Converter resultado\n: ","Opção Inválida",1)
              if convarea3 == 0:
                break
              elif convarea3 == 1:
                break
              elif convarea3 == 2:
                while True:
                  unid_area_i3 = valid(0,7,f"\nEscolha a unidade de medida do valor a ser convertido:\n 0 - Voltar\n 1 - km^2\n 2 - hm^2\n 3 - dam^2\n 4 - m^2\n 5 - dm^2\n 6 - cm^2\n 7 - mm^2\n: ","Opção Inválida",1)
                  if unid_area_i3 == 0:
                    break
                  unid_area_f3 = valid(0,7,f"\nEscolha a unidade final desejada para a conversão:\n 0 - Voltar\n 1 - km^2\n 2 - hm^2\n 3 - dam^2\n 4 - m^2\n 5 - dm^2\n 6 - cm^2\n 7 - mm^2\n: ","Opção Inválida",1)
                  if unid_area_f3 == 0:
                    continue
                  convert(area3,unid_area_i3,unid_area_f3,2)
                  break 
              if unid_area_i3 == 0:
                continue
            if convarea3 == 0:
              continue
            break 
      elif op2 == 4: #Trapézio
        while True:
          base_MA = valid(0,"s",f"\n(2)>({op2}) CÁLCULO ÁREA: Trapézio\n0 = Voltar\nInsira o valor da Base Maior do Trapézio: ", "Valor inválido")
          if base_MA == 0:
            break
          while True:
            base_MN = valid(0,"s","\n0 = Voltar\nInsira o valor da Base Menor do Trapézio: ", "Valor inválido")
            if base_MN == 0:
              break
            while True:
              altura4 = valid(0,"s","\n0 = Voltar\nInsira o valor da Altura do Trapézio: ", "Valor inválido")
              if altura4 == 0:
                break
              area4 = (base_MA + base_MN)*altura4/2
              print(f"\nÁrea = {round(area4,6)}   {notacient(area4)}")
              while True:
                convarea4 = valid(0,2,f"\nDigite a opção desejada:\n 0 - Voltar\n 1 - Continuar\n 2 - Converter resultado\n: ","Opção Inválida",1)
                if convarea4 == 0:
                  break
                elif convarea4 == 1:
                  break
                elif convarea4 == 2:
                  while True:
                    unid_area_i4 = valid(0,7,f"\nEscolha a unidade de medida do valor a ser convertido:\n 0 - Voltar\n 1 - km^2\n 2 - hm^2\n 3 - dam^2\n 4 - m^2\n 5 - dm^2\n 6 - cm^2\n 7 - mm^2\n: ","Opção Inválida",1)
                    if unid_area_i4 == 0:
                      break
                    unid_area_f4 = valid(0,7,f"\nEscolha a unidade final desejada para a conversão:\n 0 - Voltar\n 1 - km^2\n 2 - hm^2\n 3 - dam^2\n 4 - m^2\n 5 - dm^2\n 6 - cm^2\n 7 - mm^2\n: ","Opção Inválida",1)
                    if unid_area_f4 == 0:
                      continue
                    convert(area4,unid_area_i4,unid_area_f4,2)
                    break
                if unid_area_i4 == 0:
                  continue
              if convarea4 == 0:
                continue
              break 
            if altura4 == 0:
              continue
            break
      elif op2 == 5: #Paralelogramos
        while True:
          base5 = valid(0,"s",f"\n(2)>({op2}) CÁLCULO ÁREA: Paralelogramos\n0 = Voltar\nInsira o valor da base do Paralelogramo: ", "Valor inválido")
          if base5 == 0:
            break
          while True:
            altura5 = valid(0,"s","\n0 = Voltar\nInsira o valor da Altura do Paralelogramo: ", "Valor inválido")
            if altura5 == 0:
              break
            area5 = base5 * altura5
            print(f"\nÁrea = {round(area5,6)}   {notacient(area5)}")
            while True:
              convarea5 = valid(0,2,f"\nDigite a opção desejada:\n 0 - Voltar\n 1 - Continuar\n 2 - Converter resultado\n: ","Opção Inválida",1)
              if convarea5 == 0:
                break
              elif convarea5 == 1:
                break
              elif convarea5 == 2:
                while True:
                  unid_area_i5 = valid(0,7,f"\nEscolha a unidade de medida do valor a ser convertido:\n 0 - Voltar\n 1 - km^2\n 2 - hm^2\n 3 - dam^2\n 4 - m^2\n 5 - dm^2\n 6 - cm^2\n 7 - mm^2\n: ","Opção Inválida",1)
                  if unid_area_i5 == 0:
                    break
                  unid_area_f5 = valid(0,7,f"\nEscolha a unidade final desejada para a conversão:\n 0 - Voltar\n 1 - km^2\n 2 - hm^2\n 3 - dam^2\n 4 - m^2\n 5 - dm^2\n 6 - cm^2\n 7 - mm^2\n: ","Opção Inválida",1)
                  if unid_area_f5 == 0:
                    continue
                  convert(area5,unid_area_i5,unid_area_f5,2)
                  break 
              if unid_area_i5 == 0:
                continue
            if convarea5 == 0:
              continue
            break 
      elif op2 == 6: #Círculo
        while True:
          raio = valid(0,"s",f"\n(2)>({op2}) CÁLCULO ÁREA: Círculo\n0 = Voltar\nInsira o valor do Raio do círculo: ", "Valor inválido")
          if raio == 0:
            break
          area6 = m.pi * raio**2
          print(f"\nÁrea = {round(area6,6)}   {notacient(area6)}")
          while True:
            convarea6 = valid(0,2,f"\nDigite a opção desejada:\n 0 - Voltar\n 1 - Próximo formato\n 2 - Converter resultado\n: ","Opção Inválida",1)
            if convarea6 == 0:
              break
            elif convarea6 == 1:
              break
            elif convarea6 == 2:
              while True:
                unid_area_i6 = valid(0,7,f"\nEscolha a unidade de medida do valor a ser convertido:\n 0 - Voltar\n 1 - km^2\n 2 - hm^2\n 3 - dam^2\n 4 - m^2\n 5 - dm^2\n 6 - cm^2\n 7 - mm^2\n: ","Opção Inválida",1)
                if unid_area_i6 == 0:
                  break
                unid_area_f6 = valid(0,7,f"\nEscolha a unidade final desejada para a conversão:\n 0 - Voltar\n 1 - km^2\n 2 - hm^2\n 3 - dam^2\n 4 - m^2\n 5 - dm^2\n 6 - cm^2\n 7 - mm^2\n: ","Opção Inválida",1)
                if unid_area_f6 == 0:
                  continue
                convert(area6,unid_area_i6,unid_area_f6,2)
                break 
            if unid_area_i6 == 0:
              continue
          if convarea6 == 0:
            continue
          break 
      elif op2 == 7: #Polígonos Equiláteros
        while True:
          num_lados = valid(0,"s",f"\n(2)>({op2}) CÁLCULO ÁREA: Polígonos Equiláteros\n0 = Voltar\nInsira o número de lados do Polígono Equilátero: ", "Valor inválido",1)
          if num_lados == 1 or num_lados == 2:
            print("Valor Inválido")
            continue
          if num_lados == 0:
            break
          while True:
            lado7 = valid(0,"s","\n0 = Voltar\nInsira o valor do lado do Polígono Equilátero: ", "Valor inválido")
            if lado7 == 0:
              break
            area7 = (num_lados * lado7**2)/(4*m.tan(m.pi/num_lados))
            print(f"\nÁrea = {round(area7,6)}   {notacient(area7)}")
            while True:
              convarea7 = valid(0,2,f"\nDigite a opção desejada:\n 0 - Voltar\n 1 - Continuar\n 2 - Converter resultado\n: ","Opção Inválida",1)
              if convarea7 == 0:
                break
              elif convarea7 == 1:
                break
              elif convarea7 == 2:
                while True:
                  unid_area_i7 = valid(0,7,f"\nEscolha a unidade de medida do valor a ser convertido:\n 0 - Voltar\n 1 - km^2\n 2 - hm^2\n 3 - dam^2\n 4 - m^2\n 5 - dm^2\n 6 - cm^2\n 7 - mm^2\n: ","Opção Inválida",1)
                  if unid_area_i7 == 0:
                    break
                  unid_area_f7 = valid(0,7,f"\nEscolha a unidade final desejada para a conversão:\n 0 - Voltar\n 1 - km^2\n 2 - hm^2\n 3 - dam^2\n 4 - m^2\n 5 - dm^2\n 6 - cm^2\n 7 - mm^2\n: ","Opção Inválida",1)
                  if unid_area_f7 == 0:
                    continue
                  convert(area7,unid_area_i7,unid_area_f7,2)
                  break 
              if unid_area_i7 == 0:
                continue
            if convarea7 == 0:
              continue
            break
#########################################################################################
  elif op == 3:           #Cálculo de Volume
    while True:
      print("\n(3) CÁLCULO VOLUME") 
      op3 = valid(0,6,"Selecione o formato da figura:\n 0 - Voltar\n 1 - Pirâmides (Base Equilátera)\n 2 - Paralelepípedos\n 3 - Cilindros\n 4 - Cones\n 5 - Esferas\n 6 - Prismas (Base Equilátera)\n: ","Opção Inválida",1)
      if op3 == 0:
        break
      elif op3 == 1: #Pirâmides
        while True:
          num_lados_v1 = valid(0,"s",f"\n(3)>({op3}) CÁLCULO VOLUME: Pirâmides (Base Equilátera)\n0 = Voltar\nInsira o número de lados da base da pirâmide: ", "Valor inválido",1)
          if num_lados_v1 == 1 or num_lados_v1 == 2:
            print("Valor Inválido")
            continue
          if num_lados_v1 == 0:
            break
          while True:
            lado_base_v1 = valid(0,"s","\n0 = Voltar\nInsira o valor do lado da pirâmide: ", "Valor inválido")
            if lado_base_v1 == 0:
              break
            while True:
              altura_v1 = valid(0,"s","\n0 = Voltar\nInsira o valor da altura da pirâmide: ", "Valor inválido")
              if altura_v1 == 0:
                break
              area_base_v1 = (num_lados_v1 * lado_base_v1**2)/(4*m.tan(m.pi/num_lados_v1))
              volume1 = area_base_v1 * altura_v1 / 3
              print(f"\nVolume = {round(volume1,9)}   {notacient(volume1)}")
              while True:
                conv_v1 = valid(0,2,f"\nDigite a opção desejada:\n 0 - Voltar\n 1 - Continuar\n 2 - Converter resultado\n: ","Opção Inválida",1)
                if conv_v1 == 0:
                  break
                elif conv_v1 == 1:
                  break
                elif conv_v1 == 2:
                  while True:
                    unid_volume_i1 = valid(0,7,f"\nEscolha a unidade de medida do valor a ser convertido:\n 0 - Voltar\n 1 - km^3\n 2 - hm^3\n 3 - dam^3\n 4 - m^3\n 5 - dm^3\n 6 - cm^3\n 7 - mm^3\n: ","Opção Inválida",1)
                    if unid_volume_i1 == 0:
                      break
                    unid_volume_f1 = valid(0,7,f"\nEscolha a unidade final desejada para a conversão:\n 0 - Voltar\n 1 - km^3\n 2 - hm^3\n 3 - dam^3\n 4 - m^3\n 5 - dm^3\n 6 - cm^3\n 7 - mm^3\n: ","Opção Inválida",1)
                    if unid_volume_f1 == 0:
                      continue
                    convert(volume1,unid_volume_i1,unid_volume_f1,3)
                    break
                if unid_volume_i1 == 0:
                  continue
              if conv_v1 == 0:
                continue
              break 
            if altura_v1 == 0:
              continue
            break
      elif op3 == 2: #Paralelepípedos
        while True:
          lado_A_v2 = valid(0,"s","\n0 = Voltar\nInsira o valor do lado A do paralelepípedo: ", "Valor inválido")
          if lado_A_v2 == 0:
            break
          while True:
            lado_B_v2 = valid(0,"s","\n0 = Voltar\nInsira o valor do lado B do paralelepípedo: ", "Valor inválido")
            if lado_B_v2 == 0:
              break
            while True:
              altura_v2 = valid(0,"s","\n0 = Voltar\nInsira o valor da altura do paralelepípedo: ", "Valor inválido")
              if altura_v2 == 0:
                break
              volume2 = lado_A_v2 * lado_B_v2 * altura_v2 
              print(f"\nVolume = {round(volume2,9)}   {notacient(volume2)}")
              while True:
                conv_v2 = valid(0,2,f"\nDigite a opção desejada:\n 0 - Voltar\n 1 - Continuar\n 2 - Converter resultado\n: ","Opção Inválida",1)
                if conv_v2 == 0:
                  break
                elif conv_v2 == 1:
                  break
                elif conv_v2 == 2:
                  while True:
                    unid_volume_i2 = valid(0,7,f"\nEscolha a unidade de medida do valor a ser convertido:\n 0 - Voltar\n 1 - km^3\n 2 - hm^3\n 3 - dam^3\n 4 - m^3\n 5 - dm^3\n 6 - cm^3\n 7 - mm^3\n: ","Opção Inválida",1)
                    if unid_volume_i2 == 0:
                      break
                    unid_volume_f2 = valid(0,7,f"\nEscolha a unidade final desejada para a conversão:\n 0 - Voltar\n 1 - km^3\n 2 - hm^3\n 3 - dam^3\n 4 - m^3\n 5 - dm^3\n 6 - cm^3\n 7 - mm^3\n: ","Opção Inválida",1)
                    if unid_volume_f2 == 0:
                      continue
                    convert(volume2,unid_volume_i2,unid_volume_f2,3)
                    break
                if unid_volume_i2 == 0:
                  continue
              if conv_v2 == 0:
                continue
              break 
            if altura_v2 == 0:
              continue
            break
      elif op3 == 3: #Cilindros
        while True:
          raio_v3 = valid(0,"s",f"\n(3)>({op3}) CÁLCULO VOLUME: Cilindros\n0 = Voltar\nInsira o valor do raio do cilindro: ", "Valor inválido")
          if raio_v3 == 0:
            break
          while True:
            altura_v3 = valid(0,"s","\n0 = Voltar\nInsira o valor da altura do cilindro: ", "Valor inválido")
            if altura_v3 == 0:
              break
            volume3 = altura_v3 * m.pi * raio_v3**2
            print(f"\nÁrea = {round(volume3,9)}   {notacient(volume3)}")
            while True:
              conv_v3 = valid(0,2,f"\nDigite a opção desejada:\n 0 - Voltar\n 1 - Continuar\n 2 - Converter resultado\n: ","Opção Inválida",1)
              if conv_v3 == 0:
                break
              elif conv_v3 == 1:
                break
              elif conv_v3 == 2:
                while True:
                  unid_volume_i3 = valid(0,7,f"\nEscolha a unidade de medida do valor a ser convertido:\n 0 - Voltar\n 1 - km^3\n 2 - hm^3\n 3 - dam^3\n 4 - m^3\n 5 - dm^3\n 6 - cm^3\n 7 - mm^3\n: ","Opção Inválida",1)
                  if unid_volume_i3 == 0:
                    break
                  unid_volume_f3 = valid(0,7,f"\nEscolha a unidade final desejada para a conversão:\n 0 - Voltar\n 1 - km^3\n 2 - hm^3\n 3 - dam^3\n 4 - m^3\n 5 - dm^3\n 6 - cm^3\n 7 - mm^3\n: ","Opção Inválida",1)
                  if unid_volume_f3 == 0:
                    continue
                  convert(volume3,unid_volume_i3,unid_volume_f3,3)
                  break 
              if unid_volume_i3 == 0:
                continue
            if conv_v3 == 0:
              continue
            break 
      elif op3 == 4: #Cones
        while True:
          raio_v4 = valid(0,"s",f"\n(3)>({op3}) CÁLCULO VOLUME: Cones\n0 = Voltar\nInsira o valor do raio do cone: ", "Valor inválido")
          if raio_v4 == 0:
            break
          while True:
            altura_v4 = valid(0,"s","\n0 = Voltar\nInsira o valor da altura do cone: ", "Valor inválido")
            if altura_v4 == 0:
              break
            volume4 = (altura_v4 * m.pi * raio_v4**2)/3
            print(f"\nÁrea = {round(volume4,9)}   {notacient(volume4)}")
            while True:
              conv_v4 = valid(0,2,f"\nDigite a opção desejada:\n 0 - Voltar\n 1 - Continuar\n 2 - Converter resultado\n: ","Opção Inválida",1)
              if conv_v4 == 0:
                break
              elif conv_v4 == 1:
                break
              elif conv_v4 == 2:
                while True:
                  unid_volume_i4 = valid(0,7,f"\nEscolha a unidade de medida do valor a ser convertido:\n 0 - Voltar\n 1 - km^3\n 2 - hm^3\n 3 - dam^3\n 4 - m^3\n 5 - dm^3\n 6 - cm^3\n 7 - mm^3\n: ","Opção Inválida",1)
                  if unid_volume_i4 == 0:
                    break
                  unid_volume_f4 = valid(0,7,f"\nEscolha a unidade final desejada para a conversão:\n 0 - Voltar\n 1 - km^3\n 2 - hm^3\n 3 - dam^3\n 4 - m^3\n 5 - dm^3\n 6 - cm^3\n 7 - mm^3\n: ","Opção Inválida",1)
                  if unid_volume_f4 == 0:
                    continue
                  convert(volume4,unid_volume_i4,unid_volume_f4,3)
                  break 
              if unid_volume_i4 == 0:
                continue
            if conv_v4 == 0:
              continue
            break 
      elif op3 == 5: #Esferas
        while True:
          raio_v5 = valid(0,"s",f"\n(3)>({op3}) CÁLCULO VOLUME: Esfera\n0 = Voltar\nInsira o valor do Raio da esfera: ", "Valor inválido")
          if raio_v5 == 0:
            break
          volume5 = (m.pi * raio_v5**3) * 4 / 3
          print(f"\nÁrea = {round(volume5,9)}   {notacient(volume5)}")
          while True:
            conv_v5 = valid(0,2,f"\nDigite a opção desejada:\n 0 - Voltar\n 1 - Próximo formato\n 2 - Converter resultado\n: ","Opção Inválida",1)
            if conv_v5 == 0:
              break
            elif conv_v5 == 1:
              break
            elif conv_v5 == 2:
              while True:
                unid_volume_i5 = valid(0,7,f"\nEscolha a unidade de medida do valor a ser convertido:\n 0 - Voltar\n 1 - km^3\n 2 - hm^3\n 3 - dam^3\n 4 - m^3\n 5 - dm^3\n 6 - cm^3\n 7 - mm^3\n: ","Opção Inválida",1)
                if unid_volume_i5 == 0:
                  break
                unid_volume_f5 = valid(0,7,f"\nEscolha a unidade final desejada para a conversão:\n 0 - Voltar\n 1 - km^3\n 2 - hm^3\n 3 - dam^3\n 4 - m^3\n 5 - dm^3\n 6 - cm^3\n 7 - mm^3\n: ","Opção Inválida",1)
                if unid_volume_f5 == 0:
                  continue
                convert(volume5,unid_volume_i5,unid_volume_f5,3)
                break 
            if unid_volume_i5 == 0:
              continue
          if conv_v5 == 0:
            continue
          break 
      elif op3 == 6:
        while True:
          num_lados_v6 = valid(0,"s",f"\n(3)>({op3}) CÁLCULO VOLUME: Prisma (Base Equilátera)\n0 = Voltar\nInsira o número de lados da base do prisma: ", "Valor inválido",1)
          if num_lados_v6 == 1 or num_lados_v6 == 2:
            print("Valor Inválido")
            continue
          if num_lados_v6 == 0:
            break
          while True:
            lado_base_v6 = valid(0,"s","\n0 = Voltar\nInsira o valor do lado do prisma: ", "Valor inválido")
            if lado_base_v6 == 0:
              break
            while True:
              altura_v6 = valid(0,"s","\n0 = Voltar\nInsira o valor da altura do prisma: ", "Valor inválido")
              if altura_v6 == 0:
                break
              area_base_v6 = (num_lados_v6 * lado_base_v6**2)/(4*m.tan(m.pi/num_lados_v6))
              volume6 = area_base_v6 * altura_v6
              print(f"\nVolume = {round(volume6,9)}   {notacient(volume6)}")
              while True:
                conv_v6 = valid(0,2,f"\nDigite a opção desejada:\n 0 - Voltar\n 1 - Continuar\n 2 - Converter resultado\n: ","Opção Inválida",1)
                if conv_v6 == 0:
                  break
                elif conv_v6 == 1:
                  break
                elif conv_v6 == 2:
                  while True:
                    unid_volume_i6 = valid(0,7,f"\nEscolha a unidade de medida do valor a ser convertido:\n 0 - Voltar\n 1 - km^3\n 2 - hm^3\n 3 - dam^3\n 4 - m^3\n 5 - dm^3\n 6 - cm^3\n 7 - mm^3\n: ","Opção Inválida",1)
                    if unid_volume_i6 == 0:
                      break
                    unid_volume_f6 = valid(0,7,f"\nEscolha a unidade final desejada para a conversão:\n 0 - Voltar\n 1 - km^3\n 2 - hm^3\n 3 - dam^3\n 4 - m^3\n 5 - dm^3\n 6 - cm^3\n 7 - mm^3\n: ","Opção Inválida",1)
                    if unid_volume_f6 == 0:
                      continue
                    convert(volume6,unid_volume_i6,unid_volume_f6,3)
                    break
                if unid_volume_i6 == 0:
                  continue
              if conv_v6 == 0:
                continue
              break 
            if altura_v6 == 0:
              continue
            break
#########################################################################################
print("\nPrograma Encerrado!")