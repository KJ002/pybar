import yaml
import psutil
from pathlib import Path
from typing import List
from datetime import datetime
import pytz
from dataclasses import dataclass, field


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


@dataclass
class Module:
    type: str
    enabled: bool
    position: int
    prefix: str = ""
    args: List = field(default_factory=list)


    def __lt__(self, other):
        return self.position < other.position


    def __call__(self):
        return module_table[self.type](self.args)


def main():
    with open(str(Path.home()) + "/.config/pybar/config.yml") as file:
        config = yaml.load(
            file,
            Loader=yaml.FullLoader
        )

    seperator = config["bar"][0].get("seperator", "")

    active_modules = [
        Module(**i) for i in config["modules"] if i["enabled"]
    ]

    result = [i() for i in sorted(active_modules)]

    print(seperator.join(result))

if __name__ == "__main__":
    main()
