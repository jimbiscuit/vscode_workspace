# -*- coding: utf-8 -*-
import json
import os


IGNORE_FOLDER = ["parts", "build", "node_modules", "omelette", "var", "bin", "blobstorage", ]


def recursive_folder(path, list_of_package=[]):
    for folder in os.listdir(path):

        if folder in IGNORE_FOLDER:
            continue
        if not os.path.isdir(os.path.join(path, folder)):
            continue

        if os.path.isdir(os.path.join(path, folder, ".git")):
            list_of_package.append(os.path.join(path, folder))

        recursive_folder(os.path.join(path, folder), list_of_package)

    return list_of_package


def main():
    # find path

    curr_path = os.path.realpath(os.path.curdir)
    path = os.path.join(curr_path)

    # get folder name

    workspace = os.path.basename(curr_path)

    # create dict

    dict_to_json = {
        "folders": [{"path": package} for package in recursive_folder(path)],
        "settings": {}
    }

    dict_to_json["folders"].append({"path": "."})

    # dump to json
    with open(workspace + ".code-workspace", "w") as out_files:
        json.dump(dict_to_json, out_files)

if __name__ == "__main__":
    main()
