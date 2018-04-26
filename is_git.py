# -*- coding: utf-8 -*-
import os

import os.path

git_set=set()

def is_git(path='./',checkgit='.git'):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,checkgit)):
            git_set.add(path)
            git_set.add(path)
        if not os.path.isdir(os.path.join(path,file)):
            continue
        elif file == checkgit:
            git_set.add(path)
            git_set.add(path)
        else:
            is_git(os.path.join(path,file))


is_git('.\\')

print '----------------------'
for d in git_set:
    print d

