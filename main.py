phone = '70000000000'
api_id = 1111111
api_hash = 'aaaaaaaaaaaaaaaaaaaaaa'
numlist = 'numlist.txt'

from abuse_handler import AbuseTg

if __name__=='__main__':
    abuser = AbuseTg(api_id=api_id, api_hash=api_hash,phone = phone, numlist = numlist)
    abuser.brute_force()
