import os, sys

def createSIP(id, password):
	templateExt = f'''
exten=>{id},1,Dial(SIP/{id},99999)
'''

	templateSIP = f'''
[{id}]
type=friend
context=from-internal
host=dynamic
secret={password}
disallow=all
allow=ulaw
'''

	os.system(f'echo "{templateSIP}" > /etc/asterisk/sip.conf.d/{id}.conf')
	os.system(f'echo "{templateExt}" > /etc/asterisk/extensions.conf.d/{id}.conf')

def deleteSIP():
	print('''
Delete SIP Account
''')

	files = os.listdir('/etc/asterisk/sip.conf.d')
	for i in files:
		i = i.split('.conf')[0]

		print(f'[(*) {i}]')

	print('\n')
	id = input('Masukkan id : ')
	os.system(f'rm -f /etc/asterisk/sip.conf.d/{id}.conf')
	os.system(f'rm -f /etc/asterisk/extensions.conf.d/{id}.conf')

def main():
	os.system('clear')

	print('''
1. Init aterisk
2. Create SIP Account
3. Remove SIP Account
4. Exit

''')

	pilihan = int(input('Masukkan pilihan : '))

	if pilihan == 1:
		os.system('mkdir -p /etc/asterisk/sip.conf.d')
		os.system('mkdir -p /etc/asterisk/extensions.conf.d')
		os.system('echo "[general]\ncontext=default\ndirectrtpsetup=no\ncanreinvite=no\n\n#include /etc/asterisk/sip.conf.d/*" > /etc/asterisk/sip.conf')
		os.system('echo "[from-internal]\n\n#include /etc/asterisk/extensions.conf.d/*" > /etc/asterisk/extensions.conf')

		os.system('service restart asterisk')

		main()

	elif pilihan == 2:
		os.system('clear')
		print('''
Create SIP Account
''')

		id = input('Masukkan id / username SIP\t:\t')
		password = input('Masukkan password SIP\t\t:\t')

		createSIP(id, password)

		os.system('service asterisk reload')

		main()

	elif pilihan == 3:
		os.system('clear')
		deleteSIP()

		main()

	elif pilihan == 4:
		sys.exit();

	else:
		print('pilihan tidak ada dalam menu !!!')



main()
