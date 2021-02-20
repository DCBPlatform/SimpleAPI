from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

from api.blockchain import connect


def get_all_pairs():
    data_ = {}
    substrate = connect()
    

    data_['pairs'] = []   

    pair_count = substrate.query(
        module='Exchange',
        storage_function='PairCount'
    )
    data_['pairCount'] = pair_count.value
    for i in range(0, pair_count.value):
        pair = substrate.query(
            module='Exchange',
            storage_function='Pair',
            params=[str(i)])
        pair_data = pair.value
        pair_data['pairId'] = str(i)
        data_['pairs'].append(pair_data)    

    data_['nativePairs'] = []   

    native_pair_count = substrate.query(
        module='Exchange',
        storage_function='PairNativeCount'
    )
    data_['nativePairCount'] = native_pair_count.value
    for i in range(0, native_pair_count.value):
        native_pair = substrate.query(
            module='Exchange',
            storage_function='PairNative',
            params=[str(i)])
        native_pair_data = native_pair.value
        native_pair_data['pairId'] = str(i)
        data_['nativePairs'].append(native_pair_data)

    return data_

def get_a_pair(ticker, native=False):
    data_ = {}
    substrate = connect()
    if native:
        pair = substrate.query(
            module='Exchange',
            storage_function='PairNative',
            params=[str(ticker)]) 
    else:
        pair = substrate.query(
            module='Exchange',
            storage_function='Pair',
            params=[str(ticker)]) 
    if pair:
        data_['pairId'] = ticker
        data_['pair'] = pair.value
        data_['pairExist'] = True
    else:
        data_['pair'] = []
        data_['pairExist'] = False
    data_['nativePair'] = native
    return data_

def get_orderbook_for_a_pair(ticker, detail, depth, native=False):
    data_ = {}
    substrate = connect()

    if native:
        pair = substrate.query(
            module='Exchange',
            storage_function='PairNative',
            params=[str(ticker)])             
    else:
        pair = substrate.query(
            module='Exchange',
            storage_function='Pair',
            params=[str(ticker)]) 
    
    data_['nativePair'] = native     
    if pair:
        data_['pairId'] = ticker
        data_['pair'] = pair.value        
        data_['pairExist'] = True
    else:
        data_['pair'] = []
        data_['pairExist'] = False
        return data_         

    if native:
        data_['buyOrders'] = []        
        buy_order_list = substrate.query(
            module='Exchange',
            storage_function='BuyOrderNativeList',
            params=[str(ticker)]) 
        if buy_order_list:
            data_['buyOrderCount'] = len(buy_order_list.value)
            for i in buy_order_list.value:
                buy_order = substrate.query(
                    module='Exchange',
                    storage_function='BuyOrderNative',
                    params=[({
                        'col1': ticker,
                        'col2': str(i)
                    })])
                if buy_order:
                    data_['buyOrders'].append(buy_order.value)   
        else:
            data_['buyOrderCount'] = 0

        data_['sellOrders'] = []    
        sell_order_list = substrate.query(
            module='Exchange',
            storage_function='SellOrderNativeList',
            params=[str(ticker)])   
        if sell_order_list:
            data_['sellOrderCount'] = len(sell_order_list.value)
            for i in sell_order_list.value:
                sell_order = substrate.query(
                    module='Exchange',
                    storage_function='SellOrderNative',
                    params=[({
                        'col1': ticker,
                        'col2': str(i)
                    })])
                if sell_order:
                    data_['sellOrders'].append(sell_order.value)    
        else:
            data_['sellOrderCount'] = 0                                        
    else:
        data_['buyOrders'] = []        
        buy_order_list = substrate.query(
            module='Exchange',
            storage_function='BuyOrderList',
            params=[str(ticker)]) 
        if buy_order_list:
            data_['buyOrderCount'] = len(buy_order_list.value)
            for i in buy_order_list.value:
                buy_order = substrate.query(
                    module='Exchange',
                    storage_function='BuyOrder',
                    params=[({
                        'col1': ticker,
                        'col2': str(i)
                    })])
                if buy_order:
                    data_['buyOrders'].append(buy_order)   
        else:
            data_['buyOrderCount'] = 0                    

        data_['sellOrders'] = []    
        sell_order_list = substrate.query(
            module='Exchange',
            storage_function='SellOrderList',
            params=[str(ticker)])   
        if sell_order_list:
            data_['sellOrderCount'] = len(sell_order_list.value)
            for i in sell_order_list.value:
                sell_order = substrate.query(
                    module='Exchange',
                    storage_function='SellOrder',
                    params=[({
                        'col1': ticker,
                        'col2': str(i)
                    })])
                if sell_order:
                    data_['sellOrders'].append(sell_order)      

        else:
            data_['sellOrderCount'] = 0                    

    return data_

def get_trades_for_a_pair(ticker, detail, limit, start_time, end_time, native=False):
    data_ = {}
    substrate = connect()
    if native:
        pair = substrate.query(
            module='Exchange',
            storage_function='PairNative',
            params=[str(ticker)])             
    else:
        pair = substrate.query(
            module='Exchange',
            storage_function='Pair',
            params=[str(ticker)]) 
    
    data_['nativePair'] = native     
    if pair:
        data_['pairId'] = ticker
        data_['pair'] = pair.value        
        data_['pairExist'] = True
    else:
        data_['pair'] = []
        data_['pairExist'] = False
        return data_         

    if native:
        data_['trades'] = []        
        trade_order_count = substrate.query(
            module='Exchange',
            storage_function='TradeNativeCount',
            params=[str(ticker)]) 
        if trade_order_count:
            data_['tradeCount'] = trade_order_count.value
            for i in range(0, trade_order_count.value):
                trade = substrate.query(
                    module='Exchange',
                    storage_function='TradeNatives',
                    params=[({
                        'col1': ticker,
                        'col2': str(i)
                    })])                
                if trade:          
                    data_['trades'].append(trade.value)   
        else:
            data_['tradeCount'] = 0
                                      
    else:
        data_['trades'] = []        
        trade_order_count = substrate.query(
            module='Exchange',
            storage_function='TradeCount',
            params=[str(ticker)]) 
        if trade_order_count:
            data_['tradeCount'] = trade_order_count.value
            for i in range(0, trade_order_count.value):
                trade = substrate.query(
                    module='Exchange',
                    storage_function='Trades',
                    params=[({
                        'col1': ticker,
                        'col2': str(i)
                    })])
                if trade:
                    data_['trades'].append(trade)   
        else:
            data_['tradeCount'] = 0                           

    return data_


def create_buy_order(ticker, _data, native=False):
    data_ = {}
    substrate = connect()
    if native:
        pair = substrate.query(
            module='Exchange',
            storage_function='PairNative',
            params=[str(ticker)])             
    else:
        pair = substrate.query(
            module='Exchange',
            storage_function='Pair',
            params=[str(ticker)]) 
    
    data_['nativePair'] = native     
    if pair:
        data_['pairId'] = ticker
        data_['pair'] = pair.value        
        data_['pairExist'] = True
    else:
        data_['pair'] = []
        data_['pairExist'] = False
        return data_   

    keypair = Keypair.create_from_mnemonic(_data['mnemonic'])

    if native:
        call_function = 'exchange_order_native_create_buy'
    else:
        call_function = 'exchange_order_create_buy'

    call = substrate.compose_call(
        call_module='Exchange',
        call_function=call_function,
        call_params={
                'pair': str(ticker),
                'volume': _data['volume'],
                'ratio': _data['ratio']
        }
    )

    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_

def cancel_buy_order(ticker, order_id, _data, native=False):
    data_ = {}
    substrate = connect()
    if native:
        pair = substrate.query(
            module='Exchange',
            storage_function='PairNative',
            params=[str(ticker)])             
    else:
        pair = substrate.query(
            module='Exchange',
            storage_function='Pair',
            params=[str(ticker)]) 
    
    data_['nativePair'] = native     
    if pair:
        data_['pairId'] = ticker
        data_['pair'] = pair.value        
        data_['pairExist'] = True
    else:
        data_['pair'] = []
        data_['pairExist'] = False
        return data_    

    return data_

def get_all_buy_order(ticker, native=False):
    data_ = {}
    substrate = connect()
    if native:
        pair = substrate.query(
            module='Exchange',
            storage_function='PairNative',
            params=[str(ticker)])             
    else:
        pair = substrate.query(
            module='Exchange',
            storage_function='Pair',
            params=[str(ticker)]) 
    
    data_['nativePair'] = native     
    if pair:
        data_['pairId'] = ticker
        data_['pair'] = pair.value        
        data_['pairExist'] = True
    else:
        data_['pair'] = []
        data_['pairExist'] = False
        return data_         

    if native:
        data_['buyOrders'] = []        
        buy_order_list = substrate.query(
            module='Exchange',
            storage_function='BuyOrderNativeList',
            params=[str(ticker)]) 
        if buy_order_list:
            data_['buyOrderCount'] = len(buy_order_list.value)
            for i in buy_order_list.value:
                buy_order = substrate.query(
                    module='Exchange',
                    storage_function='BuyOrderNative',
                    params=[({
                        'col1': ticker,
                        'col2': str(i)
                    })])
                if buy_order:
                    data_['buyOrders'].append(buy_order.value)   
        else:
            data_['buyOrderCount'] = 0
                                     
    else:
        data_['buyOrders'] = []        
        buy_order_list = substrate.query(
            module='Exchange',
            storage_function='BuyOrderList',
            params=[str(ticker)]) 
        if buy_order_list:
            data_['buyOrderCount'] = len(buy_order_list.value)
            for i in buy_order_list.value:
                buy_order = substrate.query(
                    module='Exchange',
                    storage_function='BuyOrder',
                    params=[({
                        'col1': ticker,
                        'col2': str(i)
                    })])
                if buy_order:
                    data_['buyOrders'].append(buy_order)   
        else:
            data_['buyOrderCount'] = 0                                     

    return data_    

def create_sell_order(ticker, _data, native=False):
    data_ = {}
    substrate = connect()

    if native:
        pair = substrate.query(
            module='Exchange',
            storage_function='PairNative',
            params=[str(ticker)])             
    else:
        pair = substrate.query(
            module='Exchange',
            storage_function='Pair',
            params=[str(ticker)]) 
    
    data_['nativePair'] = native     
    if pair:
        data_['pairId'] = ticker
        data_['pair'] = pair.value        
        data_['pairExist'] = True
    else:
        data_['pair'] = []
        data_['pairExist'] = False
        return data_    

    keypair = Keypair.create_from_mnemonic(_data['mnemonic'])

    if native:
        call_function = 'exchange_order_native_create_sell'
    else:
        call_function = 'exchange_order_create_sell'

    call = substrate.compose_call(
        call_module='Exchange',
        call_function=call_function,
        call_params={
                'pair': str(ticker),
                'volume': _data['volume'],
                'ratio': _data['ratio']
        }
    )

    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)
    data_['extrinsic'] = extrinsic.value
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    data_['receiptExtrinsicHash'] = receipt.extrinsic_hash
    data_['receipBlockHash'] = receipt.block_hash

    return data_

def cancel_sell_order(ticker, order_id, _data, native=False):
    data_ = {}
    substrate = connect()

    if native:
        pair = substrate.query(
            module='Exchange',
            storage_function='PairNative',
            params=[str(ticker)])             
    else:
        pair = substrate.query(
            module='Exchange',
            storage_function='Pair',
            params=[str(ticker)]) 
    
    data_['nativePair'] = native     
    if pair:
        data_['pairId'] = ticker
        data_['pair'] = pair.value        
        data_['pairExist'] = True
    else:
        data_['pair'] = []
        data_['pairExist'] = False
        return data_    

    return data_

def get_all_sell_order(ticker, native=False):
    data_ = {}
    substrate = connect()

    if native:
        pair = substrate.query(
            module='Exchange',
            storage_function='PairNative',
            params=[str(ticker)])             
    else:
        pair = substrate.query(
            module='Exchange',
            storage_function='Pair',
            params=[str(ticker)]) 
    
    data_['nativePair'] = native     
    if pair:
        data_['pairId'] = ticker
        data_['pair'] = pair.value        
        data_['pairExist'] = True
    else:
        data_['pair'] = []
        data_['pairExist'] = False
        return data_    

    if native:

        data_['sellOrders'] = []    
        sell_order_list = substrate.query(
            module='Exchange',
            storage_function='SellOrderNativeList',
            params=[str(ticker)])   
        if sell_order_list:
            data_['sellOrderCount'] = len(sell_order_list.value)
            for i in sell_order_list.value:
                sell_order = substrate.query(
                    module='Exchange',
                    storage_function='SellOrderNative',
                    params=[({
                        'col1': ticker,
                        'col2': str(i)
                    })])
                if sell_order:
                    data_['sellOrders'].append(sell_order.value)    
        else:
            data_['sellOrderCount'] = 0                                        
    else:                

        data_['sellOrders'] = []    
        sell_order_list = substrate.query(
            module='Exchange',
            storage_function='SellOrderList',
            params=[str(ticker)])   
        if sell_order_list:
            data_['sellOrderCount'] = len(sell_order_list.value)
            for i in sell_order_list.value:
                sell_order = substrate.query(
                    module='Exchange',
                    storage_function='SellOrder',
                    params=[({
                        'col1': ticker,
                        'col2': str(i)
                    })])
                if sell_order:
                    data_['sellOrders'].append(sell_order)      

        else:
            data_['sellOrderCount'] = 0                    

    return data_  
