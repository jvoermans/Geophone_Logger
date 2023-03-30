import glob
import os
import pickle
from BinaryParser import GPRMC_extractor

os.chdir(r'example_data')
myFiles = glob.glob('F*.pkl')
print(myFiles)


# - the data corresponding to each file:
#with open(str(path_to_folder_data.joinpath("F00000440.pkl")), "br") as fh:
for x in myFiles:
    with open(x, "br") as fh:
        dict_data_example = pickle.load(fh)
    vec0=dict_data_example["ADC"]["timestamps"]
    vec1=dict_data_example["ADC"]["channel_{}".format(0)]
    vec2=dict_data_example["ADC"]["channel_{}".format(1)]
    vec3=dict_data_example["ADC"]["channel_{}".format(2)]
    vec4=dict_data_example["ADC"]["channel_{}".format(3)]
    vec5=dict_data_example["ADC"]["channel_{}".format(4)]
    with open(x[0:9] + "_Data.txt", "w") as f:
        f.writelines(map("{},{},{},{},{},{}\n".format, vec0, vec1, vec2, vec3, vec4, vec5))
    parsed_gprmc = GPRMC_extractor(dict_data_example)
    with open(x[0:9] + "_GPS.txt", "w") as f:
        f.writelines(str(parsed_gprmc[0]))



