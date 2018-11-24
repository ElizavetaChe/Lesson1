def get_summ_uppercase(one, two, delimiter='&'):
	return str(one).upper() + str(delimiter) + str(two).upper()
sum_string = get_summ_uppercase('Learn', 'python')
print(sum_string)