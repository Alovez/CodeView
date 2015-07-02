from gittle import Gittle
 
repo_path = '/home/a/Programing/Cutie'
repo_url = 'http://git.oschina.net/alovez/Cutie'
repo = Gittle.clone(repo_url, repo_path)
print repo