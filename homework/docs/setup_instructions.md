source /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise4_budget_planner/hw4/venv/bin/activate
Kamelia ~/Desktop/kamelia_solutions source /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise4_budget_planner/hw4/venv/bin/activate
(venv) Kamelia ~/Desktop/kamelia_solutions cd homework/exercise2 
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2 pip install pytest 
Requirement already satisfied: pytest in /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise4_budget_planner/hw4/venv/lib/python3.14/site-packages (9.0.2)
Requirement already satisfied: iniconfig>=1.0.1 in /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise4_budget_planner/hw4/venv/lib/python3.14/site-packages (from pytest) (2.3.0)
Requirement already satisfied: packaging>=22 in /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise4_budget_planner/hw4/venv/lib/python3.14/site-packages (from pytest) (26.0)
Requirement already satisfied: pluggy<2,>=1.5 in /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise4_budget_planner/hw4/venv/lib/python3.14/site-packages (from pytest) (1.6.0)
Requirement already satisfied: pygments>=2.7.2 in /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise4_budget_planner/hw4/venv/lib/python3.14/site-packages (from pytest) (2.19.2)

[notice] A new release of pip is available: 25.3 -> 26.0.1
[notice] To update, run: pip install --upgrade pip
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2 cd hw2   
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2 pytst tests/test_exercise2.py
zsh: command not found: pytst
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2 pip install pytest
Requirement already satisfied: pytest in /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise4_budget_planner/hw4/venv/lib/python3.14/site-packages (9.0.2)
Requirement already satisfied: iniconfig>=1.0.1 in /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise4_budget_planner/hw4/venv/lib/python3.14/site-packages (from pytest) (2.3.0)
Requirement already satisfied: packaging>=22 in /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise4_budget_planner/hw4/venv/lib/python3.14/site-packages (from pytest) (26.0)
Requirement already satisfied: pluggy<2,>=1.5 in /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise4_budget_planner/hw4/venv/lib/python3.14/site-packages (from pytest) (1.6.0)
Requirement already satisfied: pygments>=2.7.2 in /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise4_budget_planner/hw4/venv/lib/python3.14/site-packages (from pytest) (2.19.2)

[notice] A new release of pip is available: 25.3 -> 26.0.1
[notice] To update, run: pip install --upgrade pip
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2 pytst tests/test_exercise2.py
zsh: command not found: pytst
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2 pytest tests/test_exercise2.py
=================================================================== test session starts ===================================================================
platform darwin -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise2/hw2
collected 5 items                                                                                                                                         

tests/test_exercise2.py ....F                                                                                                                       [100%]

======================================================================== FAILURES =========================================================================
_____________________________________________________________________ test_calculator _____________________________________________________________________

    def test_calculator():
        user_inputs = [
            "add 2 to 5",
            "subtract 2 from 5"
      ,"multiply 2 by 5"
      , "divide 10 by 5"
       , "exit"
        ]
    
        expected_outputs = [
            "The answer is 7",
            "The answer is 3",
            "The answer is 10",
            "The answer is 2.0"
    
        ]
>       with patch("builtins.input", side_effect= user_inputs):
             ^^^^^
E       NameError: name 'patch' is not defined

tests/test_exercise2.py:47: NameError
================================================================= short test summary info =================================================================
FAILED tests/test_exercise2.py::test_calculator - NameError: name 'patch' is not defined
=============================================================== 1 failed, 4 passed in 0.04s ===============================================================
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2 pytest tests/test_exercise2.py
=================================================================== test session starts ===================================================================
platform darwin -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise2/hw2
collected 5 items                                                                                                                                         

tests/test_exercise2.py ....F                                                                                                                       [100%]

======================================================================== FAILURES =========================================================================
_____________________________________________________________________ test_calculator _____________________________________________________________________

    def test_calculator():
        user_inputs = [
            "add 2 to 5",
            "subtract 2 from 5"
      ,"multiply 2 by 5"
      , "divide 10 by 5"
       , "exit"
        ]
    
        expected_outputs = [
            "The answer is 7",
            "The answer is 3",
            "The answer is 10",
            "The answer is 2.0"
    
        ]
        with patch("builtins.input", side_effect= user_inputs):
>           with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
                                                  ^^
E           NameError: name 'io' is not defined. Did you forget to import 'io'?

tests/test_exercise2.py:49: NameError
================================================================= short test summary info =================================================================
FAILED tests/test_exercise2.py::test_calculator - NameError: name 'io' is not defined. Did you forget to import 'io'?
=============================================================== 1 failed, 4 passed in 0.05s ===============================================================
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2 pytest tests/test_exercise2.py
=================================================================== test session starts ===================================================================
platform darwin -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise2/hw2
collected 5 items                                                                                                                                         

tests/test_exercise2.py .....                                                                                                                       [100%]

==================================================================== 5 passed in 0.01s ====================================================================
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2 cd tests 
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2/tests black .
reformatted /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise2/hw2/tests/test_exercise2.py

All done! ✨ 🍰 ✨
1 file reformatted, 3 files left unchanged.
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2/tests flake8 .
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2/tests mypy .
test_exercise2.py:7: error: Function is missing a return type annotation  [no-untyped-def]
test_exercise2.py:7: note: Use "-> None" if function does not return a value
test_exercise2.py:13: error: Function is missing a return type annotation  [no-untyped-def]
test_exercise2.py:13: note: Use "-> None" if function does not return a value
test_exercise2.py:19: error: Function is missing a return type annotation  [no-untyped-def]
test_exercise2.py:19: note: Use "-> None" if function does not return a value
test_exercise2.py:25: error: Function is missing a return type annotation  [no-untyped-def]
test_exercise2.py:25: note: Use "-> None" if function does not return a value
test_exercise2.py:32: error: Function is missing a return type annotation  [no-untyped-def]
test_exercise2.py:32: note: Use "-> None" if function does not return a value
Found 5 errors in 1 file (checked 4 source files)
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2/tests mypy .
test_exercise2.py:32: error: Function is missing a return type annotation  [no-untyped-def]
test_exercise2.py:32: note: Use "-> None" if function does not return a value
Found 1 error in 1 file (checked 4 source files)
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2/tests mypy .
Success: no issues found in 4 source files
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2/tests cd ..
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2 cd ..
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2 cd .. 
(venv) Kamelia ~/Desktop/kamelia_solutions/homework cd exercise3 
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3 cd hw3 
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3 pytest tests/test_exercise2.py
=================================================================== test session starts ===================================================================
platform darwin -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise3/hw3
collected 4 items                                                                                                                                         

tests/test_exercise2.py ....                                                                                                                        [100%]

==================================================================== 4 passed in 0.01s ====================================================================
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3 cd tests 
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3/tests black .
reformatted /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise3/hw3/tests/test_exercise1.py
reformatted /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise3/hw3/tests/test_exercise2.py

All done! ✨ 🍰 ✨
2 files reformatted, 1 file left unchanged.
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3/tests flake8 .
./test_exercise2.py:24:1: F811 redefinition of unused 'test_febonacci4' from line 19
./test_exercise2.py:28:9: W503 line break before binary operator
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3/tests cd ..
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3 pytest tests/test_exercise2.py
=================================================================== test session starts ===================================================================
platform darwin -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise3/hw3
collected 5 items                                                                                                                                         

tests/test_exercise2.py .....                                                                                                                       [100%]

==================================================================== 5 passed in 0.01s ====================================================================
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3 cd tests 
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3/tests black .
All done! ✨ 🍰 ✨
3 files left unchanged.
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3/tests flake8 .
./test_exercise2.py:28:9: W503 line break before binary operator
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3/tests black .
reformatted /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise3/hw3/tests/test_exercise2.py

All done! ✨ 🍰 ✨
1 file reformatted, 2 files left unchanged.
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3/tests flake8 .
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3/tests mypy .
test_exercise1.py:5: error: Function is missing a return type annotation  [no-untyped-def]
test_exercise1.py:5: note: Use "-> None" if function does not return a value
test_exercise1.py:10: error: Function is missing a return type annotation  [no-untyped-def]
test_exercise1.py:10: note: Use "-> None" if function does not return a value
test_exercise1.py:15: error: Function is missing a return type annotation  [no-untyped-def]
test_exercise1.py:15: note: Use "-> None" if function does not return a value
Found 3 errors in 1 file (checked 3 source files)
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3/tests mypy .
Success: no issues found in 3 source files
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3/tests black . 
reformatted /Users/kameliaziyan/Desktop/kamelia_solutions/homework/exercise3/hw3/tests/test_exercise1.py

All done! ✨ 🍰 ✨
1 file reformatted, 2 files left unchanged.
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3/tests flake8 .
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3/tests mypy .  
Success: no issues found in 3 source files
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3/tests cd ..
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3/hw3 cd ..
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise3 cd ..
(venv) Kamelia ~/Desktop/kamelia_solutions/homework cd exercise2 
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2 cd hw2 
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2 deactivate
Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2 source venv/bin/activate
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2 pip freeze
black==26.1.0
click==8.3.1
flake8==7.3.0
iniconfig==2.3.0
librt==0.7.8
mccabe==0.7.0
mypy==1.19.1
mypy_extensions==1.1.0
numpy==2.4.2
packaging==26.0
pandas==3.0.0
pathspec==1.0.4
platformdirs==4.5.1
pluggy==1.6.0
pycodestyle==2.14.0
pyflakes==3.4.0
Pygments==2.19.2
pytest==9.0.2
python-dateutil==2.9.0.post0
pytokens==0.4.1
six==1.17.0
typing_extensions==4.15.0
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2 pip install -r requirements.txt 
Requirement already satisfied: black in ./venv/lib/python3.14/site-packages (from -r requirements.txt (line 1)) (26.1.0)
Requirement already satisfied: flake8 in ./venv/lib/python3.14/site-packages (from -r requirements.txt (line 2)) (7.3.0)
Collecting wemake-python-styleguide (from -r requirements.txt (line 3))
  Downloading wemake_python_styleguide-1.5.0-py3-none-any.whl.metadata (9.5 kB)
Requirement already satisfied: mypy in ./venv/lib/python3.14/site-packages (from -r requirements.txt (line 4)) (1.19.1)
Requirement already satisfied: pytest in ./venv/lib/python3.14/site-packages (from -r requirements.txt (line 5)) (9.0.2)
Requirement already satisfied: click>=8.0.0 in ./venv/lib/python3.14/site-packages (from black->-r requirements.txt (line 1)) (8.3.1)
Requirement already satisfied: mypy-extensions>=0.4.3 in ./venv/lib/python3.14/site-packages (from black->-r requirements.txt (line 1)) (1.1.0)
Requirement already satisfied: packaging>=22.0 in ./venv/lib/python3.14/site-packages (from black->-r requirements.txt (line 1)) (26.0)
Requirement already satisfied: pathspec>=1.0.0 in ./venv/lib/python3.14/site-packages (from black->-r requirements.txt (line 1)) (1.0.4)
Requirement already satisfied: platformdirs>=2 in ./venv/lib/python3.14/site-packages (from black->-r requirements.txt (line 1)) (4.5.1)
Requirement already satisfied: pytokens>=0.3.0 in ./venv/lib/python3.14/site-packages (from black->-r requirements.txt (line 1)) (0.4.1)
Requirement already satisfied: mccabe<0.8.0,>=0.7.0 in ./venv/lib/python3.14/site-packages (from flake8->-r requirements.txt (line 2)) (0.7.0)
Requirement already satisfied: pycodestyle<2.15.0,>=2.14.0 in ./venv/lib/python3.14/site-packages (from flake8->-r requirements.txt (line 2)) (2.14.0)
Requirement already satisfied: pyflakes<3.5.0,>=3.4.0 in ./venv/lib/python3.14/site-packages (from flake8->-r requirements.txt (line 2)) (3.4.0)
Collecting attrs (from wemake-python-styleguide->-r requirements.txt (line 3))
  Downloading attrs-25.4.0-py3-none-any.whl.metadata (10 kB)
Requirement already satisfied: pygments<3.0,>=2.19 in ./venv/lib/python3.14/site-packages (from wemake-python-styleguide->-r requirements.txt (line 3)) (2.19.2)
Requirement already satisfied: typing_extensions>=4.6.0 in ./venv/lib/python3.14/site-packages (from mypy->-r requirements.txt (line 4)) (4.15.0)
Requirement already satisfied: librt>=0.6.2 in ./venv/lib/python3.14/site-packages (from mypy->-r requirements.txt (line 4)) (0.7.8)
Requirement already satisfied: iniconfig>=1.0.1 in ./venv/lib/python3.14/site-packages (from pytest->-r requirements.txt (line 5)) (2.3.0)
Requirement already satisfied: pluggy<2,>=1.5 in ./venv/lib/python3.14/site-packages (from pytest->-r requirements.txt (line 5)) (1.6.0)
Downloading wemake_python_styleguide-1.5.0-py3-none-any.whl (219 kB)
Downloading attrs-25.4.0-py3-none-any.whl (67 kB)
Installing collected packages: attrs, wemake-python-styleguide
Successfully installed attrs-25.4.0 wemake-python-styleguide-1.5.0

[notice] A new release of pip is available: 25.3 -> 26.0.1
[notice] To update, run: pip install --upgrade pip
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2 ./lint.sh
zsh: permission denied: ./lint.sh
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2 /lint.sh 
zsh: no such file or directory: /lint.sh
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2 chmod +x lint.sh
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2 ./lint.sh       
Running flake8 with "wemake-python-styleguide (WPS)" plugin
./solution/exercise1.py:8:9: WPS111 Found too short name: i < 2
./solution/exercise1.py:8:14: WPS518 Found implicit `enumerate()` call
./solution/exercise2.py:10:9: WPS111 Found too short name: a < 2
./solution/exercise2.py:11:9: WPS111 Found too short name: b < 2
./solution/exercise2.py:16:16: WPS226 Found string literal over-use: invalid operation > 3
./solution/exercise2.py:22:9: WPS111 Found too short name: a < 2
./solution/exercise2.py:23:9: WPS111 Found too short name: b < 2
./solution/exercise2.py:34:9: WPS111 Found too short name: a < 2
./solution/exercise2.py:35:9: WPS111 Found too short name: b < 2
./solution/exercise2.py:46:9: WPS111 Found too short name: a < 2
./solution/exercise2.py:47:9: WPS111 Found too short name: b < 2
./solution/exercise2.py:58:1: WPS231 Found function with too much cognitive complexity: 48 > 16
./solution/exercise2.py:60:5: WPS327 Found useless `continue` at the end of the loop
./solution/exercise2.py:63:13: WPS204 Found overused expression: print('invalid operation'); used 5 > 4
./solution/exercise2.py:72:16: WPS204 Found overused expression: words[0]; used 5 > 4
./solution/exercise2.py:89:9: WPS229 Found too long ``try`` body length: 2 > 1
./solution/exercise3.py:34:1: WPS212 Found too many return statements: 9 > 5
./tests/test_exercise1.py:21:1: WPS118 Found too long name: test_analyze_log_content_with_no_valid_entries > 45
Running mypy
Success: no issues found in 8 source files
(venv) Kamelia ~/Desktop/kamelia_solutions/homework/exercise2/hw2  




wps --
cd hw2  
 deactivate  
 source venv/bin/activate   
 pip freeze   
 pip install -r requirements.txt
./lint.sh   
chmod +x lint.sh
./lint.sh     
which python  


cd ..
cd ..
cd ..
cd exercise2
cd hw2
deactivate
source venv/bin/activate
pip freeze
pip install -r requirements.txt
./lint.sh
chmod +x lint.sh
./lint.sh


main command => python3 -m solution.main



fast api download 
python -m venv .venv

 source .venv/bin/activate  |  .venv\Scripts\Activate.ps1

 pip install "fastapi[standard]"


api run----------
fastapi dev ./file.py


how to enter data in the url 
http://127.0.0.1:8000/products?name=Phone&description=Nice&price=100&stock=5