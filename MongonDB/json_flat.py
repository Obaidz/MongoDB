
import json, sys
import urllib.request as request

x = {}
# This methid is to remove 's' from https, because https won't alllow to get data into terminal
def sub_str():
    firstname = input('Enter JSON link: ')
    if firstname[0] == 'h' and firstname[1] == 't' and firstname[2] == 't' and firstname[3] == 'p' and firstname[4] == 's':
        x = firstname[0:4] + firstname[5:]
        return x
    else:
        return firstname

# This method get api from sub_str() and copies all data into varibale and returns it.
def api_method():
    with request.urlopen(sub_str()) as response:
        if response.getcode() == 200:
            source = response.read()
            data = json.loads(source)
        else:
            print('An error occurred while attempting to retrieve data from the API.')
        
        for item, value in data.items():
            if type(value) == list:
                print('\n')
                return 'Your JSON file contains an arry input. Please use a JSON file without input array in it. Thanks'
        
        print('\n Results from API: \n', data)
        print('\n')
        return data


# This method Flats the nested JSON object into a simple one.
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '.')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


# If link option is not selected by the user then own_file will falt the jata given in 'test.json' file.
def own_file():
    with open('test.json') as f:
        data = json.load(f)
    
        for item, value in data.items():
            if type(value) == list:
                print('\n')
                return 'Your JSON file contains an arry input. Please use a JSON file without input array in it. Thanks'   
        return data



# Giving user an option to falt either the given json in test.json file or paste a web api for json.
print('Two options are available: \n 1) Enter 1 to preceed without an API link for JSON onject \n 1) Enter 2 to preceed with an API link for JSON onject')
firstname = input('Enter Your option: ')
if firstname == '1':
    print('Given JSON object: \n',own_file())
    f = flatten_json(own_file())
    print('After Flattening: \n',f)  
elif firstname == '2':
    
    f = flatten_json(api_method())

    print('Results after Flat:')
    print(f)
else:
    print('Wrong Option selected \n quitting...')
    sys.exit(0)

