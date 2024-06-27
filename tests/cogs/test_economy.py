import pytest
from redbot.pytest.economy import *
from redbot.core import errors


async def test_bank_register(bank, ctx):
    default_bal = await bank.get_default_balance(ctx.guild)
    assert default_bal == (await bank.get_account(ctx.author)).balance


async def has_account(member, bank):
    balance = await bank.get_balance(member)
    if balance == 0:
        balance = 1
    await bank.set_balance(member, balance)


async def test_bank_transfer(bank, member_factory):
    mbr1 = member_factory.get()
    mbr2 = member_factory.get()
    bal1 = (await bank.get_account(mbr1)).balance
    bal2 = (await bank.get_account(mbr2)).balance
    await bank.transfer_credits(mbr1, mbr2, 50)
    newbal1 = (await bank.get_account(mbr1)).balance
    newbal2 = (await bank.get_account(mbr2)).balance
    assert bal1 - 50 == newbal1
    assert bal2 + 50 == newbal2


async def test_bank_set(bank, member_factory):
    mbr = member_factory.get()
    await bank.set_balance(mbr, 250)
    acc = await bank.get_account(mbr)
    assert acc.balance == 250

async def test_bank_can_spend(bank, member_factory):
    mbr = member_factory.get()
    canspend = await bank.can_spend(mbr, 50)
    assert canspend == (50 < await bank.get_default_balance(mbr.guild))
    await bank.set_balance(mbr, 200)
    acc = await bank.get_account(mbr)
    canspendnow = await bank.can_spend(mbr, 100)
    assert canspendnow
    print("yeeeeeeeeeeeeet123")


async def test_set_bank_name(bank, guild_factory):
    guild = guild_factory.get()
    await bank.set_bank_name("Test Bank", guild)
    name = await bank.get_bank_name(guild)
    assert name == "Test Bank"


async def test_set_currency_name(bank, guild_factory):
    guild = guild_factory.get()
    await bank.set_currency_name("Coins", guild)
    name = await bank.get_currency_name(guild)
    assert name == "Coins"


async def test_set_default_balance(bank, guild_factory):
    guild = guild_factory.get()
    await bank.set_default_balance(500, guild)
    default_bal = await bank.get_default_balance(guild)
    assert default_bal == 500


async def test_nonint_transaction_amount(bank, member_factory):
    mbr1 = member_factory.get()
    mbr2 = member_factory.get()
    with pytest.raises(TypeError):
        await bank.deposit_credits(mbr1, 1.0)
    with pytest.raises(TypeError):
        await bank.withdraw_credits(mbr1, 1.0)
    with pytest.raises(TypeError):
        await bank.transfer_credits(mbr1, mbr2, 1.0)

async def test_bank_set(bank, member_factory):
    mbr = member_factory.get()
    with pytest.raises(ValueError):
        await bank.set_balance(mbr, -1)

    with pytest.raises(TypeError):
        await bank.set_balance(mbr, "1")

    with pytest.raises(errors.BalanceTooHigh):
        await bank.set_balance(mbr,  2 ** 63)
    
    await bank.set_global(True)
    bank.set_balance(mbr, 100)
    assert await bank.get_balance(mbr) == 100

async def test_bank_withdraw(bank, member_factory):
    mbr = member_factory.get()
    with pytest.raises(TypeError):
        await bank.withdraw_credits(mbr, 1.0)
    with pytest.raises(ValueError):
        await bank.withdraw_credits(mbr, -1)
    await bank.set_balance(mbr, 100)
    with pytest.raises(ValueError):
        await bank.withdraw_credits(mbr, 101)

async def test_get_account(bank, member_factory):
    mbr = member_factory.get()
    await bank.set_global(True)
    await bank.get_account(mbr)
    await bank.set_global(False)

async def test_get_bank_name(bank, guild_factory):
    guild = guild_factory.get()
    with pytest.raises(RuntimeError):
        await bank.get_bank_name(guild=None)

    await bank.set_global(True)
    await bank.get_bank_name(guild=guild)
    await bank.set_global(False)