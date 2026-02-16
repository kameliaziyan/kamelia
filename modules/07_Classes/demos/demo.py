from datetime import datetime
from uuid import uuid4


a = 1
a = "sdsdsd"
fl = 1.2
b = True # False
by = b"sfdfs"
n = None

my_string = "hello" + ' world' # helloworld
my_string = f"hello {fl}"

# No:
if n == None:
    print("None")
# Yes:
if n is None:
    print("None")


x_str = "1"
x_int = int(x_str)

y_float = 5.5
y_str = str(y_float)

list = [1, 2, 3]
list[0] = 55

if not n:
    print("n doesn't exist")
elif not list:
    print("n exists and list doesn't exist")
elif y_str == "5":
    print("n exists, list exists and y_str is 5")
else:
    print("n exists, list exists and y_str is not 5")

obj: int | None = 0

if not obj:
    print("None or False or 0 or [] or {} or ()")

# What python considers as a falsy value:
# None
# False
# 0
# []
# {}
# ()

if obj is None:
    print("obj is None!")

for i in range(4):
    print(i)

list1 = ["a", "b", "c"]
for index, item in enumerate(list1):
    print(f"({index}. {item}") 
    # (0). a
    # (1). b
    # ...

num = 1
while True:
    num += 1
    
    if num == 10:
        break
    
    if num % 7 == 0:
        continue

    print(num)

def calculate_tax(item_price: float) -> float:
    # .......
    return item_price * 1.18

def print_something() -> None:
    print("sdfdfdsd")

def validate(name: str, invalid_message:str = "INVALID!!!!", min_length: int = 3) -> None:
    if (len(name) > min_length):
        return None
    
    print(invalid_message)

validate(name="Shay")
validate("Shay")
validate("Shay", min_length=3)
validate(name="Shay", min_length=5)

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Function started")
        result = func(*args, **kwargs)
        print(f"[{datetime.now()}] Function ended")
        return result
    return wrapper

@logger
def do_something():
    print("Doing something...")

do_something()



def execute_func(func, times):
    for i in range(times):
        print(func(i))

execute_func(lambda x: x*x, 5)

def do_more(x): 
    print(f"Working on {x}")
    return x*x

execute_func(do_more, 5)

class User:
    save_to: str = "DB" # "File", "API"
    # name
    # UUID
    # create / update / login / logout / delete
    def __init__(self, name: str, uuid: str):
        self.name = name
        self.uuid = uuid
    
    def create(self):
        # Save to DB...
        if self.save_to == "DB":
            self.save_to_db(self.name, self.uuid)
        elif self.save_to == "File":
            # self.save_to_file...
            pass
        else:
            # save through API call
            pass

    def save_to_db(self, name, uuid):
        print(f"saved to db: name={name}, uuid={uuid}")
    
    @classmethod
    def build(cls, name: str):
        return cls(name, str(uuid4()))
    
    @classmethod
    def change_save_target(cls, new_save_to: str):
        cls.save_to = new_save_to    


user_with_build = User.build("Lala")
print(user_with_build.uuid)
print(user_with_build.save_to)

User.change_save_target("File")
user = User("Moshe", "123-456-789")
print(user.name)
user.create()
print(user.save_to)
print(user_with_build.save_to)


user1 = User("Avi", "333-444-555")

class FormatUtils:
    @staticmethod
    def formatDollar(num: int) -> str:
        return f"${num}"
    
FormatUtils.formatDollar(5)

class ToDoItem:
    def __init__(self, title: str, assignee: str, time_estimation_in_days: int) -> None:
        self._set_title(title)
        self.assignee = assignee
        self.time_estimation_in_days = time_estimation_in_days

    def _set_title(self, new_title: str) -> None:
        self.title = new_title

    def __str__(self) -> str:
        return f"{self.title} (assigned to {self.assignee})"
    
    def __repr__(self) -> str:
        return f"title={self.title}, assignee={self.assignee}"
    
    def __len__(self) -> int:
        return self.time_estimation_in_days


todo = ToDoItem("Wash the dishes", "Shay", 5)

todo_str = str(todo)
print(todo)
print(f"Todo: {todo}")
len(todo)

def dodo():
    """
    dodo method does ....
    gets input:
    returns ...
    """

# ---------------------------------------------
