from substrateinterface.contracts import ContractCode, ContractInstance
from substrateinterface import SubstrateInterface, Keypair

from decouple import config

import ssl
from websocket import create_connection, WebSocketConnectionClosedException



substrate = SubstrateInterface(
    websocket=config('NODE_URL'),
    ss58_format=42,
    type_registry_preset='substrate-node-template'
)
