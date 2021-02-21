from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

from api.blockchain import connect



def find_account_by_code(code):
    data_ = {}
    substrate = connect()
    result = substrate.query(
        module='Referral',
        storage_function='Promoter',
        params=[code]
    )   
    data_['code'] = code   
    if result:
        data_['accountId'] = result.value
    return data_

def find_code_by_account(account_id):
    data_ = {}
    substrate = connect()
    result = substrate.query(
        module='Referral',
        storage_function='PromoterCode',
        params=[account_id]
    )   
    data_['accountId'] = account_id
    if result:
        data_['code'] = result.value
    return data_       

def check_code_set(account_id):
    data_ = {}
    substrate = connect()
    result = substrate.query(
        module='Referral',
        storage_function='PromoterCodeSet',
        params=[account_id]
    )   
    if result:
        data_['codeSet'] = result.value
    else:
        data_['codeSet'] = False
    return data_   

def check_number_of_references(account_id):
    data_ = {}
    substrate = connect()
    result = substrate.query(
        module='Referral',
        storage_function='ReferenceCount',
        params=[account_id]
    )   
    data_['accountId'] = account_id
    if result:
        data_['count'] = result.value

    return data_   


def check_registration(account_id):
    data_ = {}
    substrate = connect()
    result = substrate.query(
        module='Referral',
        storage_function='Registered',
        params=[account_id]
    )   
    data_['accountId'] = account_id
    if result:
        data_['registered'] = result.value
    else:
        data_['registered'] = False
    
    return data_                                          

def register_from_code(code, _data):
    data_ = {}
    substrate = connect()

    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Referral',
        call_function='register_from_code',
        call_params={
            'code': code
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash
    return data_


def set_promoter_code(code, _data):
    data_ = {}
    substrate = connect()

    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Referral',
        call_function='promoter_set_code',
        call_params={
            'code': code
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash
    return data_      
