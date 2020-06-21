# VAMOR RECOMEÇAR.
# PARTICIONANDO A STRING DE CARACTERES.



def descript( v ):
    # PARTICIONANDO O PARAMETRO "v"
    particao = []
    cont = 0
    tam = len( v )
    r = ''
    caractere = ''
    n = 0
    convert_text = 0
    # ARREDONDANDO...
    if tam % 8 > 0:
        d = int( tam / 8 ) + 1
    else:
        d = int( tam / 8 )
    # PARTICIONANDO
    for q in range( 0, d):
        particao.append( v[ cont:cont+8] )
        cont += 8
        
        # DESCRIPTOGRAFANDO POR PARTES.
        for i, c in enumerate( particao[q] ):
            print('Sequência: {}'.format(i))
            for it in c:
                if ord(it) < ( 22 * (i+1)):
                    convert_text = ( 22 * ( i +1 ) ) - ord( it  )
                elif ord(it) > ( 22 * (i+1)):
                    convert_text = ord( it  ) - ( 22 * ( i +1 ) )
                caractere = ( chr( convert_text ) )
                r += caractere
                print( 'Ordem: {}, Código e Caractere ASCII Original: {} - {}, Fórmula ( 22 * ( {} + 1 ) ) = : {}, Novo Codigo e Caractere ASCII: {} - {}'
                    .format( i, ord(it), it, i, (22*(i+1)), ord( caractere ), caractere))
                print( '-'*80)
            
    return r       




# CAMPO C_CODIGO = 00002. C_CLIENTE = CARLOS JOSE ALVES FEITOSA
word = 'Ym¤½×ºú/8(_ ¥É¬èý8Icg\r´Êàö"8Ndz¦¼Òèþ'

print( descript(word ) )
