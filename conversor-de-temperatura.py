# função para converter temperatura de Celsius para Fahrenheit e Kelvin

def converter_temperatura(celsius):
    fahrenheit = celsius * 9/5 + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# entrada do usuário para a temperatura em Celsius
celsius = float(input("Informe a temperatura em Celsius: "))

# chamando a função para converter a temperatura
fahrenheit, kelvin = converter_temperatura(celsius)

# exibindo o resultado da conversão
print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F e {kelvin:.2f}K.")
