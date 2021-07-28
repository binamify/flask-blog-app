
#importing create_app function from self made module i.e webiste folder
from website import create_app

#Inside __init__.py app is used and it has __name__
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
