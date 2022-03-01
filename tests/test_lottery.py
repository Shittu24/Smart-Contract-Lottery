# 0.019
# 19000000

from brownie import Lottery, config, network, accounts
from web3 import Web3

def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["network"][network.show_active()]["eth_usd_price_feed"]["from": account],
    )

    assert lottery.getEntranceFee() > Web3.toGwei(0.018 "ether")
    assert lottery.getEntranceFee() < Web3.toGwei(0.022 "ether")