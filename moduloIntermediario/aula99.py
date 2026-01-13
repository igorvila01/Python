from sys import path

# utilizamos esse formato para importar modulos que estao dentro de pacotes
from aula99_package.modulo import soma_modulo
from aula99_package import modulo
import aula99_package.modulo

print(soma_modulo(1,2))
print(modulo.soma_modulo(5,2))
print(aula99_package.modulo.soma_modulo(2,3))

