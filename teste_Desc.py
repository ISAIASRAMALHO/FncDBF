def descript( v ):
    formula = 0
    t = len( v )
    r = ''
    caractere = ''
    n = 0
    convert_text = 0
    # for i in range(0, t ):
    #     formula = ord( v[i] ) - ( 22 * (i + 1) )
    #     caractere = chr( formula )
    #     print( 'Ordinal: {} - Calculo {} - Resultado {} - Caractere {}'
    #             .format( ord( v[i]), (22 * (i+1)), formula, caractere))
    #     r += caractere
    for i, c in enumerate( v ):
        # if i > 9: n =0
        convert_text = ord( c )
        caractere = ( chr( convert_text - 22 * (i +1) ) )
        # n += 1
        r += caractere
        print( 'Ordinal {}, Caractere {}'.format( convert_text, caractere))
    return r       




# CAMPO C_CODIGO = 00002. C_CLIENTE = CARLOS JOSE ALVES FEITOSA
word = 'Ym¤½×ºú/7(_ ¥É¬èý8Icg\r´Êàö"8Ndz¦¼Òèþ'

print( descript(word ) )