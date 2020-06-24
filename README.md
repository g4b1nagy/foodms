# foodms

Food management system

* git clone git@github.com:g4b1nagy/foodms.git
* cd foodms/
* virtualenv -p python3 venv
* source venv/bin/activate
* pip install -r requirements.txt
* ./manage.py migrate
* ./manage.py loaddata measure.json
* ./manage.py loaddata nutrient.json
* ./manage.py loaddata food.json
* ./manage.py createsuperuser
* ./manage.py runserver
* http://localhost:8000/
* http://localhost:8000/admin/foods/food/1/change/
