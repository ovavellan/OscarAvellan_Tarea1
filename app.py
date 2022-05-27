
#importar libreria de Flask
from tkinter import SW
from flask import Flask, render_template

#Iniciar variable de aplicacion 
app= Flask(__name__, template_folder='templates')

#decorador para definir la ruta raíz e index 
@app.route('/' )
def principal():
    return render_template('index.html')


# main del programa 
if __name__ == '__main__':
    #debug = true, para reiniciar automaticamente el servidor , tiemo de desarrollo 
    app.run(debug=True)