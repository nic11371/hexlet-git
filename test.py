def maximumWealth(accounts):
    customer_amount = []
    for customer in accounts:
        sum_amount = 0
        for amount in customer:
            sum_amount += amount
            customer_amount.append(sum_amount)
    return max(customer_amount)


print(maximumWealth([[1,5],[7,3],[3,5]]))
