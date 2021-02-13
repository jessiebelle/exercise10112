import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
    print('HOMEPATH')
else:
    hdir = os.environ['HOME']
    print('HOME')

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')
print(pattern)

# for file_name in glob.glob('/Users/rafikaturemis/*'):
#     print(file_name)
#
# for our_file_name in glob.glob('/Users/rafikaturemis/JessnRaf_Wk3/*'):
#     print(our_file_name)

for our_repo in glob.glob('/Users/rafikaturemis/JessnRaf_Wk3/exercise10112/*'):
    file_sizes = os.path.getsize(our_repo)
    print(file_sizes)
    if len(our_repo) == 0:
        pass
    else:
        print(len(our_repo))
    our_repo = os.path.basename(our_repo)
    print(our_repo)

# Below we were attempting to familiarize ourselves with the functionality of glob.glob() and .getsize()
# our_repo = glob.glob('/Users/rafikaturemis/JessnRaf_Wk3/exercise10112/*')
# print(our_repo)
#
# file_sizes = os.path.getsize("/Users/rafikaturemis/JessnRaf_Wk3/exercise10112/")
# print(file_sizes)




# TODO: Use the glob.glob() function to obtain the list of filenames

# TODO: use os.path.getsize to find each file's size

# TODO: Add a test to only display files that are not zero length

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()

