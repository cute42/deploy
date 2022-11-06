# file-uuid=     '627398e0-5d4b-11ed-8755-d0817aaf398c' # (fuuid.py)
# project-uuid=  'c7856c22-5d4b-11ed-989b-d0817aaf398c' # (core)
# family-uuid=   'b47de9ba-5d4b-11ed-8e57-d0817aaf398c' # (cute)


from uuid import uuid1 as new_uuid
from pyperclip import copy 
from pathlib import Path 
from tomli import loads, TOMLDecodeError #!md| [code](https://github.com/hukkin/tomli)
# from tomli_w import dump #!md| [code](https://github.com/hukkin/tomli-w)
from tomlkit import dump, parse #!md| [docs](https://github.com/sdispater/tomlkit/blob/master/docs/quickstart.rst) [openbase](https://openbase.com/python/tomlkit/documentation)
from tomlkit import document, table, comment, nl 

from sys import argv
from rich import print 
from datetime import datetime, UTC

script_file = Path(argv[0])
parent_path = script_file.parents[0]
toml_file_path =  parent_path / 'uuid_store.toml'

print(f'{toml_file_path} exits {Path(toml_file_path).exists()}')
content_string = Path(toml_file_path).read_text() #encoding='utf-8')

try:
    data = loads(content_string)
except TOMLDecodeError:
    print("Yep, definitely not valid.")

doc = parse(content_string)
doc.add( nl() )
doc.add( nl() )
doc.add( nl() )
doc.add( comment('!md| # Table'))

database = table()
database.comment("- create an example")
database["server"] = "192.168.1.1"
database["ports"] = [8001, 8001, 8002]
database["connection_max"] = 5000
database["enabled"] = True
database["entry"] = datetime(1979, 5, 27, 7, 32, tzinfo=UTC)
doc["database"] = database


print('data')
print(data['files']['py']['fuuid'])

def new_uuid_str( ):
    return str(new_uuid())

copy( new_uuid_str() )


with open(str(parent_path / 'tests_uuid.toml'), "w") as file_handle:
    dump(doc, file_handle)


