def descript( v ):
    r = ''
    caractere = ''
    contador, convert_text = 0, 0
    for i, c in enumerate( v ):
        if i < 9:
            convert_text = ord( c ) - ( 22 * ( contador +1 ) )
            contador +=1
        elif i > 9:
            contador = 0  
        # if convert_text >= 0 and convert_text <= 255:
        #     caractere = chr( convert_text  )
        # elif convert_text < 0:
        #     caractere = chr( convert_text + 255  )
        # elif convert_text > 255:
        #     caractere = chr( convert_text - 255 )
        # r += caractere
        # print( 'Ordem: {} - Ordinal: {} - Caractere Original: {} - Formula ( 22 * ({}+1): {} - Caractere Descriptografado: {}'
            # .format( i, ord(c), c, i,  int(22 * (i+1)), caractere))
        if convert_text <= 0:
            print( convert_text + 255 )
        elif convert_text >= 255:
            print( convert_text - 255)
    # return r       


# CAMPO C_CODIGO = 00002. C_CLIENTE = CARLOS JOSE ALVES FEITOSA
word = 'Ym¤½×ºú/7(_ ¥É¬èý8Icg\r´Êàö"8Ndz¦¼Òèþ'

# for i, c in enumerate( word ):
#     print('Ordem: {} - Caractere: {} - Ordinal: {}'.format( i, c, ord( c )))

word2 = 'lm³Òãü+@(l¥É¬õ6?cF\r´Êàö"8Ndz¦¼Òèþ'

descript(word)