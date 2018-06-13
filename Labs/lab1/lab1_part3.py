base10size = 512
base2size = base10size * 10 **(9) // 2**30
lost_size = base10size - base2size

print(base10size, "GB in base 10 is actually", base2size, "in base 2,", lost_size, "less than advertised.")

