import random

user_details = {
    "first_name": "favour",
    "last_name": "Nwadike",
    "age": 20,
    "states": "imo",
    "skills": {
        "soft": ["Communication", "Verbal", "Violence"],
        "technical": ["python", "Java", "JavaScript", "Csharp"]
    },
    "height": 5.
}
# print(user_details["skills"]["technical"][3])
val = user_details["skills"]["soft"][1]
# val = user_details["skills "]["soft"][1] = [1, False, "Verbal", "Hello"]
# Remove key value pair with key
# result = user_details.pop("height")
# result = user_details.get("first_name")
# print(result)
# Generate key view pair
# result = user_details.items()
# result = user_details["first_name "] = "Richard"
# if i dont want to use this
# result = user_details.update({"first_name,": "Richard"})
# user_details["hobbies"] = "Swimming"
# print(result)
# del user_details
# print(user_details)


print("Welcome to Elite Quiz Games !!!\n")
user_question = str(input('Enter yes if you wish to play the quiz name:)')).lower
question_dict = {"what is 1+1?": "2",
                 "What is 2*2?": "4",
                 }
while True:
    keys = random.sample(list(question_dict.keys)), 0, 30

