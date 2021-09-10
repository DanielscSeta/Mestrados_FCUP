from flask_frozen import Freezer
from app import app, Mestrados

freezer = Freezer(app)

@freezer.register_generator
def company():
    for product in Mestrados:
        yield "/" + product

if __name__ == '__main__':
    freezer.freeze()