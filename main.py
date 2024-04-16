def wiegand_to_decimal(area, code):
  calc = (area * 65536) + code
  return calc

def decimal_to_hex(decimal):
  hexadecimal = hex(decimal)
  return hexadecimal

def hex_to_decimal(hexadecimal):
  decimal = int(hexadecimal, 16)
  return decimal


def decimal_to_wiegand_area(decimal):
  area_numero = decimal // (4294967296)

  return area_numero

def decimal_to_wiegand_codigo(decimal):
  codigo_numero = decimal % (4294967296)
  return codigo_numero

while True:
  print("Selecione Uma opção:\n")
  print("1 - Converter de Decimal para Hexadecimal")
  print("2 - Converter de Hexadecimal para Decimal")
  print("3 - Converter de Decimal para Wiegand")
  print("4 - Converter de Wiegand para Decimal")
  print("5 - Converter de Hexadecimal para Wiegand")
  print("6 - Converter de Wiegand para Hexadecimal")
  print("0 - Sair")

  get_conversion = input()

  if get_conversion == "1":
      decimal_num = int(input("Insira o valor em decimal: "))
      print("Hexa: \n", decimal_to_hex(decimal_num))

  elif get_conversion == "2":
      hexadecimal_num = input("Insira o valor em hexadecimal: ")
      print("Decimal:", hex_to_decimal(hexadecimal_num))

  elif get_conversion == "3":
      decimal_num = int(input("Insira o valor em decimal: "))
      wiegand_area = decimal_to_wiegand_area(decimal_num)
      wiegand_codigo = decimal_to_wiegand_codigo(decimal_num)
      print("Wiegand: ", wiegand_area,",", wiegand_codigo)

  elif get_conversion == "4":
      wiegand_area = int(input("Insira o valor da área: "))
      wiegand_code = int(input("Insira valor do código: "))
      print("Decimal: ", wiegand_to_decimal(wiegand_area, wiegand_code))
    

  elif get_conversion == "5":
     hexadecimal_num = input("Insira o valor em hexadecimal: ")
     value_decimal = hex_to_decimal(hexadecimal_num)
     value_wiegand_area = decimal_to_wiegand_area(value_decimal)
     value_wiegand_codigo = decimal_to_wiegand_codigo(value_decimal)
     print("Wiegand:", value_wiegand_area,",", value_wiegand_codigo)
      

  elif get_conversion == "6":
      wiegand_area = int(input("Insira o valor da area: "))
      wiegand_code = int(input("Insira o valor do código: "))
      value_decimal = wiegand_to_decimal(wiegand_area, wiegand_code)
      value_hexa = decimal_to_hex(value_decimal)
      print("Hexadecimal: ", value_hexa)

  elif get_conversion == "0":
      print("Saindo...")
      break

  else:
      print("Opção inválida")