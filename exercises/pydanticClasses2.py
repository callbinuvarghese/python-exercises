"""

Parsing complex json structure with pydantic.

Using example json file from from nobelprize.org
### laureate.json from http://api.nobelprize.org/v1/laureate.json

Original data looked like this:

------------

{
"laureates" : [
       {
       "id":"1",
       "firstname":"Wilhelm Conrad",
       "surname":"R\u00f6ntgen",
       "born":"1845-03-27",
       "died":"1923-02-10",
       "bornCountry":"Prussia (now Germany)",
       "bornCountryCode":"DE",
       "bornCity":"Lennep (now Remscheid)",
       "diedCountry":"Germany",
       "diedCountryCode":"DE",
       "diedCity":"Munich",
       "gender":"male",
       "prizes":[
          {
             "year":"1901",
             "category":"physics",
             "share":"1",
             "motivation":"\"in recognition of the extraordinary services he has rendered by the discovery of the remarkable rays subsequently named after him\"",
             "affiliations":[
                {
                   "name":"Munich University",
                   "city":"Munich",
                   "country":"Germany"
                }
             ]
          }
       ]
    }
}
---------------------------

"""


import json

from enum import Enum
from typing import List
from devtools import pprint

from pydantic import BaseModel


class Category(str, Enum):
    physics = "physics"
    math = "math"
    economics = "economics"
    medicine = "medicine"
    peace = "peace"
    chemistry = "chemistry"
    literature = "literature"


class Prize(BaseModel):
    year: int
    category: Category
    share: int
    motivation: str
    affiliations: list


class Laureate(BaseModel):
    """fields with no values are required"""
    id: int
    firstname: str
    surname: str = ""
    born: str = None
    died: str = None
    bornCountry: str = None
    bornCountryCode: str = None
    bornCity: str = None
    diedCountry: str = None
    diedCountryCode: str = None
    diedCity: str = None
    gender: str = None
    prizes: List[Prize]


class Laureates(BaseModel):
    laureates: List[Laureate]

# Load data
with open("laureate.json") as f:
    datax = json.load(f)
    laureates_data = Laureates(**datax)

# Try filtering by filed values
filtered = filter(lambda l: "Wilhelm" in l.firstname, laureates_data.laureates)

print("\n".join(["%s %s" % (l.firstname, l.surname) for l in filtered]))

# Write data to file
with open('laureate_output.json', 'w') as f:
    pprint(laureates_data, f)


# Write json schema to file
with open('laureate_output_schema.json', 'w') as f:
    #f.write(laureates_data.schema_json(indent=2))
    f.write(json.dumps(laureates_data.model_json_schema()))