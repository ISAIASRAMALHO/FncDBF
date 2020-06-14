def descript( v ):
    formula = 0
    t = len( v )
    r = ''
    caractere = ''
    n = 0
    for i in range(0, t ):
        formula = ord( v[i] ) - ( 22 * (n + 1) )
        n += 1
        if len(caractere) % 10 == 0 : n = 1
        print( 'Caractere: {}'.format(formula))
        caractere = chr( formula )
        r += caractere
        print('Formula {}, for número: {}'.format(formula, r )  )
    return r       


word = '\~¦±Ííóü;V_w¡ÐçØ!3Ocg\r´Êàö'

print( descript(word ) )

# t = len( word)
# w = ''
# print('Quantidade de caracteres: {}'.format( t ))

# for c in range(0, t ):
#     w += word[c]
#     print( w)


# print('Original: {}'.format(word))


# sub = descript( word )

# print( sub )