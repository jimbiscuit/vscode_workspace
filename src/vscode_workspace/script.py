import json
import os


def main():
    # find path

    curr_path = os.path.realpath(os.path.curdir)
    src = "src"
    path = os.path.join(curr_path, src)
    list_of_package = os.listdir(path)

    # get folder name

    workspace = os.path.basename(curr_path)

    # create dict

    dict_to_json = {"folders": [{"path": "."}], "settings": {}}

    for package in list_of_package:
        dict_to_json["folders"].append({"path": "src/" + package})

    # dump to json
    with open(workspace + ".code-workspace", "w") as out_files:
        json.dump(dict_to_json, out_files)

if __name__ == "__main__":
    main()
