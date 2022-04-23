import dns.resolver

res = dns.resolver.Resolver()
alvo = 'bancocn.com'
arquivo = open('/home/sl/Documentos/my/cyber-sec/scripts/wordlist.txt', 'r')
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
