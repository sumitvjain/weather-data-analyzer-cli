import os, sys, json 
from pprint import pprint

from colorama import Fore, Back, Style

import random
colors = [Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTMAGENTA_EX, Fore.CYAN, Fore.LIGHTRED_EX, Fore.LIGHTBLACK_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTRED_EX]


# Data will save in json file.
def json_data_dumps(fle_dir_pth, data_for_json):
    """
    fle_dir_pth: Python file directory path
    data_for_json: dictionary{key:value}
    """
    json_fle_nm = 'average_temperatures.json'
    json_new_fle_full_pth = os.path.join(fle_dir_pth, json_fle_nm)

    open_json_file = open(json_new_fle_full_pth, 'w') 
    json.dump(data_for_json, open_json_file, indent=4)
    print('Successful stored data in json file')


# Check json file is empty or having data for search/process.
def check_json_data(json_full_pth):
    """
    param: json full path (with file name and extention)
    return: bln
    """
    if os.path.getsize(json_full_pth) == 0:
        print('[Info] :  json file is empty!')     

        return False 
    else:
        return True


# Get average value.
def get_average(temp_vals):
    """
    param: list of integer value like [30, 28]
    return: average value of the list like 29.0
    """
    val_ = sum(temp_vals) / len(temp_vals)
    return val_


# Get data from json file.
def get_data_from_json_file(json_full_pth):
    """
    param: json file full path
    return: json file data
    example: 
    [{'city': 'New York', 'temperature': 30},
    {'city': 'Los Angeles', 'temperature': 25},
    {'city': 'New York', 'temperature': 28},
    ]
    """
    try:
        is_json_data = check_json_data(json_full_pth)   
        if is_json_data:
            with open(json_full_pth , 'r') as rd:
                data = json.load(rd)
        return data
    except Exception as e:
        print(e)
        sys.exit(1)


# Show sepcific city temperature value which is provided from user.
def display_specific_city_temp(fle_dir_pth, json_full_pth, city_name_):
    """
    fle_dir_pth: python file directory path
    json_full_path: json file full path(with file name)
    city_name_: specific city name for search data
    print: Average temperature value for provided city name 
    """
    data = get_data_from_json_file(json_full_pth)

    city_found = False
    data_for_json = {}

    temperature_data = []
    for dic_ in data:
        if dic_['city'] == city_name_:
            city_found = True
            temperature_data.append(dic_['temperature'])
            data_for_json[city_name_] = dic_['temperature']

    if not city_found:
        print('[Info]: city not found in json file..')
        sys.exit(0)

    if temperature_data:
        ave_temp = get_average(temperature_data)
        print(Fore.CYAN + 'Average Temperatures:')
        print(random.choice(colors) + f'{city_name_}: {ave_temp}')
        if data_for_json != {}:    
            json_data_dumps(fle_dir_pth, data_for_json)

    else:
        print(f'[Error]: Temperature data not found for this {city_name_} city')
        sys.exit(1)


# Convert temperature value into fahrenheit value.
def convert_temp_to_fahrenheit(fle_dir_pth, json_full_pth):
    """
    fle_dir_pth: python file directory path
    json_full_path: json file full path(with file name)    
    print: Fahrenheit value for city
    """
    data = get_data_from_json_file(json_full_pth)

    data_for_json = {}
    data_dict = {}
    for dic_ in data:
        if dic_['city'] in data_dict:
            data_dict[dic_['city']] += [dic_['temperature']]
        else:
            data_dict[dic_['city']] = [dic_['temperature']]

    print(Fore.CYAN + 'Average Fahrenheit Temperatures:')
    for city_nm in data_dict:
        ave_temp = get_average(data_dict[city_nm])
        fahrenheit_temperature = (ave_temp * 9/5) + 32
        data_for_json[city_nm] = fahrenheit_temperature
        print(random.choice(colors) + f'- {city_nm}: {fahrenheit_temperature}')

    if data_for_json != {}:    
        json_data_dumps(fle_dir_pth, data_for_json)

# Show the all city name.
def print_city_nm(json_full_pth):
    """
    param: full json file path(with file name and extention)
    print: List for all city name from json file
    """
    data = get_data_from_json_file(json_full_pth)

    weather_data_city_names = []
    for dic_ in data:
        if dic_['temperature']:
            weather_data_city_names.append(dic_['city'])
    
    weather_data_city_names = list(set(weather_data_city_names))

    print(Fore.CYAN + 'Available Cities:')
    for city_nm in weather_data_city_names:
        print(random.choice(colors) + f'- {city_nm}')
        


# Calculate all city temperatue Average value and display it.
def calculate_display_average(fle_dir_pth, json_full_pth):
    """
    fle_dir_pth: Python file directory path
    json_full_pth: Json file full path (with file name and extention)
    print: Average temperatue value for all city
    """

    data = get_data_from_json_file(json_full_pth)

    data_dict = {}
    for dic_ in data:
        if dic_['city'] in data_dict:
            data_dict[dic_['city']] += [dic_['temperature']]
        else:
            data_dict[dic_['city']] = [dic_['temperature']]
            
    print(Fore.CYAN + 'Average Temperatures:')
    data_for_json = {}
    
    for city_nm in data_dict:
        ave_temp = get_average(data_dict[city_nm])
        data_for_json[city_nm] = ave_temp
        print(random.choice(colors) + f'- {city_nm}: {ave_temp}')

    if data_for_json != {}:    
        json_data_dumps(fle_dir_pth, data_for_json)

    else:
        print('[Error]: data dict is empty.')
   


# Check data stored json file is available or not.
def is_json_fle_exist(json_full_pth):
    try:
        # json_full_pth = os.path.join(fle_dir_pth, 'weather.json')
        if os.path.isfile(json_full_pth):
            return True
        else:
            return False
    except FileNotFoundError as fl:
        print(fl)


# Check python file name like sys.argv[0]
def check_file_nm(fle_dir_pth):
    try:
        full_file_path = os.path.join(fle_dir_pth, sys.argv[0])
        if os.path.isfile(full_file_path):
            return True
        else:
            return False
    except FileNotFoundError as fl:
        print(fl)
        sys.exit(1)


# Display instruction and usage of the tool.
def print_help():
    info = """
        Weather CLI Tool Usage:

        python weather_cli.py [OPTIONS]

        This CLI tool reads weather data from a JSON file, calculates the average temperature for each city,
        writes the results to a new JSON file, and prints the average temperatures in the terminal with colored output.

        Arguments:
            --help Show this help message and exit.
            --city CITY_NAME Calculate and display the average temperature for the specified city only.
            --convert UNIT Convert temperatures to 'fahrenheit' or 'celsius' (default is Celsius).

        Examples:
            python weather_cli.py
            python weather_cli.py --list
            python weather_cli.py --city New York
            python weather_cli.py --convert fahrenheit

        """
    
    print(info)


# Used edge case for starting programe.
# sanity check in-between functions.
def start(fle_dir_pth):

    try:

        is_py_fle_exist = check_file_nm(fle_dir_pth)

        if is_py_fle_exist:

            json_full_pth = os.path.join(fle_dir_pth, 'weather.json')
            if is_json_fle_exist(json_full_pth):
                arg_len = len(sys.argv)

                if arg_len == 1:
                    calculate_display_average(fle_dir_pth, json_full_pth)
                    sys.exit(0)

                elif arg_len == 2:
                    arg_2 = sys.argv[1]
                    if arg_2 in ['--help', '--list']:
                        if arg_2 == '--help':
                            print_help()
                        else:
                            print_city_nm(json_full_pth)
                    else:
                        print('[Error]: Invalid argument!')
                        print('Please check using (--help) command.')

                elif arg_len == 3:
                    arg_2 = sys.argv[1]
                    arg_3 = sys.argv[2]

                    if arg_2 == '--convert':
                        if arg_3 == 'fahrenheit':
                            convert_temp_to_fahrenheit(fle_dir_pth, json_full_pth)
                        else:
                            print('[Error]: Invalid argument!')
                            print('Please check using (--help) command.')

                    elif arg_2 == '--city':
                        display_specific_city_temp(fle_dir_pth, json_full_pth, arg_3)

                    else:
                        print('[Error]: Invalid argument!')
                        print('Please check using (--help) command.')

                else:
                    print('[Error]: Takes 3 position arguments but {arg_len} were given.' )
                    return False
            else:
                print('[Error]: weather.json file does not exists!')
                sys.exit(1)

        else:
            print('[Error]: File not found!')
            sys.exit(1)

    except Exception as e:
        print(e)
        sys.exit(1)
    


# Programe will start from here.
def main():

    try:       
        fle_dir_pth = os.path.dirname(os.path.abspath(__name__))        
        start(fle_dir_pth)   
    except Exception as e:
        print(e)
        sys.argv(1)
 

if __name__ == '__main__':
    main()





