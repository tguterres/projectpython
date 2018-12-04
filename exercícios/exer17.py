#catetos
import math
ca = float(input('Cateto adjacente: '))
co = float(input('Cateto oposto: '))
hp = math.hypot(ca, co)
print('{:.2f}'.format(hp))
