from api import create_app
app = create_app('adventureworks', 'postgres', 'afrocs221994' )
app.run(debug = True)