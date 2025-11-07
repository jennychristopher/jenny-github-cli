from addmul_model.addmul_model import addmul
from adddiv_model.adddiv_model import adddiv

def compound_model(a,b,c):
    addmul_res = addmul(a,b,c)
    adddiv_res = adddiv(a,b,c)
    return addmul_res + adddiv_res