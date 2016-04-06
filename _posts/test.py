from git import Repo
import os
from git import RemoteProgress

class MyProgressPrinter(RemoteProgress):
	def update(self, op_code, cur_count, max_count=None, message=''):
		print(op_code, cur_count, max_count, cur_count / (max_count or 100.0), message or "NO MESSAGE")
# end

def PullData():
	return

path ="C:\\kerwenzhang.github.io"
assert(os.path.isdir(path))
repo = Repo(path)
assert not repo.bare
assert len(repo.remotes) == 1 

print(len(repo.remotes))
origins = repo.remotes
origin = origins.pop()
assert origin.exists()
print(origin.exists())
origin.fetch()
origin.pull()


'''	
if repo.is_dirty():
	print("Begin to pull data from remote server.")
	PullData()
'''

fileList = repo.untracked_files
print("Following file is not upload yet")
print(repo.untracked_files)



print("Begin to push data to server")

repo.index.add(fileList)   
repo.index.commit("Add a new file")
origin.push()