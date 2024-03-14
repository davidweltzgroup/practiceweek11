


def getBondPrice(y, face, couponRate, m, ppy=1):
    if ppy == 1:
        x = 2170604
    if ppy == 2:
        x = 2171686
    pvcfsum = 0
    
    cf = couponRate*face
    for t in range(1,(ppy*m)+1):
        pv = (1+y/ppy) **(-(t))
        pvcf=pv*cf/ppy
        pvcfsum += pvcf
    
    bondprice = pvcfsum + pv*face
    #print(bondprice, "hello")
    return(bondprice)
