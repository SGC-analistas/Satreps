"""
SGC_satreps1.0
Es una página web creada para visualizar los eventos del proyecto SATREPS

autores: - Emmanuel Castillo ecastillo@sgc.gov.co
         - Angel agudelo adagudelo@sgc.gov.co
04-2020
"""
import os
import argparse
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple

from home import app as dash_app_home
from index import app as dash_app_index

application = DispatcherMiddleware(dash_app_index.server, {
    '/home': dash_app_home.server,
})


def read_args():
    prefix = "+"
    ini_msg = "#"*120
 

    parser = argparse.ArgumentParser("Visualizacion escenarios Satreps. ",prefix_chars=prefix)

    parser.add_argument(prefix+"s",prefix*2+"server",
                        type=str,
                        metavar='',
                        help="Servidor, ejemplo: 10.100.100.11", required = True)

    parser.add_argument(prefix+"p",prefix*2+"port",
                        type=int,
                        metavar='',
                        help="Puerto, ejemplo: 8050", required = True)

    parser.add_argument(prefix+"es",prefix*2+"escenario_server",
                        type=str,
                        metavar='',
                        help="Servidor de escenario (web_page). ejemplo: 10.100.100.11", 
                        required = True)

    parser.add_argument(prefix+"ep",prefix*2+"escenario_port",
                        type=int,
                        metavar='',
                        help="Puerto del escenario (web_page) . ejemplo: 8090", 
                        required = True)

    args = parser.parse_args()
    # vars_args = vars(args)
    return args


def write_escenario(server,port):
    path = os.path.join(os.path.dirname(__file__),'escenario.txt')
    f = open(path,"w")
    f.write(f"http://{server}:{port}")
    f.close()

if __name__ == '__main__':
    args = read_args()
    write_escenario(args.escenario_server,args.escenario_port)
    run_simple(args.server, args.port, application,threaded=True)



#REFERENCES
## https://dash.plotly.com/integrating-dash correr flask y dash simultaneamente
## http://www.compjour.org/lessons/flask-single-page/multiple-dynamic-routes-in-flask/ crear multiples rutas en flask
## https://dash.plotly.com/sharing-data-between-callbacks compartir datos entre callbacks