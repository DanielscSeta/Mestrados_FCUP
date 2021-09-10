# save this as app.py
from flask import Flask, request, render_template, session, redirect, request
from data import *
from functions import *
import requests

app = Flask(__name__, template_folder="templates")

###### Gerar nova imagem de plot ######
# @app.route('/plot')
# def chartTest():
#     Sobrantes_df = tab_sobrantes()
#     plt.figure(figsize=(15,8))
#     plt.bar(Sobrantes_df.index, Sobrantes_df['Sobrantes'])
#     plt.xticks(rotation=90)
#     # plt.savefig('./static/images/new_plot.png')
#     plt.savefig('./static/images/new_plot.png',bbox_inches='tight')

#     return render_template('plot.html', name = 'new_plot', url ='/static/images/new_plot.png')
@app.route('/suggestions')
def suggestions():
    text = request.args.get('jsdata')
    print(text)

    suggestions_list = stalker(text)

    return render_template('suggestions.html', suggestions=suggestions_list)



@app.route('/', methods=("POST", "GET"))
def html_table():
    if request.form.get('comp_select') is not None:
        select = request.form.get('comp_select')
        return(redirect(select)) 

    Sobrantes_df = tab_sobrantes()
    header = Sobrantes_df.columns.values.tolist()
    header.insert(0,Sobrantes_df.index.name)
    return render_template('index.html', data=Mestrados, header1=header, data1=Sobrantes_df.to_records(index=True),
    url ='/static/images/new_plot.png')

# @app.route("/test" , methods=['GET', 'POST'])
# def test():
#       select = request.form.get('comp_select')
#       return(redirect(select)) 

    

@app.route('/<var>', methods=("POST", "GET"))
def company(var):
    colocados = d["df_2_{0}".format(var)]
    header1 = colocados.columns.values.tolist()
    header1.insert(0,colocados.index.name)


    if d["df_1_{0}".format(var)][1][0] < d["df_1_{0}".format(var)][1][1]:
        candidatos = d["df_3_{0}".format(var)]
        header2 = candidatos.columns.values.tolist()
        header2.insert(0,candidatos.index.name)
    else:
         header2=()
         candidatos=pd.DataFrame()
    # return render_template('simple.html', var=var.replace("_", " "), header = df_sup.columns,  data = lista[var].values)
    return render_template('simple.html', select=Mestrados, var=var, data=table1(var), data2=table2(var),
     header=header1 , data3=colocados.to_records(index=True), header2=header2, data4=candidatos.to_records(index=True))



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')