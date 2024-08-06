import re

calls = 0
def count_calls():
    global calls
    calls += 1
def string_info (string):
    str_info = (len(string), string.upper(), string.lower())
    print (str_info)
    count_calls()
def is_contains(string, *list_to_search):
    if type(string) != str:
        if string in list_to_search:
            print(True)
        else:
            print(False)
    else:
        if string.casefold() in str(list_to_search).casefold():
            print(True)
        else:
            print(False)
    count_calls()
string_info('1st try')
is_contains(1, 7, 12, 1, 0)
string_info('Finally')
is_contains('False', 4, 'list', True, '7')
is_contains('TeSt', 'Test', 99, 'seven')
print(calls)