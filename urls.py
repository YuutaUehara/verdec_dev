from .controller import * 


# FastAPIのルーティング用関数
app.add_api_route('./', top)
app.add_api_route('./register', register, methods=['GET', 'POST']) 

#app.add_api_route('/register', register)