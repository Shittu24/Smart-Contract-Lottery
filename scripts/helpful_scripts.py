from brownie import network, accounts, config, MockV3Aggregator, VRFCoordinator, Contract


FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

def get_account(index=None, id=None):

    if index:
        return accounts[index]

    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or 
        network.show_active() in FORKED_LOCAL_ENVIRONMENTS 
    ):
        returnaccounts[0]

# During execution, if the above conditons are not met, it will automtically execute the below instructions: It becomes default 
    
    return accounts.add(config["wallets"]["from_key"])

contract_to_mock = {"eth_usd_price_feed": MockV3Aggregator,
"vrf_coordinator": VRFCoordinatorMock,
}


def get_contract(contract_name):

    contract_type = contract_to_mock[contact_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(contract_type) <=0:
        #MockV3Aggregator.lengt
            deploy_mocks()
        contract = contract_type[-1]
        # MockV3Aggregator[-1]
    else:
        contract_address = config(["network"] [network.show_active()] [contract_name])
            #Adress
            #ABI

        contract = Contract.from_abi(contract_type._name, contract_address, contract_type.abi)
            # MockV3Aggregator.abi

    return contract

DECIMALS = 8
INITIAL_VALUE = 2000

def deploy_mocks(decimals=DECIMALS, initial_value=INITIAL_VALUE):
    account = get_account()
    MockV3Aggregator.deploy(
        decimals, initial_value, {"from":account}
    )
    print("Deployed!")





def main():
    get_account()