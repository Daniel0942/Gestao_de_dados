from setup import app
from setup.models.table import criarTabelas

if __name__ == "__main__":
    criarTabelas()
    app.run(debug=True)