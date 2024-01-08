import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')

except urllib.error.URLError:
    print('Não foi possivel acessar o site \"pudim\"')

else:
    print('Foi possivel acessar o site \"pudim\"')