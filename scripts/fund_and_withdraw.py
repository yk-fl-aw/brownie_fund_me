from brownie import FundMe1
from scripts.helper import get_account


def fund():
    fund_me = FundMe1[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entrance fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe1[-1]
    account = get_account()
    print("Withdraw")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
