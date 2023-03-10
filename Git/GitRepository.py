import os
import time

from git.repo import Repo
from git.repo.fun import is_git_dir

from Config.GitConfig import GIT_TOKEN, DEFAULT_GIT_PATH, DEFAULT_BRANCH


class GitRepository(object):
    """
    git仓库管理
    """

    def __init__(self, local_path, repo_url, branch=DEFAULT_BRANCH):
        self.local_path = local_path
        self.repo_url = repo_url
        self.repo = None
        self.initial(repo_url, branch)

    def initial(self, repo_url, branch):
        """
        初始化git仓库
        :param repo_url:
        :param branch:
        :return:
        """
        if not os.path.exists(self.local_path):
            os.makedirs(self.local_path)

        git_local_path = os.path.join(self.local_path, '.git')
        if not is_git_dir(git_local_path):
            self.repo = Repo.clone_from(repo_url, to_path=self.local_path, branch=branch)
        else:
            self.repo = Repo(self.local_path)

    def pull(self):
        """
        从线上拉最新代码
        :return:
        """
        self.repo.git.pull()

    def branches(self):
        """
        获取所有分支
        :return:
        """
        branches = self.repo.remote().refs
        return [item.remote_head for item in branches if item.remote_head not in ['HEAD', ]]

    def commits(self):
        """
        获取所有提交记录
        :return:
        """
        commit_log = self.repo.git.log('--pretty={"commit":"%h","author":"%an","summary":"%s","date":"%cd"}',
                                       max_count=50,
                                       date='format:%Y-%m-%d %H:%M')
        log_list = commit_log.split("\n")
        return [eval(item) for item in log_list]

    def tags(self):
        """
        获取所有tag
        :return:
        """
        return [tag.name for tag in self.repo.tags]

    def change_to_branch(self, branch):
        """
        切换分值
        :param branch:
        :return:
        """
        self.repo.git.checkout(branch)

    def change_to_commit(self, branch, commit):
        """
        切换commit
        :param branch:
        :param commit:
        :return:
        """
        self.change_to_branch(branch=branch)
        self.repo.git.reset('--hard', commit)

    def change_to_tag(self, tag):
        """
        切换tag
        :param tag:
        :return:
        """
        self.repo.git.checkout(tag)

    def push(self):
        self.repo.remote().push()

    def is_dirty(self):
        """
        表示是否存在文件变更
        :return:
        """
        return self.repo.is_dirty()

    def add(self):
        self.repo.git.add('.')

    def commit(self):
        self.repo.git.commit(m=time.strftime('%Y %b %d %H:%M:%S', time.localtime(time.time())))

    def sync(self):
        self.add()
        if self.is_dirty() or self.repo.index.entries is not None:
            self.commit()
            self.push()

if __name__ == '__main__':
    local_path = DEFAULT_GIT_PATH
    repo = GitRepository(local_path, 'https://'+GIT_TOKEN+'@github.com/liucxu/V2IConfig.git')
    branch_list = repo.branches()
    print(branch_list)
    # repo.change_to_branch('dev')
    repo.pull()
    repo.sync()
