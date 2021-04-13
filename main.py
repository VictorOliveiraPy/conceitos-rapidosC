from src.acoes.correr import FazerCorrida
from src.pessoa import Pessoa
from src.acoes.falar import IniciarFala

# Injecao de dependencias


pessoa1 = Pessoa(IniciarFala())
pessoa1.realizarAcao()

pessoa2 = Pessoa(FazerCorrida())
pessoa2.realizarAcao()
