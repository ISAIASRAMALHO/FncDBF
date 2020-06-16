def descript( v ):
    r = ''
    caractere = ''
    convert_text = 0
    formula = 0

    for i, c in enumerate( v ):
        convert_text = ord( c ) - 22 * (i+1)
        if convert_text < 0:
            caractere = ( chr( convert_text + 256 ) )
        elif convert_text > 255:
            caractere = ( chr( convert_text - 255  ) )
        else:
            caractere= ( chr( convert_text ) )
        r += caractere
        print( 'Ordem: {} - Ordinal: {} - Caractere Original: {} - Formula ( 22 * ({}+1): {} - Caractere Descriptografado: {}'
            .format( i, ord(c), c, i,  int(22 * (i+1)), caractere))
    return r       




# CAMPO C_CODIGO = 00002. C_CLIENTE = CARLOS JOSE ALVES FEITOSA
word = 'Ym¤½×ºú/7(_ ¥É¬èý8Icg\r´Êàö"8Ndz¦¼Òèþ'

w2 = '/7(_ ¥É'

word2 = 'lm³Òãü+@(l¥É¬õ6?cF\r´Êàö"8Ndz¦¼Òèþ'

print( descript(word) )

# w1 = word[0:8]
# w2 = word[9:17]

# print( descript( w1 ) )
# print( descript( w2 ) )