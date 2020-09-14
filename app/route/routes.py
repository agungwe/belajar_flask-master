from app import app
from app.controllers import controllerRoute

@app.route('/ctr')
def testctr():
    return controllerRoute.fungsiController()
@app.route('/ctr/')
@app.route('/ctr/<parameter>')
def testctParameter(parameter="kosong"):
    return controllerRoute.fungsiControllerParameter(parameter)

@app.route('/')
def index():    #routes diatas, membaca satu def ini
    return "Hello ,World!"

 
# @app.route('/users/')
# @app.route('/user/<name>') 
# @app.route('/user/')
# def tesParameter(name="kosong"): # 3 routes diatas, membaca satu def ini
#     return f"Hello,{name}!"

# @app.route('/users_coba/')
# @app.route('/users_coba/<name>')
# def tesParameter1(name="kosong"):# 2 routes diatas, membaca satu def ini
#     return f"coba,{name}!" 