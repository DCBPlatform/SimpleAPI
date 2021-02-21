from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException


from api.blockchain import connect


def get_bazaar_trader_id(account_id):
    data_ = {}
    substrate = connect()
    data_['accountId'] = account_id
    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTraderId',
        params=[str(account_id)])  
    if result:
        data_['traderId'] = result.value
        data_['isTrader'] = True
    else:
        data_['isTrader'] = False
    return data_

def get_bazaar_trader_detail(trader_id):
    data_ = {}
    substrate = connect()
    data_['traderId'] = trader_id
    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTraderDetail',
        params=[str(trader_id)])  
    if result:
        data_['trader'] = result.value
        data_['trader']['account'] = substrate.ss58_encode(data_['trader']['account'])
        data_['isTrader'] = True
    else:
        data_['isTrader'] = False
    return data_

def get_bazaar_trader_count():
    data_ = {}
    substrate = connect()

    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTraderCount')
    if result:
        data_['traderCount'] = result.value

    return data_

def get_bazaar_trade(trade_id):
    data_ = {}
    substrate = connect()

    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTrade',
        params=[str(trade_id)])         
    if result:
        data_['trade'] = result.value
    else:
        data_['trade'] = None

    return data_

def get_bazaar_trade_count():
    data_ = {}
    substrate = connect()

    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTradeCount')   
    if result:
        data_['tradeCount'] = result.value
    else:
        data_['tradeCount'] = 0

    return data_

def get_bazaar_completed_trade_count():
    data_ = {}
    substrate = connect()

    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarCompletedTradeCount')   
    if result:
        data_['completedTradeCount'] = result.value
    else:
        data_['completedTradeCount'] = 0

    return data_

def get_bazaar_completed_trade_by_trader(trader_id):
    data_ = {}
    substrate = connect()

    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarCompletedTradeByTrader',
        params=[str(trader_id)])                  
    if result:
        data_['completedTradeCount'] = result.value
    else:
        data_['completedTradeCount'] = 0    

    return data_


def get_bazaar_trade_initiated_count():
    data_ = {}
    substrate = connect()

    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTradeInitiatedCount')            
    if result:
        data_['tradeCount'] = result.value
    else:
        data_['tradeCount'] = 0 

    return data_

def get_bazaar_trade_initiated(account_id):
    data_ = {}
    substrate = connect()
    data_['accountId'] = account_id
    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTradeInitiated',
        params=[str(account_id)])  
    if result:
        data_['trade'] = result.value
        data_['result'] = True
    else:
        data_['result'] = False
    return data_


def get_bazaar_trade_initiated_by_trader(trader_id):
    data_ = {}
    substrate = connect()
    data_['traderId'] = trader_id
    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTradeInitiatedByTrader',
        params=[str(trader_id)])  
    if result:
        data_['trade'] = result.value
        data_['result'] = True
    else:
        data_['result'] = False
    return data_


def get_bazaar_trade_escrowed_count():
    data_ = {}
    substrate = connect()

    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTradeEscrowedCount')         
    if result:
        data_['tradeCount'] = result.value
    else:
        data_['tradeCount'] = 0 

    return data_

def get_bazaar_trade_escrowed(account_id):
    data_ = {}
    substrate = connect()
    data_['accountId'] = account_id
    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTradeEscrowed',
        params=[str(account_id)])  
    if result:
        data_['trade'] = result.value
        data_['result'] = True
    else:
        data_['result'] = False
    return data_


def get_bazaar_trade_escrowed_by_trader(trader_id):
    data_ = {}
    substrate = connect()
    data_['traderId'] = trader_id
    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTradeEscrowedByTrader',
        params=[str(trader_id)])  
    if result:
        data_['trade'] = result.value
        data_['result'] = True
    else:
        data_['result'] = False
    return data_

def get_bazaar_trade_money_in_count():
    data_ = {}
    substrate = connect()

    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTradeMoneyInCount')              
    if result:
        data_['tradeCount'] = result.value
    else:
        data_['tradeCount'] = 0 

    return data_

def get_bazaar_trade_money_in(account_id):
    data_ = {}
    substrate = connect()
    data_['accountId'] = account_id
    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTradeMoneyIn',
        params=[str(account_id)])  
    if result:
        data_['trade'] = result.value
        data_['result'] = True
    else:
        data_['result'] = False
    return data_

    return data_

def get_bazaar_trade_money_in_by_trader(trader_id):
    data_ = {}
    substrate = connect()
    data_['traderId'] = trader_id
    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTradeMoneyInByTrader',
        params=[str(trader_id)])  
    if result:
        data_['trade'] = result.value
        data_['result'] = True
    else:
        data_['result'] = False
    return data_

def get_bazaar_trade_money_in_confirmed_count():
    data_ = {}
    substrate = connect()

    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTradeMoneyInConfirmedCount')                
    if result:
        data_['tradeCount'] = result.value
    else:
        data_['tradeCount'] = 0     


    return data_

def get_bazaar_trade_money_in_confirmed(account_id):
    data_ = {}
    substrate = connect()
    data_['accountId'] = account_id
    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTradeMoneyInConfirmed',
        params=[str(account_id)])  
    if result:
        data_['trade'] = result.value
        data_['result'] = True
    else:
        data_['result'] = False
    return data_

def get_bazaar_trade_money_in_confirmed_by_trader(trader_id):
    data_ = {}
    substrate = connect()     
    data_['traderId'] = trader_id
    result = substrate.query(
        module='Bazaar',
        storage_function='BazaarTradeMoneyInConfirmedByTrader',
        params=[str(trader_id)])  
    if result:
        data_['trade'] = result.value
        data_['result'] = True
    else:
        data_['result'] = False
    return data_








def bazaar_initiate_buy(_data):
    data_ = {}
    substrate = connect()

    price = _data['price']
    amount = _data['amount']
    seller = _data['seller']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Bazaar',
        call_function='initiate_buy',
        call_params={
            'price': price,
            'amount': amount,
            'seller': seller
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_

def bazaar_escrow_coin():
    data_ = {}
    substrate = connect()

    trade_id = _data['trade_id']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Bazaar',
        call_function='escrow_coin',
        call_params={
            'trade_id': trade_id
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_

def bazaar_cancel_escrow():
    data_ = {}
    substrate = connect()

    trade_id = _data['trade_id']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Bazaar',
        call_function='cancel_escrow',
        call_params={
            'trade_id': trade_id
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_

def bazaar_transfer_money():
    data_ = {}
    substrate = connect()


    return data_

def bazaar_receive_money():
    data_ = {}
    substrate = connect()


    trade_id = _data['trade_id']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Bazaar',
        call_function='receive_money',
        call_params={
            'trade_id': trade_id
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_

def bazaar_complete():
    data_ = {}
    substrate = connect()
    trade_id = _data['trade_id']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Bazaar',
        call_function='compelete',
        call_params={
            'trade_id': trade_id
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_

def bazaar_register_trader():
    data_ = {}
    substrate = connect()

    name = _data['name']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Bazaar',
        call_function='register_trader',
        call_params={
            'name': name
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_

def bazaar_update_trader():
    data_ = {}
    substrate = connect()


    name = _data['name']
    mnemonic = _data['mnemonic']

    keypair = Keypair.create_from_mnemonic(mnemonic)
    call = substrate.compose_call(
        call_module='Bazaar',
        call_function='update_trader',
        call_params={
            'name': name
    })
    
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_