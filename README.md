### CO2 dashboard
this repo consist of global co2 visualization dashboard made using django .

## setup
 setup venv
 python -m venv ./venv
  ./venv/Scripts/activate

install all the required modules 
  pip install -r requirements.txt

run the server
  python manage.py runserver
 

## File structure for the project
./
├── dashboard_dash/
│   ├── dashboard_dash/
│   │   ├── __pycache__
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── routing.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── Data/
│   │   ├── co2_emission_by_continents.csv
│   │   └── co2_emission_by_country.csv
│   ├── home/
│   │   ├── __pycache__
│   │   ├── dash_app_country/
│   │   │   ├── __pycache__
│   │   │   ├── Area_chart.py
│   │   │   ├── Bub_chart.py
│   │   │   ├── Data_table.py
│   │   │   ├── Line_chart.py
│   │   │   ├── Pie_chart.py
│   │   │   └── Scat_plot.py
│   │   ├── dash_apps_conte/
│   │   │   ├── __pycache__
│   │   │   ├── Area_c.py
│   │   │   ├── B_chart.py
│   │   │   ├── D_table.py
│   │   │   ├── Dash_Board.py
│   │   │   ├── L_chart.py
│   │   │   └── P_chart.py
│   │   ├── management
│   │   ├── migrations
│   │   ├── templates/home/
│   │   │   ├── country.html
│   │   │   ├── dashboard.html
│   │   │   ├── forgot-password.html
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   └── welcome.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── static
│   ├── templates/
│   │   ├── partials
│   │   └── base.html
│   ├── db.sqlite3
│   ├── manage.py
│   └── README.md
├── requirements.txt
└── venv
