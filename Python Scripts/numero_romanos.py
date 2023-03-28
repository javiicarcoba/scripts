def romanToInt(s: str) -> int:
    suma = 0
    letras = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for i in range(len(s)):
        if s[i] == 'V' and s[i-1] == 'I' and i>0:
            suma += 3
        elif s[i] == 'L' and s[i-1] == 'X' and i>0:
            suma += 30
        elif s[i] == 'C' and s[i-1] == 'X' and i>0:
            suma += 80
        elif s[i] == 'D' and s[i-1] == 'C' and i>0:
            suma += 300
        elif s[i] == 'M' and s[i-1] == 'C' and i>0:
            suma += 800
        else:
            suma +=letras[s[i]]    

    return suma

pruebas = ["III","LVIII","MCMXCIV"]

for cad in pruebas:
    print(romanToInt(cad))