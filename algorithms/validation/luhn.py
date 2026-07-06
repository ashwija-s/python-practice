def card_number_validator(dig):
    dig = dig.replace(" ", "").replace("-","")
    dig = [int(d) for d in dig]
    for i in range(len(dig) - 2, -1, -2):
        dig[i] = dig[i] * 2
        if dig[i] > 9:
            dig[i] = dig[i] - 9
    total = 0
    for i in range(len(dig)):
        total += dig[i]
    if total % 10 != 0:
        return "INVALID!"
    else:
        return "VALID!"