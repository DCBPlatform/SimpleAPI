from substrateinterface.contracts import ContractCode, ContractInstance
from substrateinterface import SubstrateInterface, Keypair

import ssl 

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

substrate = SubstrateInterface(
    url="wss://1.dcb.my",
    ss58_format=42,
    type_registry_preset='substrate-node-template'
)