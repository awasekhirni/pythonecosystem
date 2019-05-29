Flask-Boiler plate with Bootstrap
Copyright 2013-19 Dr. Syed Awase Khirni
TPRI/SYCLIQ GEOSPATIAL PVT LTD.


Boilerplate template Folder Structure 

boilerplateprj/
...boilerplateapp/
.......__init__.py
.......config.py
.......controllers.py
.......filters.py
.......models.py
.......dbscript.py
.......admin/
..............__init__.py
..............controllers.py 
...static/
......css/
......images/
......fonts/
......js/
...templates/
.......base.html 
.......errors/
..........404.html 
..........500.html
..........403.html 
........home/
..........index.html 
..........dashboard.html 
........auth/
...........login.html 
...........register.html
...........password_change.html 
.........admin/
..............index.html
.........layouts/
..............dashboard_layout.html
..............grid_viewlayout.html 
..............homepage_layout.html 
..............profile_layout.html
..............reporting_layout.html 
..............single_product_view.html 
..............three_col_sidebar_layout.html
..............two_col_sidebar_layout.html


Dependency packages installation

python -m venv flaskenv
cd scripts
./activate 

cd ..
 
 #install flask 
 pip install flask 
 python -m pip install --upgrade pip
 pip install flask-SQLAlchemy flask-moment flask-login werkzeug psycopg2 flask-bootstrap flask-debugtoolbar

 #flask-script 
 pip install flask-script 
 
 #flask dependencies for wtforms 
 pip install flask-wtf wtforms flask-SQLAlchemy
 
 cd project 
 python manage.py runserver 

 Open in browser 
 http://localhost:9090/ 
 http://localhost:9090/dashboard 
