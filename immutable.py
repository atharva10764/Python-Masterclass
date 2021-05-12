# result = False
# another_result = result
#
# print(id(result))
# print(id(another_result))
# result=True
# print(id(result))
#

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ism"
print(id(result))
print(id(another_result))


