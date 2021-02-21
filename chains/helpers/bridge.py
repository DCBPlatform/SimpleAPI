from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException


from api.blockchain import connect


def get_watchers():
    data_ = {}
    substrate = connect()
    result = substrate.query(
        module='Bridge',
        storage_function='Watchers')  
    list_of_watchers = []          
    if result:
        for watcher in result.value:
            list_of_watchers.append(substrate.ss58_encode(watcher))
        
    data_['watchers'] = list_of_watchers
    return data_

def get_ether_issue(issue_id):
    data_ = {}
    substrate = connect()
    result = substrate.query(
        module='Bridge',
        storage_function='Issue',
        params=[issue_id])   
    if result:
        data_['issue'] = result.value
    else:
        data_['issue'] = []  
    return data_

def get_ether_issue_by_user(account_id):
    data_ = {}
    substrate = connect()
    result = substrate.query(
        module='Bridge',
        storage_function='IssueByUser',
        params=[account_id])   
    if result:
        data_['issue'] = result.value
    else:
        data_['issue'] = []      
    return data_

def get_ether_issue_count():
    data_ = {}
    substrate = connect()
    result = substrate.query(
        module='Bridge',
        storage_function='IssueCount')   
    if result:
        data_['count'] = result.value
    else:
        data_['count'] = 0
    return data_

def get_ether_unminted_issues():
    data_ = {}
    substrate = connect()
    result = substrate.query(
        module='Bridge',
        storage_function='UnmintedIssues')  
    list_of_issues = []          
    if result:
        for issue in result.value:
            list_of_issues.append(issue)
        
    data_['issues'] = list_of_issues    
    return data_

def get_ether_redemption(redemption_id):
    data_ = {}
    substrate = connect()
    result = substrate.query(
        module='Bridge',
        storage_function='Redemption',
        params=[redemption_id])   
    if result:
        data_['redemption'] = result.value
    else:
        data_['redemption'] = []     
    return data_

def get_ether_redemption_by_user(account_id):
    data_ = {}
    substrate = connect()
    result = substrate.query(
        module='Bridge',
        storage_function='RedemptionByUser',
        params=[account_id])   
    if result:
        data_['redemption'] = result.value
    else:
        data_['redemption'] = []         
    return data_

def get_ether_redemption_count():
    data_ = {}
    substrate = connect()
    result = substrate.query(
        module='Bridge',
        storage_function='RedemptionCount')   
    if result:
        data_['count'] = result.value
    else:
        data_['count'] = 0    
    return data_

def get_ether_unburnt_redemptions():
    data_ = {}
    substrate = connect()
    result = substrate.query(
        module='Bridge',
        storage_function='UnburntRedemptions')  
    list_of_redemptions = []          
    if result:
        for redemption in result.value:
            list_of_redemptions.append(redemption)
        
    data_['redemptions'] = list_of_redemptions     
    return data_



def add_watcher(_data):
    data_ = {}
    substrate = connect()
    account_id = _data['accountId']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Bridge',
        call_function='add_watcher',
        call_params={
            'watcher': account_id,
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_

def remove_watcher(_data):
    data_ = {}
    substrate = connect()
    
    account_id = _data['accountId']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Bridge',
        call_function='remove_watcher',
        call_params={
            'watcher': account_id,
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_

def create_issue(_data):
    data_ = {}
    substrate = connect()
    eth_sender = _data['ethSender']
    eth_vault = _data['ethVault']
    eth_amount = _data['ethAmount']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Bridge',
        call_function='create_issue',
        call_params={
            'eth_sender': eth_sender,
            'eth_vault': eth_vault,
            'eth_amount': eth_vault,
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_

def execute_issue(_data):
    data_ = {}
    substrate = connect()
    issue_id = _data['issueId']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Bridge',
        call_function='execute_issue',
        call_params={
            'issue_id': issue_id
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_

def create_redemption(_data):
    data_ = {}
    substrate = connect()
    eth_receiver = _data['ethReceiver']
    eth_vault = _data['ethVault']
    eth_amount = _data['ethAmount']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Bridge',
        call_function='create_redemption',
        call_params={
            'eth_receiver': eth_receiver,
            'eth_vault': eth_vault,
            'eth_amount': eth_vault,
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_

def update_issue(_data):
    data_ = {}
    substrate = connect()
    issue_id = _data['issueId']
    transaction = _data['transaction']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Bridge',
        call_function='update_issue',
        call_params={
            'issue_id': issue_id,
            'transaction': transaction,
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_

def update_redemption(_data):
    data_ = {}
    substrate = connect()
    redemption_id = _data['redemptionId']
    transaction = _data['transaction']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Bridge',
        call_function='update_redemption',
        call_params={
            'redemption_id': redemption_id,
            'transaction': transaction,
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

def cancel_issue(_data):
    data_ = {}
    substrate = connect()
    issue_id = _data['issueId']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Bridge',
        call_function='cancel_issue',
        call_params={
            'issue_id': issue_id
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_

def cancel_redemption(_data):
    data_ = {}
    substrate = connect()
    redemption_id = _data['redemptionId']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Bridge',
        call_function='cancel_redemption',
        call_params={
            'redemption_id': redemption_id
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_
