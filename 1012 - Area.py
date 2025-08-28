A, B, C = map(float, input().split())
pi = 3.14159
TRI = (A * C) / 2
CIR = pi * C ** 2
TRAP = ((A + B) /2) * C
SQA = B ** 2
REC = A * B
print(f'TRIANGULO: {TRI:.3f}')
print(f'CIRCULO: {CIR:.3f}')
print(f'TRAPEZIO: {TRAP:.3f}')
print(f'QUADRADO: {SQA:.3f}')
print(f'RETANGULO: {REC:.3f}')