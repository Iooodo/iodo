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
# print(d)

# d = datetime.now(tz=UTC)
# print(d)
# print(d.timestamp())
# print(d.fromtimestamp(1717245807.845073, tz=UTC))


# print(__name__)

# from pydantic import BaseModel, EmailStr
# from pydantic_extra_types.
#
#
# class Valid(BaseModel):
#     email: EmailStr
#
# data = Valid(email="iodonadin@mail.ru")
# print(data)