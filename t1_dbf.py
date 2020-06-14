from dbfread import DBF
import sys
import glob
from pandas import DataFrame


def descript( v ):
    s = ''
    for i in range(0, len( v ) ):
        s += chr( ord( v[i] ) - 10 )
    return s    


def Openfile( f_lista):
    # MONTAR MENU DE OPÇÕES.
    f_lista.append('SAIR')
    for d, valor in enumerate(f_lista):
        print('Opção {} - {}'.format(d, valor) )
    # VAMOS PEDIR O USUÁRIO QUE DIGITE UM VALOR     
    q_dbf = input( 'Digite a opção desejada: ')
    if q_dbf:
        if int( q_dbf)  == len( f_lista) - 1:
            print('Saindo...')
        else:
            tabela = DBF(f_lista[ int( q_dbf) ], encoding='latin1')
            frame = DataFrame( tabela )
            # frame.head()
            if f_lista[ int( q_dbf) ] == 'A_CLIENT.DBF':
                print( frame['C_CLIENTE'] )
            print( frame.head() )
            # if tabela.field_names == 'CLIENTE':
            #     print(tabela.fields)
            #     for record in tabela:
            #             print(record)


#f = input()
lista_f = glob.glob( '*.dbf')

if lista_f:
    Openfile( lista_f )
    #print( 'Existem {} arquivos nesta pasta'.format( len( f_lista) ) )
else:
    print('Não existe nenhum arquivo do tipo nesta pasta')