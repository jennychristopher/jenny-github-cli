from adddiv_model.adddiv_model import adddiv
from addmul_model.addmul_model import addmul

def compound_model(a,b,c):
    first_output = adddiv(a,b,c)
    sec_output = addmul(a,b,c)
    return first_output + sec_output