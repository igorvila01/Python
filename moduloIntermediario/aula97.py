# Entendendo os seus proprios modulos 
# O primeiro modulo executado chama-se __main__
# Voce pode importar outro modulo inteiro ou parte do modulo
# O Python conhece a pasta onde o __main__ esta e as pastas abaixo dele.
# Ele nao reconhece pastas e modulos acima do __main__ por padrao
# O python conhece todos os modulos e pacotes presentes nos caminhos de sys.path

# import sys

# importação do modulo inteiro 
import aula97_m

# importando somente o necessario 
from aula97_m import soma, variavel_modulo

print(aula97_m.variavel_modulo)
print(variavel_modulo)
print(soma(2,3))
print(aula97_m.soma(2,5))

#  print('Este modulo se chama', __name__)
#  print(*sys.path, sep='\n')