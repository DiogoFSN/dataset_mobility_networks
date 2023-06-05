import os

mydir = os.getcwd()
print('mydir: ', mydir)
files = os.listdir(mydir + '\\IBGE_2016_mobilidade\\main_code\\input_data\\networks')
if files.__len__() == 0:
    os.system('python \\IBGE_2016_mobilidade\\main_code\\input_data\\create_networks.py')
files.sort()

# mydir = os.chdir('src/metrics/')
# print(mydir)
# mydir = os.getcwd()
# print(mydir)

print('Computing metrics: ')
os.system('python src\\plot_network.py')
