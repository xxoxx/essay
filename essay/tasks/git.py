# coding: utf-8
import logging
from fabric.state import env
from fabric.context_managers import lcd, cd
from fabric.operations import local, run

logger = logging.getLogger(__name__)


def command(cmd, in_local=False, git_path=None):
    cmd = cmd.encode('utf-8')
    print cmd, '###'

    if in_local:
        if git_path:
            with lcd(git_path):
                return local(cmd)
        else:
            return local(cmd)
    else:
        if git_path:
            with cd(git_path):
                return run(cmd)
        else:
            return run(cmd)

def clone(project_name, in_local=False, git_path=None):
    """
        把项目lone到本地
    """

    if env.GIT_SERVER.startswith('http'):
        cmd = 'git clone %s/%s' % (env.GIT_SERVER, project_name)
    else:
        cmd = 'git clone git@%s:%s' % (env.GIT_SERVER, project_name)
    command(cmd, in_local, git_path)


def reset(in_local=False, git_path=None):
    """
        把项目lone到本地
    """
    cmd = 'git reset --hard'
    command(cmd, in_local, git_path)


def push(branch=None, in_local=False, git_path=None):
    """
        把项目lone到本地
    """
    cmd = 'git push'
    if branch:
        cmd += ' origin ' + branch
    command(cmd, in_local, git_path)


def pull(in_local=False, git_path=None):
    """
        把项目lone到本地
    """
    cmd = 'git pull'

    command(cmd, in_local, git_path)


def add(files=None, add_all=False, in_local=False, git_path=None):
    if not files and not add_all:
        raise Exception(u'无效参数')

    if add_all:
        cmd = 'git add .'
    else:
        if not isinstance(files, (tuple, list)):
            files = [files]
        cmd = 'git add ' + ' '.join(files)
    command(cmd, in_local, git_path)


def commit(msg, in_local=False, git_path=None):
    """
        把项目lone到本地
    """
    cmd = u'git commit -a -m "%s"' % msg
    command(cmd, in_local, git_path)


def checkout(commit_or_branch, in_local=False, git_path=None):
    """
        根据commit回滚代码或者获取分支的所有代码

        commit据有优先权
    """

    cmd = 'git reset --hard && git checkout %s && git pull' % commit_or_branch
    command(cmd, in_local, git_path)


def get_version(in_local=False, git_path=None):
    cmd = "git rev-parse HEAD"
    return command(cmd, in_local, git_path)
