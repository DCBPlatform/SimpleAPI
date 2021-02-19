from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

from api.blockchain import substrate

# from scalecodec.type_registry import load_type_registry_file
# custom_type_registry = load_type_registry_file("api/custom.json")

def get_all_pairs():
    data_ = {}

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
        data_['pairs'].append(pair.value)    

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
        data_['nativePairs'].append(native_pair.value)

    return data_

def get_a_pair(ticker, native=False):
    data_ = {}
    pair = substrate.query(
        module='Exchange',
        storage_function='PairNative',
        params=['0'])          
    print(pair)           
    return data_

def get_orderbook_for_a_pair(ticker, detail, depth):
    data_ = {}
    return data_

def get_trades_for_a_pair(ticker, detail, limit, start_time, end_time):
    data_ = {}
    return data_

def get_all_matched_order(ticker):
    data_ = {}
    return data_

def get_a_matched_order(ticker, match_id):
    data_ = {}
    return data_

def create_buy_order(ticker, _data):
    data_ = {}
    return data_

def update_buy_order(ticker, order_id, _data):
    data_ = {}
    return data_

def cancel_buy_order(ticker, order_id, _data):
    data_ = {}
    return data_

def get_all_buy_order(ticker):
    data_ = {}
    return data_

def get_a_buy_order(ticker, order_id):
    data_ = {}
    return data_

def create_sell_order(ticker, _data):
    data_ = {}
    return data_

def update_sell_order(ticker, order_id, _data):
    data_ = {}
    return data_

def cancel_sell_order(ticker, order_id, _data):
    data_ = {}
    return data_

def get_all_sell_order(ticker):
    data_ = {}
    return data_

def get_a_sell_order(ticker, order_id):
    data_ = {}
    return data_