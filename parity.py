def calculate_parity(code):
	code = format(code, "b")
	return int(code + str(xor_all_bits(code)), 2)
def check_parity(code):
	code = bin(code)[2:]
	return xor_all_bits(code[:-1]) == int(code[-1])
	
def xor_all_bits(bits):
	return reduce(lambda x,y: int(x) ^ int(y), bits) 

code = 0b111011010101
with_parity = calculate_parity(code)
parity_check =  check_parity(with_parity)
print "Code = ", bin(code), ", With Parity = ", bin(with_parity), ", Parity Check: ", parity_check	