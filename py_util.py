
import math;
from sklearn.externals import joblib;
import os;
import datetime, calendar;
import platform;

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
    joblib.dump(obj, filename);

#######################################################################################################
# deserialize a file into a binary object.
#######################################################################################################
def load_object(filename):
    if check_file_existence(filename):
        return joblib.load(filename);
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

def is_os_win():
    return platform.system() == "Windows";