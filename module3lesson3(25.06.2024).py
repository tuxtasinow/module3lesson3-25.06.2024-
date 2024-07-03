def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(a, b, c)
print_params(a,b)
print_params(a, b, c ,d)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [1, '2', 2.5]
values_dict = {'a' : 11, 'b' : 'Hi', 'c' : 3.14}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [False, 3.15]
print_params(*values_list_2, 42)