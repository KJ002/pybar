import yaml
import psutil
from pathlib import Path
from typing import List
from datetime import datetime
import pytz


def cpu(args: List) -> str:
    return f"{psutil.cpu_percent(*args)}%"


def mem(args: List) -> str:
    return f"{psutil.virtual_memory(*args)[2]}%"


def dtime(args: List) -> str:
    return f"{datetime.now(pytz.timezone(args[0])).strftime(args[1])}"


module_table = {
    "cpu": cpu,
    "mem": mem,
    "datetime": dtime
}


def main():
    with open(str(Path.home()) + "/.config/pybar/config.yml") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    active_modules = [
        i for i in config["modules"]
        if list(i.values())[0] == "active"
    ]

    result = [None for i in active_modules]

    for i in active_modules:
        result.insert(
            i["position"],
            i.get("prefix", "")+module_table[list(i.keys())[0]](i.get("args", []))
        )

    print(
        config["bar"][0]["seperator"].join(
            [
                i for i in result
                if i is not None
            ]
        )
    )


if __name__ == "__main__":
    main()
