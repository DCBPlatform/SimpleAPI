from substrateinterface.contracts import ContractCode, ContractInstance
from substrateinterface import SubstrateInterface, Keypair

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

substrate = SubstrateInterface(
    url="https://1.dcb.my",
    ss58_format=42,
    type_registry_preset='substrate-node-template'
)