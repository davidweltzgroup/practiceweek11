
def getBondDuration(y, face, couponRate, m, ppy = 1):
    #return(8.51)
    pvcfsum = 0
    pvcfdsum = 0
    
    cf = couponRate*face
    for t in range(1,m+1):
        #print(t)
        pv = (1+y) **(-(t))
        pvcf=pv*cf
        pvcfsum += pvcf
        pvcfdsum += pvcf*(t)
    
    bondprice = pvcfsum + pv*face
    bondpriced = pvcfdsum + pv*face*m
    #print(bondprice, "hello", bondpriced/bondprice, m)
    return(bondpriced/bondprice)
