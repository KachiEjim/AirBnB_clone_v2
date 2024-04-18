#!/usr/bin/python3
""" This script generates a .tgz archive from the web_static folder """
from fabric.api import local
from datetime import datetime

def do_pack():
    """ Generates a .tgz archive """

    # Create a timestamp for the filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "web_static_{}.tgz".format(timestamp)
    archive_path = path.join("versions", filename)

    print("Packing web_static to {}".format(archive_path))

    # Create the versions directory if it doesn't exist
    if not path.exists("versions"):
        makedirs("versions")

    # Compress the web_static directory into a .tgz archive
    local("tar -cvzf {} web_static".format(archive_path))

    print("Successfully packed web_static to {}".format(archive_path))

    return archive_path


