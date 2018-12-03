def rate_conver(i,n,tasa_a_conv="nominal"):
    if tasa_a_conv == "nominal":
        tasa_conv=n*((1+i)**(1/n)-1)
    elif tasa_a_conv == "efectiva":
        tasa_cov=(1+i/n)**n-1
    return tasa_conv