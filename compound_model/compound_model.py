from addcmul_model.addcmul_model import addcmul
from addcdiv_model.addcdiv_model import addcdiv

def compound_model(a,b,c):
    mul_part = addcmul(a,b,c)
    div_part = addcdiv(a,b,c)
    return mul_part + div_part