from model.empleados_routes import empleados
from model.categorias_routes import categorias
from model.platillos_routes import platillos
from util.Aplication import Aplication

aplication = Aplication()
app = aplication.app
app.register_blueprint(empleados)
app.register_blueprint(categorias)
app.register_blueprint(platillos)


def pagina_no_encontrada(error):
    return "<h1>Método no encontrado</h1>"

if __name__ == "__main__":
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)
