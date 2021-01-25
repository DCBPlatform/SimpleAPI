from substrateinterface.contracts import ContractCode, ContractInstance
from substrateinterface import SubstrateInterface, Keypair

import ssl
from websocket import create_connection
ws = create_connection("wss://1.dcb.my",sslopt={"cert_reqs": ssl.CERT_NONE})

substrate = SubstrateInterface(
    websocket=ws,
    ss58_format=42,
    type_registry_preset='substrate-node-template'
)

result = substrate.query(
    module='System',
    storage_function='Account',
    params=['5EUxFDn9K7GQhLNxGHsCcTeXNuuFUVmSfV4fkdLjgm4VyNdq']
)

print(result) #  7695
#print(result.value['data']['free']) # 635278638077956496
