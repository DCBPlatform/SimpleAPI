from substrateinterface.contracts import ContractCode, ContractInstance
from substrateinterface import SubstrateInterface, Keypair

from decouple import config

import ssl
from websocket import create_connection
ws = create_connection(config('NODE_URL'),sslopt={"cert_reqs": ssl.CERT_NONE})



substrate = SubstrateInterface(
    websocket=ws,
    ss58_format=42,
    type_registry_preset='substrate-node-template'
)

