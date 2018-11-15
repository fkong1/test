import os

ip = os.environ['IP']
port = os.environ['PORT']

app = None
if 'MAINIP' in os.environ:
    import slave
    app = slave.create_app(os.environ['MAINIP'])
else:
    import master
    import db
    app = master.create_app(db.InMemoryDB())

app.run(host=ip, port=port)

