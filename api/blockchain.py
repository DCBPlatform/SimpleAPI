from substrateinterface.contracts import ContractCode, ContractInstance
from substrateinterface import SubstrateInterface, Keypair
from scalecodec.type_registry import load_type_registry_file

from decouple import config

import ssl
from websocket import create_connection, WebSocketConnectionClosedException

ws = create_connection("wss://2.dcb.my",sslopt={"cert_reqs": ssl.CERT_NONE})
custom_type_registry = load_type_registry_file("api/custom.json")

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

def connect():
    substrate = SubstrateInterface(
        websocket=ws,
        ss58_format=42,
        type_registry_preset='substrate-node-template',
        type_registry=custom_type_registry
    )
    return substrate

try:
    substrate = connect()
except WebSocketConnectionClosedException:
    substrate = connect()

# substrate = SubstrateInterface(
#         url="wss://2.dcb.my",
#         ss58_format=42,
#         type_registry_preset='substrate-node-template',
#         type_registry=custom_type_registry
# )