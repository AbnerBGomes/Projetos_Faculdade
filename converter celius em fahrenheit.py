f = float(input("informe a temperatura em Fahrenheit: "))
c = 5 * ((f-32) / 9)
print("a temperatura {} Fahrenheit é igual a {} Celsius. "
      .format(f, "%.2f" % c))
