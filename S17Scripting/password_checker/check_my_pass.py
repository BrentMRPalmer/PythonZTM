# Check My Password

# CBFDAC6008F9CAB4083784CBD1874F76618D2A97 is the SHA1 hashed version of password123
# k-anonymity - only give first 5 - they also don't know who we are

import requests
import hashlib
import sys

def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error fetching: {res.status_code}', 'check the api and try again')
	return res

def get_password_leaks_count(hashes, hash_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hash_to_check:
			return count
	return 0

def pwned_api_check(password):
	# Check if password exists in API response
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char, tail = sha1password[:5], sha1password[5:]
	response = request_api_data(first5_char)
	return get_password_leaks_count(response, tail)

def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count:
			print(f'Your password {password} was found {count} times. You should change your password.')
		else: print(f'Your password {password} was not found. Carry on!')
	return 'Done!'

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))