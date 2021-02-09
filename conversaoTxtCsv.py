import pandas as pd
import time

inicio = time.time()
arquivoTXT = pd.read_fwf('arquivo.txt')
arquivoCSV = arquivoTXT.to_csv('novoArquivo.csv', index = None)
fim = time.time()
print ('Tempo de execução: %f' % (fim - inicio))