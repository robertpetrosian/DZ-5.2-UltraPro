import divisor_master

LST_SIMPLE= divisor_master.get_simple(10**3)
print(len(LST_SIMPLE))
print(divisor_master.lst_dividers(1))
print(divisor_master.max_divider(0))
print(divisor_master.max_divider(113))
print(divisor_master.factorize(1000))
print(divisor_master.factorize(12010))
print([1,2,3]+[1,2,3])
dct_name = {1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine'}
print(dct_name[5])
dn=lambda x: dct_name[x]
print(dn(1))