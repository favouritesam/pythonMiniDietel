from pathlib import Path
import csv

path = Path.cwd() / "consensus.csv"
path.touch()

census = [
    {"name": "Ned",
     "isSingle": False,
     "cohort": 15,
     "status": "COMPLICATED"
     },

    {"name": "Ridwan",
     "isSingle": True,
     "cohort": 15,
     "status": "SINGLE"
     },

    {"name": "Timmy",
     "isSingle": True,
     "cohort": 15,
     "status": "UNDISCLOSED"
     },
]

with open(path, encoding="utf-8", mode="r+") as file:
    writer = csv.DictWriter(file,
               fieldnames =["name", "isSingle", "cohort", "status"])
    writer.writeheader()
    writer.writerows(census)

# numbers = [
#     [29, 39, 49, 58, 34, 56],
#     [80, 34, 56, 32, 67, 89],
#     [43, 65, 76, 34, 78, 54]
# ]

# with open(path, encoding="utf-8", mode="r+") as file:
#     reader = csv.reader(file)
#     for this in reader:
#         print(this)
