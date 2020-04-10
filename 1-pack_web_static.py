#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of the web_static 
# folder of your AirBnB Clone repo, using the function do_pack

from os import path
from fabric.api import local
from datetime import datetime


def do_pack():
    now = datetime.utcnow()
    vfl = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                        now.month,
                                                        now.day,
                                                        now.hour,
                                                        now.minute,
                                                        now.second)

    if not path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    if local('tar -cvzf {} web_static'.format(vfl)).failed:
        return None
    return vfl
