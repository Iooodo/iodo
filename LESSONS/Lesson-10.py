from os import *
from pathlib import *
from shutil import *
from datetime import *




# makedirs(name= "LESSONS/les-10")
# remove("LESSONS/les-10")

# p = Path(__file__).resolve().parent.parent.parent
# print(p)


# d = datetime.now()
# print(d)

#  d = datetime.utsnow()            # НЕ ИСПОЛЬЗОВАТЬ - ОН DEPRECATED
# # print(d)
#
# d = datetime.now(tz=UTC)
# print(d)
# print(d.timestamp())
# print(d.fromtimestamp(1717245807.845073, tz=UTC))
#
#
# print(__name__)
#
# from pydantic import BaseModel, EmailStr
# from pydantic_extra_types.
#
#
# class Valid(BaseModel):
#     email: EmailStr
#
# data = Valid(email="iodonadin@mail.ru")
# print(data)


# from os import *
# from pathlib import *
# from sys import *
# from traceback import *
# from shutil import *
# from datetime import *
#
# from orjson import loads
# from ujson import dump
#
# import app

# makedirs(name="templates/admin/components", exist_ok=True)
# removedirs(name="templates/admin/components")
# renames(old="templates/admin/base.html", new="templates/index.html")

# print([*walk(".")])


# p = Path(__file__).resolve()
# print(p)
# print(__file__)

# config_file_path = Path(__file__).resolve().parent / "config.yaml"
# BASE_DIR = Path(__file__).resolve().parent.parent

# from core import Config
#
#
# s = Config()


# try:
#     2 / 0
# except ZeroDivisionError:
#     print_exc()


# datetime
# d = datetime.now(tz=UTC)
# print(d.strftime("DAY: %d, %A, YEar: %y",))
# print(d.fromisoformat("2024-05-23T16:56:40.907877+01:30"))
# delta = timedelta()
# d2 = datetime(year=2025, month=5, day=23)
# print((d2 - d).total_seconds())
# print(d.timestamp())
# print(datetime.fromtimestamp(1716482991.598117, tz=UTC))
# print(d.replace(year=2025))
# date
# time
# timedelta

# from logging import info, warning, error, INFO, basicConfig, getLogger


# logger = getLogger(__name__)
#
#
# basicConfig(
#     format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
#     level=INFO,
#     datefmt="%d.%m.%y %H:%M",
#     filename="log.log",
#     filemode="a"
# )
# logger.info("kek")
# print(__name__)