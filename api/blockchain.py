from substrateinterface.contracts import ContractCode, ContractInstance
from substrateinterface import SubstrateInterface, Keypair

from decouple import config

import ssl
from websocket import create_connection, WebSocketConnectionClosedException



substrate = SubstrateInterface(
    url='wss://1.dcb.my',
    ss58_format=42,
    type_registry_preset='substrate-node-template'
)

def connect():
    substrate = SubstrateInterface(
        url='wss://1.dcb.my',
        ss58_format=42,
        type_registry_preset='substrate-node-template'
    )    
    return substrate
