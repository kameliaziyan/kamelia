
  
which python  


wps --
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