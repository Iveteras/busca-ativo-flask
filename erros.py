def previne_erro(retorna_ativo):
    import json

    json_ativo_bruto = retorna_ativo[0]
    json_ativo_propriedades = json.loads(json_ativo_bruto)

    if (len(json_ativo_propriedades["Date"]) != 0): 
        return True
    




























