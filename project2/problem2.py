import os

def find_files(suffix, path):
    if os.path.isfile(path):
        if path.split('.')[-1] == suffix:
            return [path]
        return []
    res = []
    for dir in os.listdir(path):
        path_new = path
        path_new = os.path.join(path, dir)
        res += find_files(suffix, path_new)
        
    return res  

### test cases

path = "./testdir"
suffix_1 = 'c'
print("Case 1: suffix is 'c'________________________________________________________________\n")

res_1 = ["'./testdir/subdir1/a.c'", \
 "'./testdir/subdir3/subsubdir1/b.c'", \
 "'./testdir/subdir5/a.c'", \
 "'./testdir/t1.c'"]
print("Expected result is :\n{},\n{},\n{},\n{}\n".format(*res_1))

print("output is:\n{}\n{}\n{}\n{}\n".format(*find_files(suffix_1,path)))


suffix_2 = 'h'
print("Case 2: suffix is 'h'________________________________________________________________\n")

res_1 = ["'./testdir/subdir1/a.h'", \
 "'./testdir/subdir3/subsubdir1/b.h'", \
 "'./testdir/subdir5/a.h'", \
 "'./testdir/t1.h'"]
print("Expected result is :\n{},\n{},\n{},\n{}\n".format(*res_1))

print("output is:\n{}\n{}\n{}\n{}\n".format(*find_files(suffix_2,path)))

suffix_2 = 'py'
print("Case 3: suffix is 'h'________________________________________________________________\n")

res_1 = []
print("Expected result is :None\n")

print("output is:{}".format(find_files(suffix_2,path)))