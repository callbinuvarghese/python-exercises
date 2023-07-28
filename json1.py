
import json

def testJson1():

    data = {
        "president": {
            "name": "Zaphod Beeblebrox",
            "species": "Betelgeusian"
        }
    }
    json_string = json.dumps(data,indent=4)
    print(json_string)
    with open("test1.json","w") as f:
        json.dump(data,f)

    with open("test1.json","r") as f:
        data1 = json.load(f)
        print(data1)

def testJson2():
    json_string = """
    {
        "researcher": {
            "name": "Ford Prefect",
            "species": "Betelgeusian",
            "relatives": [
                {
                    "name": "Zaphod Beeblebrox",
                    "species": "Betelgeusian"
                }
            ]
        }
    }
    """
    data = json.loads(json_string)
    print(data)

# Define a function to filter out completed TODOs 
# of users with max completed TODOS.
def keep(todo, users):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

def testJson3():
    import requests
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    json1=json.loads(response.text)
    #print(json.dumps(json1, indent=2))
    
    todos = response.json()
    print(type(todos))
    #print(todos)

    todos_by_user = {}
    for todo in todos:
        if todo["completed"]:
            try:
                # Increment the existing user's count.
                todos_by_user[todo["userId"]] += 1
            except KeyError:
                # This user has not been seen. Set their count to 1.
                todos_by_user[todo["userId"]] = 1
    print(todos_by_user)

   
    # Create a sorted list of (userId, num_complete) pairs.
    top_users = sorted(todos_by_user.items(), 
                   key=lambda x: x[1], reverse=True)
    print(top_users)
    # Get the maximum number of complete TODOs.
    max_complete = top_users[0][1]
    print(max_complete)
    print(type(max_complete))

    myList = ["1", "2", "3", "4", "5"]
    output_list = []
    for element in myList:
        value = int(element)
        output_list.append(value)
    print("The input list is:", myList)
    print("The output list is:", output_list)

    max_complete_users = []
    for user, num_complete in top_users:
        if num_complete < max_complete :
            break
        else:
            max_complete_users.append(str(user)) # depening on the next statement it does not allow int to be appended; need to convert to string
    max_users = " and ".join(max_complete_users)
    print(max_users)

    users = {x["userId"] for x in todos}
    print(users)

if __name__ == "__main__":
    testJson1()
    testJson2()
    testJson3()