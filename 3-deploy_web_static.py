#!/usr/bin/python3
# Fabric script (based on the file 1-pack_web_static.py) that distributes
# an archive to your web servers, using the function do_deploy

from os.path import exists, isdir
from fabric.api import put, sudo, env, local
from datetime import datetime
env.hosts = ["35.231.170.166", "54.83.91.228"]


def do_pack():
    now = datetime.utcnow()
    vfl = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                        now.month,
                                                        now.day,
                                                        now.hour,
                                                        now.minute,
                                                        now.second)

    if not isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    if local('tar -cvzf {} web_static'.format(vfl)).failed:
        return None
    return vfl


def do_deploy(archive_path):
    """function do_deploy"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        sudo('mkdir -p {}{}/'.format(path, no_ext))
        sudo('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        sudo('rm /tmp/{}'.format(file_n))
        sudo('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        sudo('rm -rf {}{}/web_static'.format(path, no_ext))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False


def deploy():
    """that creates and distributes an archive to your web servers,
       using the function deploy
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
