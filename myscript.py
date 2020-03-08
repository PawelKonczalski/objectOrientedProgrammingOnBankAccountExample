from bankaccount import BankAccount, MinimumBalanceAccount

accountMin = MinimumBalanceAccount(1500, 1000)

result = accountMin.try_withdraw(300)

if result.is_ok():
    print(result.message)
