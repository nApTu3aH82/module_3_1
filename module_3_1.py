def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return(len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    bool = False
    for count in range(int(len(list_to_search))):
        if string.upper() == list_to_search[count].upper():
            bool = True
    return(bool)

calls = 0
print(string_info('Capibara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)