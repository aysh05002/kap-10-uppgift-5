def nettopris(x):
    if x<500:
        return x
    elif x>=500 and x<1000:
        x=x*(1-0.02)
        return x
    elif x>=1000:
        x=x*(1-0.05)
        return x

print(nettopris(int(input("Hur mycke betalar du? "))))
