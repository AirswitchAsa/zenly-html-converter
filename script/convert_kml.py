import sys
from functions import read_from_path, convert_file_to_dict, save_day_kml, save_all_kml


args = sys.argv[1:]
output_all = False

if '--all' in args:
    output_all = True
    args.remove('--all')
    
if len(args) != 1:
    print('Please provide only your data folder and --all flag')
    sys.exit(0)

data_path = args[0]
file_paths, file_names = read_from_path(data_path)

if output_all:
    save_all_kml(file_paths, file_names)
else:
    for file_path, file_name in zip(file_paths, file_names):
        date = file_name.split('.')[0]
        day = convert_file_to_dict(file_path, date)
        save_day_kml(day, date)
