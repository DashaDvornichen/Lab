my_string = "Дана строка, состоящая из слов , пробелов и знаков препинания. " \
            "На основании этой строки создайте новую (и выведите ее на консоль):"
new_string = list(filter(lambda x: x[-2:] == 'ов', my_string.split()))
print(new_string)
