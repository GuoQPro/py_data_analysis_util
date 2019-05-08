
import math;
from sklearn.externals import joblib;
import os;

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