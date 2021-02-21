from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

from api.blockchain import connect

def get_paused_status(token):
    data_ = {}
    substrate = connect()
    status = substrate.query(
        module='Token',
        storage_function='Paused',
        params=[str(token)]
    )    
    data_['status'] = status
    return data_

def get_banker(token):
    data_ = {}
    substrate = connect()
    banker = substrate.query(
        module='Token',
        storage_function='Owner',
        params=[str(token)]
    )    
    data_['banker'] = substrate.ss58_encode(banker.value)
    return data_

def get_total_supply(token):
    data_ = {}
    substrate = connect()
    supply = substrate.query(
        module='Token',
        storage_function='Supply',
        params=[str(token)]
    )    
    data_['supply'] = supply.value  
    return data_

def get_account_balance(token, account_id):
    data_ = {}
    substrate = connect()
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
    substrate = connect()
    token = substrate.query(
        module='Token',
        storage_function='Tokens',
        params=[
            str(token)
    ])  
    data_['token'] = token.value    
    data_['token']['owner'] = substrate.ss58_encode(data_['token']['owner']) 
    return data_

def get_all_token():
    data_ = {}
    substrate = connect()
    
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
        _token['owner'] = substrate.ss58_encode(_token['owner'])
        data_['tokens'].append(_token)       
    return data_

def transfer_token(token, _data):
    data_ = {}
    substrate = connect()
    
    _to = _data['to']
    _amount = _data['amount']

    caller = _data['caller']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Token',
        call_function='transfer',
        call_params={
            'token': token,
            'to': _to,
            'value': _amount
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash
    return data_
