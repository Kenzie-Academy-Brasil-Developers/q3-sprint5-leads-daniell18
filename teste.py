import re
x=41
def teste():
    if not re.fullmatch(r'\([0-9]{2}\)[0-9]{4,5}-[0-9]{4}',x):
        return ({'error':f'incorrect phone the correct format is (xx)xxxxx-xxx'})
print(teste())