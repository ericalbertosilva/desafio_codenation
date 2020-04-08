import json, requests, hashlib, string

response = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=eb39072fc130f9f018e1698c4e3d7e7fc2f772d6")

arquivo_json = json.loads(response.content)

with open('answer.json', 'w') as arq:
    json.dump(arquivo_json, arq, indent=4, ensure_ascii=False)

token = arquivo_json['token']
rotacao = int(arquivo_json['numero_casas'])  
alfabeto = string.ascii_lowercase
texto_cifrado = arquivo_json['cifrado']
texto_decifrado=''

for letra in texto_cifrado:
    if letra in alfabeto:
        posicao = alfabeto.find(letra)
        posicao = (posicao - rotacao) % 26
        texto_decifrado = texto_decifrado + alfabeto[posicao]

"""for caracter in texto_cifrado:
    if caracter in alfabeto:
        posicao = alfabeto.find(caracter)
        if posicao >= len(alfabeto):
            posicao = posicao - len(alfabeto)
        elif posicao < 0 :
            posicao = posicao + len(alfabeto)
            texto_decifrado = texto_decifrado + alfabeto[posicao]
        else:
            texto_decifrado + caracter
print(texto_decifrado)"""    

resumo_criptografico = hashlib.sha1(arquivo_json['decifrado']).hexdigest()

"""hash = hashlib.sha1()
hash.update("organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations. melvin conway")
resumo_criptografico = hash.hexdigest()
print(resumo_criptografico)"""

json_dict = {
    'numero_casas': rotacao,
    'decifrado': texto_decifrado,
    'token': token,
    'resumo_criptografico':resumo_criptografico,
    'cifrado': texto_cifrado
}

with open('answer.json', 'w') as json_file:
    json.dump(json_dict,json_file,indent=4)










