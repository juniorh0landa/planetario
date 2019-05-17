from i_dados import leitor as ler #interpreta os dados
from a_dados import analisador as analisar #analisa os dados interpretados
from v_dados import visualizador as visualizar #visualiza os dados analisados

dados = ler("dados.txt")
analise = analisar(dados.planetas,dados.modelos,dados.contato,dados.integrador,dados.tempo)
plotar = visualizar