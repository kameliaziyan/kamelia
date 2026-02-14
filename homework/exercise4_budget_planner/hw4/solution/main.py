 # Entry point for the application


#from solution.budget import Budget
from solution.cli import CLI 

def main() -> None :
    #budget = Budget()
    app = CLI()
    app.actions()

if __name__ == "__main__":
    main()
