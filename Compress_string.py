def compress(string):
    resultat= ''
    list_str = list(string)
    i=0
    while(i<len(list_str)-1):
        c = 1
        j=i+1
        while(j<len(list_str) and list_str[i] == list_str[j] ):
            c = c + 1
            j = j + 1 
        resultat += f'{list_str[i]}{c}'
        i = j 
    return resultat

print(compress('aaaabsssssssssssssssssslllllllllllaaccddaclakdvvvvfas;klssss'))

#output : a4b1s18l11a2c2d2a1c1l1a1k1d1v4f1a1s1;1k1l1s4
