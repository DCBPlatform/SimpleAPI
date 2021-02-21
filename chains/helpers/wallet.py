from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

from api.blockchain import connect
from api.twilio import send_verify_sms, verify_sms, send_sms

from wallets.models import Wallet

def generate_wallet():

    mnemonic = Keypair.generate_mnemonic()
    keypair = Keypair.create_from_mnemonic(mnemonic)
        
    data_ = {
        'mnemonic': mnemonic, 
        'address': keypair.ss58_address,
        'public_key': keypair.public_key,
        'private_key': keypair.private_key,
    }

    return data_


def check_wallet_balance(account_id, checker_id):
    data_ = {}
    substrate = connect()

    result = substrate.query(
        module='System',
        storage_function='Account',
        params=[account_id]
    )          
    data_['account'] = account_id

    if result:
        data_['balance'] = result.value
    else:
        data_['balance'] = 0

    return data_


def verify_phone(phone, _data):    
    wallets = Wallet.objects.filter(phone=phone).all()
    keypair = Keypair.create_from_mnemonic(_data['mnemonic'])
    if len(wallets) < 5 and keypair:
        result = send_verify_sms(phone)
        data_ ={
            'status': result.status,
            'wallet': keypair.ss58_address
        }
        
    else:
        data_ = {
            'phone': phone,
            'registered': True
        }
    return data_     


def verify_phone_code(phone, code, _data):
    result = verify_sms(phone, code)
    data_ = {}
    keypair = Keypair.create_from_mnemonic(_data['mnemonic'])
    if result.status == 'approved' and keypair:
        wallet = Wallet.objects.create(phone=phone, wallet_address=keypair.ss58_address)
        data_['wallet'] = wallet.id
        message = "Wallet: " + keypair.ss58_address + " has been generated for " + "+" + str(phone)
        data_['sid'] = send_sms('18454201095', '+' + str(phone), message)
    else:
        data_['status'] = 'pending'
    return data_


def upload_evidence(file_object, account_id, evidence):
    pass