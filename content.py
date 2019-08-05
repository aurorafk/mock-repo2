# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo(r"C:\Users\Olufunmike.Oluore\source\repos\middleware")
# Your mock repo
mock_repo = git.Repo(r"C:\Users\Olufunmike.Oluore\source\repos\mock-repo2")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['olaorefunke2003@yahoo.com', 'Olufunmike.Olaore@wapic.com'])
importer.import_repository()
