 # Command-line interface (UI layer)
#import budget

class CLI():
    def __init__(self):
        pass

    def actions(self):
        
        while True:

          data = input("===== BUDGET PLANNER =====\n"
          "1. Add Income\n"
          "2. Add Expense\n"
          "3. View Summary\n"
          "4. Exit\n\n"
          "Choose an option:"

          ).strip()

          ##add actions ########

          if data == "4" :
              break
          print(data)

