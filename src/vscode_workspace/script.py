# -*- coding: utf-8 -*-
import json
import os


def main():
    # find path

    curr_path = os.path.realpath(os.path.curdir)
    src = "src"
    path = os.path.join(curr_path, src)
    try:
        list_of_package = os.listdir(path)
    except OSError:
        raise OSError("Could not find src folder")

    # get folder name

    workspace = os.path.basename(curr_path)

    # create dict

    dict_to_json = {"folders": [{"path": "."}], "settings": {}}

    for package in list_of_package:
        # check if folder is a python package
        if not os.path.isfile(os.path.join(path, package, "setup.py")):
            continue
        dict_to_json["folders"].append({"path": "src/" + package})

    # dump to json
    with open(workspace + ".code-workspace", "w") as out_files:
        json.dump(dict_to_json, out_files)

if __name__ == "__main__":
    main()
