from sqlalchemy.sql.functions import current_user, user
from website import create_app
from flask import Flask , render_template
from website.models import User

app = create_app()

@app.route('/')
def login_page():
    return render_template('login.html' , user = current_user)

if __name__ == '__main__':
    app.run(debug=True,port=2002)
