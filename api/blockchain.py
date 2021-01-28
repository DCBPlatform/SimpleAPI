from substrateinterface.contracts import ContractCode, ContractInstance
from substrateinterface import SubstrateInterface, Keypair

from decouple import config

import ssl
from websocket import create_connection, WebSocketConnectionClosedException



def connect():
    ws = create_connection(config('NODE_URL'),
        max_size=2 ** 32,
        read_limit=2 ** 32,
        write_limit=2 ** 32,
        sslopt={"cert_reqs": ssl.CERT_NONE})

    return ws

substrate = SubstrateInterface(
    websocket=connect(),
    ss58_format=42,
    type_registry_preset='substrate-node-template'
)
