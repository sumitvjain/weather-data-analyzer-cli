import os, sys, json 
from pprint import pprint

from colorama import Fore, Back, Style

import random
colors = [Fore.LIGHTYELLOW_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTMAGENTA_EX, Fore.CYAN, Fore.LIGHTRED_EX]


def json_data_dumps(fle_dir_pth, data_for_json):
    json_fle_nm = 'average_temperatures.json'
    json_new_fle_full_pth = os.path.join(fle_dir_pth, json_fle_nm)

    open_json_file = open(json_new_fle_full_pth, 'w') 
    json.dump(data_for_json, open_json_file, indent=4)
    print('Successful created new json file and written with average temperature for all city')


def get_average(temp_vals):
    val_ = sum(temp_vals) / len(temp_vals)
    return val_


def check_json_data(json_full_pth):

    if os.path.getsize(json_full_pth) == 0:
        print('[Info] :  json file is empty!')
        
        return False 
    else:
        return True


def get_average(temp_vals):
    val_ = sum(temp_vals) / len(temp_vals)
    return val_


def get_data_from_json_file(fle_dir_pth, json_full_pth):
    try:
        is_json_data = check_json_data(json_full_pth)   
        if is_json_data:
            with open(json_full_pth , 'r') as rd:
                data = json.load(rd)
        return data
    except Exception as e:
        print(e)
        sys.exit(1)


def display_specific_city_temp(fle_dir_pth, json_full_pth, city_name_):
    print('wip code.....')


def convert_temp_to_fahrenheit():
    print('wip code.....')


def print_city_nm(fle_dir_pth, json_full_pth):
    data = get_data_from_json_file(fle_dir_pth, json_full_pth)

    weather_data_city_names = []
    for dic_ in data:
        if dic_['temperature']:
            weather_data_city_names.append(dic_['city'])
    
    weather_data_city_names = list(set(weather_data_city_names))

    print(Fore.CYAN + 'Available Cities:')
    for city_nm in weather_data_city_names:
        print(random.choice(colors) + city_nm)
        


def calculate_display_average(fle_dir_pth, json_full_pth):

    data = get_data_from_json_file(fle_dir_pth, json_full_pth)

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
        print(random.choice(colors) + f'{city_nm}: {ave_temp}')

    if data_for_json != {}:    
        json_data_dumps(fle_dir_pth, data_for_json)

    else:
        print('[Error]: data dict is empty.')
   


def is_json_fle_exist(fle_dir_pth, json_full_pth):
    try:
        # json_full_pth = os.path.join(fle_dir_pth, 'weather.json')
        if os.path.isfile(json_full_pth):
            return True
        else:
            return False
    except FileNotFoundError as fl:
        print(fl)


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


def start(fle_dir_pth):

    try:

        is_py_fle_exist = check_file_nm(fle_dir_pth)

        if is_py_fle_exist:

            json_full_pth = os.path.join(fle_dir_pth, 'weather.json')
            if is_json_fle_exist(fle_dir_pth, json_full_pth):
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
                            print_city_nm(fle_dir_pth, json_full_pth)
                    else:
                        print('[Error]: Invalid argument!')
                        print('Please check using (--help) command.')

                elif arg_len == 3:
                    arg_2 = sys.argv[1]
                    arg_3 = sys.argv[2]

                    if arg_2 == '--convert':
                        if arg_3 == ' fahrenheit':
                            convert_temp_to_fahrenheit()
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
    


def main():
    try:
        
        fle_dir_pth = os.path.dirname(os.path.abspath(__name__))
        
        start(fle_dir_pth)
   

    except Exception as e:
        print(e)
        sys.argv(1)
 


if __name__ == '__main__':
    main()





