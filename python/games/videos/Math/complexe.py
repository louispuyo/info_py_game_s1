
i = complex(1.3, 1.5)
# print(i)

# print(i.conjugate())
# print(i.imag, i.real)


def module(i:complex):
    print(f"|i| = {pow(((i.real*i.real)+(i.imag+i.imag)), 0.5)}")
    return pow(((i.real*i.real)+(i.imag+i.imag)), 0.5)

module(i)



'''
cos(teta) = a/|z| 
sin(teta) = b/|z|

ei0 = cos0+isin0

'''