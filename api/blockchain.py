from substrateinterface.contracts import ContractCode, ContractInstance
from substrateinterface import SubstrateInterface, Keypair

from decouple import config

import ssl
from websocket import create_connection, WebSocketConnectionClosedException

ws = create_connection("wss://1.dcb.my",sslopt={"cert_reqs": ssl.CERT_NONE})

def connect():
    substrate = SubstrateInterface(
        websocket=ws,
        ss58_format=42,
        type_registry_preset='substrate-node-template'
    )
    return substrate

try:
    substrate = connect()
except WebSocketConnectionClosedException:
    substrate = connect()
