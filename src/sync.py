from git import Repo

def check_updates(repo_path):
    repo = Repo(repo_path)
    origin = repo.remotes.origin
    origin.fetch()
    return repo.head.commit != origin.refs.main.commit

def pull_updates(repo_path):
    repo = Repo(repo_path)
    repo.remotes.origin.pull()
