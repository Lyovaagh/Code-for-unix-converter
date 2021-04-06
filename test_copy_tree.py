# importing shutil module

from copytree import copytree
from copy3 import Filter

# path = 'G:/'
# source_path = path + 'shab33'
# destination_path = path + 'G:/shab34'

path = 'C:/temp/git_projects/'
source_path = path + 'bbb'
destination_path = path + 'aaa'

from time_util import log
log("Start Program")

# Copy the content of source to destination
copytree(source_path, destination_path)
list = Filter.exts
print(list)
