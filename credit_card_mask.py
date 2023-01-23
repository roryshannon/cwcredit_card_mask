def credit_card_mask(cc):

    return ('#'*(len(cc)-4) +'{}{}{}{}').format(*cc[-4:]) if len(cc)>4 else cc

 

print(credit_card_mask("1234567890123456"))
