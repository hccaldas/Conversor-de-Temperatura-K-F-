# Conversor de Temperatura em Python

Este repositório contém um script em Python que converte temperaturas de Celsius para Fahrenheit e Kelvin.

## Funcionalidades

- Conversão de temperatura de Celsius para Fahrenheit.
- Conversão de temperatura de Celsius para Kelvin.

## Pré-requisitos

- Python 3.x

## Como usar

1. Clone este repositório ou copie o código para o seu ambiente local.
2. Certifique-se de ter o Python 3.x instalado no seu sistema.
3. Execute o script.
4. Insira a temperatura em Celsius quando solicitado.
5. O script exibirá a temperatura equivalente em Fahrenheit e Kelvin.

## Exemplo de Uso

```python
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
