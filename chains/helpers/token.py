from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

from api.blockchain import substrate

def get_paused_status(token):
    data_ = {}
    status = substrate.query(
        module='Token',
        storage_function='Paused',
        params=[str(token)]
    )    
    data_['status'] = status
    return data_

def get_banker(token):
    data_ = {}
    banker = substrate.query(
        module='Token',
        storage_function='Owner',
        params=[str(token)]
    )    
    data_['banker'] = banker.value   
    return data_

def get_total_supply(token):
    data_ = {}
    supply = substrate.query(
        module='Token',
        storage_function='Supply',
        params=[str(token)]
    )    
    data_['supply'] = supply.value  
    return data_

def get_account_balance(token, account_id):
    data_ = {}
    balance = substrate.query(
        module='Token',
        storage_function='Balance',
        params=[({
            'col1': str(token),
            'col2': account_id,
        })])  
    data_['accountId'] = account_id                  
    data_['balance'] = balance.value     
    return data_

def get_a_token(token):
    data_ = {}
    token = substrate.query(
        module='Token',
        storage_function='Tokens',
        params=[
            str(token)
    ])  
    data_['token'] = token.value     
    return data_

def get_all_token():
    data_ = {}
    data_['tokens'] = []
    token_count = substrate.query(
        module='Token',
        storage_function='TokenCount')      
    for i in range(0, token_count.value):
        token = substrate.query(
            module='Token',
            storage_function='Tokens',
            params=[str(i)])
        _token = token.value
        _token['tokenIndex'] = str(i)
        data_['tokens'].append(_token)       
    return data_

def transfer_token(token, account_from, account_to, amount, _data):
    data_ = {}
    
    _from = account_from
    _to = account_to
    _amount = amount

    caller = _data['caller']
    key = _data['key']

    keypair = Keypair.create_from_mnemonic(key)

    call = substrate.compose_call(
        call_module='Token',
        call_function='transfer',
        call_params={
            'token': token,
            'to': _to,
            'value': str(int(0.01 * 10 ** 12))
    })
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash
    return data_
