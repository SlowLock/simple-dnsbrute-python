# this script was developed as a way of learning, it is not recommended to use it in real cases

import dns.resolver

res = dns.resolver.Resolver()
alvo = 'bancocn.com'
# put the worlist path here
arquivo = open('PUT_WORDLIST', 'r')
subdominios = arquivo.read().splitlines()

print('\033[1;36m'+'------ SUBDOMINIOS ENCONTRADOS ------'+'\033[0;0m')
for subdominio in subdominios:
	try:
		sub_alvo = subdominio + '.' + alvo
		resultado = res.resolve(sub_alvo, 'A')
		for ip in resultado:
			print(sub_alvo, '-->', ip)
	except:
		pass
