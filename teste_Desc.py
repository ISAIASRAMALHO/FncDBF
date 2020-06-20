# VAMOR RECOMEÇAR.
# PARTICIONANDO A STRING DE CARACTERES.



def descript( v ):
    # PARTICIONANDO O PARAMENTRO "v"
    particao = []
    cont = 0
    tam = len( v )
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

    r = ''
    caractere = ''
    n = 0
    convert_text = 0


    # for i, c in enumerate( v[9:17] ):
    #     convert_text = ord( c  ) - ( 22 * ( i +1 ) )
    #     if convert_text >= 0 and convert_text <= 255:
    #         caractere = ( chr( convert_text ) )
    #     elif convert_text < 0:
    #         caractere = ( chr( convert_text + 255 ) )
    #     elif convert_text > 255:
    #         caractere = ( chr( convert_text - 255 ) )
    #     r += caractere
    #     print( 'Ordinal {}, Caractere {}'.format( convert_text, caractere))
    return r       




# CAMPO C_CODIGO = 00002. C_CLIENTE = CARLOS JOSE ALVES FEITOSA
word = 'Ym¤½×ºú/7(_ ¥É¬èý8Icg\r´Êàö"8Ndz¦¼Òèþ'

print( descript(word ) )
