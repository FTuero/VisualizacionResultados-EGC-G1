from ..logic.poll_service import find_poll
from flask import render_template, Response,json
from .. import app
from ..logic.question_service import question_option_result
from .login_required import login_required
import requests
from ..model import Question, session

@app.route('/visres/<poll_id>/anwsers')
@login_required
def anwsers(poll_id):

    poll = find_poll(poll_id)

    def votes_question(qo_id):
        votes =  question_option_result(qo_id)
        return votes

    return render_template('answer.html', poll=poll,votes_question=votes_question)




@app.route('/visres/votes/<question_id>/<num>') #se le pasa la id de la pregunta y el contador de cada opcion
def votes_data(question_id,num):
    question = session.query(Question).get(question_id)     #obtenemos la pregunta
    poll_id = question.poll.id #y de ahi sacamos la id de la encuesta

    j = requests.get('https://g1recvotos.egc.duckdns.org/recvotes/'+str(poll_id)) #usamos la id para sacar la informacion a traves de peticion json
                                            #puede mejorarse para que no lo haga por cada pregunta sino solo una vez
    options = ""
    quantities2 = ""
    d = j.json()
    num = int(num)
    i = 0
    for pregunta in d:  #recorremos el json
        quantities = pregunta['questionoption_set'] #obtenemos la parte de descripcion y votos

        if i == num:

            for q in quantities:

                if len(str(q['description']))>3:  #si la descripcion es mayor de 3 caracteres, acortalo
                    options += '"'+str(q['description'][:3])+'",'
                    quantities2 += str(q['result']['quantity']) + "," #acumulamos los votos
                else:
                    options += '"' + str(q['description'])+ '",'
                    quantities2 += str(q['result']['quantity'])+","
            break
        i+=1

    quantities2 = quantities2[:-1] #elimina la coma
    options = options[:-1]  #elimina la coma

    res = Response('{"len":'+str(len(quantities2))+',"labels":['+options+'], "data":['+quantities2+']}') #les pasamos los valores
    res.headers["Content-Type"] = "application/json"

    return res
