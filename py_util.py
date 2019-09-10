
import math;
import os;
import datetime, calendar;
import platform;
import pycountry;
import pandas as pd;
from .py_macosfile import pickle_load, pickle_dump 


def isstring(value):
    return isinstance(value, str);

def isnan(value):
    if isstring(value):
        if value.lower() == "nan":
            return True;
        else:
            return False;
    else:
        return math.isnan(float(value));

def check_file_existence(filename):
    return os.path.isfile(filename);

def traverse_folder(root_path):
    file_list = []
    for dirName, subdirList, fileList in os.walk(root_path):
        for fname in fileList:
            full_path = "{}/{}".format(dirName, fname)
            file_list.append(full_path)
    return file_list

#######################################################################################################
# serialize any binary object to a file.
#######################################################################################################
def serialize_object(obj, filename):
    pickle_dump(obj, filename);

#######################################################################################################
# deserialize a file into a binary object.
#######################################################################################################
def load_object(filename):
    if check_file_existence(filename):
        return pickle_load(filename);
    else:
        print("cannot find file %s" % filename);

#######################################################################################################
# convert a date string with format "mm/dd/yy" to the nth day of the given year.
#######################################################################################################
def convert_datestring_to_day_num(datestring, base_y = 19):
    sec = datestring.split("/")
    y = int(sec[2])
    m = int(sec[0])
    d = int(sec[1])
    date = datetime.datetime(y, m, d);
    day_num = int(date.strftime("%j"));

    for year in range(base_y, y):
        day_num += (365 + (1 if calendar.isleap(year) else 0));

    return day_num;

#######################################################################
# operation system 
#######################################################################
def get_os_name():
    return platform.system();

def is_os_win():
    return get_os_name() == "Windows";


#######################################################################
# country name and code convertion
# ISO 3166
#######################################################################
def get_country_name_by_alpha2_code(country_alpha2_code):
    return pycountry.countries.get(alpha_2 = country_alpha2_code).name;

def get_country_name_by_alpha3_code(country_alpha3_code):
    return pycountry.countries.get(alpha_3 = country_alpha3_code).name;

def rectify_country_name_for_pyechart(country_name):
    name_table = {
        "Russian Federation":"Russia",
        "Bolivia, Plurinational State of":"Bolivia",
        "Venezuela, Bolivarian Republic of":"Venezuela",
        "Viet Nam":"Vietnam",
        "Lao People's Democratic Republic":"Lao PDR",
        "Iran, Islamic Republic of":"Iran",
        "Czechia":"Czech Rep", 
    }

    if country_name in name_table:
        return name_table[country_name];
    else:
        return country_name;


#######################################################################
# Convert a pandas series to categorical type
#######################################################################
def get_categorical_series(series, possible_category_list):
    return pd.Categorical(series, categories = possible_category_list, ordered = False)
