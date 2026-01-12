# Entendendo os seus proprios modulos 
# O primeiro modulo executado chama-se __main__
# Voce pode importar outro modulo inteiro ou parte do modulo
# O Python conhece a pasta onde o __main__ esta e as pastas abaixo dele.
# Ele nao reconhece pastas e modulos acima do __main__ por padrao
# O python conhece todos os modulos e pacotes presentes nos caminhos de sys.path

import sys

# importação do modulo inteiro 
import aula97_m

print('Este modulo se chama', __name__)
print(*sys.path, sep='\n')