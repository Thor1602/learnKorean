# -*- coding: utf-8 -*-
from flask import Flask, url_for, render_template, request, redirect, session, jsonify
from dbHelper import Topics, User

UPLOAD_FOLDER = 'static/assets/img/user_pictures/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(import_name=__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
data = []
@app.before_request
def make_session_permanent():
    session.permanent = True

@app.route("/topics", methods=['GET', 'POST'])
def topics():
    general_info = "-----This info changes constantly and can create difficulties for web scraping.-----"
    topic = Topics()
    global data
    if request.method == "POST":
        print(request.form)
        if 'homepage' in request.form:
            data = ["" for row in range(20)]
        elif 'subject_marker' in request.form:
            data = topic.check_topic()[0]
        elif 'object_marker' in request.form:
            data = topic.check_topic()[1]
        elif 'shiot_irregular' in request.form:
            data = topic.check_topic()[2]
        elif 'speech_levels' in request.form:
            data = topic.check_topic()[3]
        elif 'digeut_irregular' in request.form:
            data = topic.check_topic()[4]
        elif 'bieup_irregular' in request.form:
            data = topic.check_topic()[5]
        elif 'verb_ending_neyo' in request.form:
            data = topic.check_topic()[6]
        elif 'connecting_verbs' in request.form:
            data = topic.check_topic()[7]
        elif 'prepositions_of_place' in request.form:
            data = topic.check_topic()[8]
        elif 'shall_we' in request.form:
            data = topic.check_topic()[9]
        elif 'approximately' in request.form:
            data = topic.check_topic()[10]
        elif 'lieul_eu_irregular' in request.form:
            data = topic.check_topic()[11]
        elif 'linking_verbs' in request.form:
            data = topic.check_topic()[12]
        elif 'even_if' in request.form:
            data = topic.check_topic()[13]
        elif 'after_ing' in request.form:
            data = topic.check_topic()[14]
        # elif '' in request.form:
        #     data = topic.check_topic()[15]
        # elif '' in request.form:
        #     data = topic.check_topic()[16]
        # elif '' in request.form:
        #     data = topic.check_topic()[17]
        # elif '' in request.form:
        #     data = topic.check_topic()[18]
        # elif '' in request.form:
        #     data = topic.check_topic()[19]
        # elif '' in request.form:
        #     data = topic.check_topic()[20]
        # elif '' in request.form:
        #     data = topic.check_topic()[21]
        # elif '' in request.form:
        #     data = topic.check_topic()[22]
        # elif '' in request.form:
        #     data = topic.check_topic()[23]
        # elif '' in request.form:
        #     data = topic.check_topic()[24]
        # elif '' in request.form:
        #     data = topic.check_topic()[25]
    return jsonify(data=data, aaa_general_info=general_info)

@app.route("/refresh", methods=['GET', 'POST'])
def refresh():
    general_info = "-----This info changes constantly and can create difficulties for web scraping.-----"
    topic1 = Topics()
    all_topics = [[topic[1], topic[2], topic[3]] for topic in topic1.check_topic()]
    return jsonify(all_topics=all_topics, aaa_general_info=general_info)


@app.route("/", methods=['GET', 'POST'])
def home():
    err = ''
    success = ''
    return render_template("index.html")

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    err = ''
    success = ''
    topicObj = Topics()

    if request.method == "POST":
        if 'new_entry' in request.form:
            topicObj.add_topic(topic=request.form['topic'],
                               title=request.form['title'],
                               description=request.form['description'],
                               rule1=request.form['rule1'],
                               rule2=request.form['rule2'],
                               rule3=request.form['rule3'],
                               rule4=request.form['rule4'],
                               rule5=request.form['rule5'],
                               rule6=request.form['rule6'],
                               rule7=request.form['rule7'],
                               rule8=request.form['rule8'],
                               example1=request.form['example1'],
                               example2=request.form['example2'],
                               example3=request.form['example3'],
                               example4=request.form['example4'],
                               example5=request.form['example5'],
                               example6=request.form['example6'],
                               example7=request.form['example7'],
                               example8=request.form['example8'],
                               )
    return render_template("admin.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login Form"""
    # if session.get('logged_in'):
    #     return redirect(url_for('admin'))
    if session.get('logged_in'):
        return redirect(url_for('admin'))
    if request.method == 'GET':
        return render_template('login.html')
    else:
        condition = False
        name = request.form['username']
        passw = request.form['password']

        try:
            user = User(name, passw, True)
            if user.check_user():
                session['logged_in'] = True
                if 'rememberMe' in request.form:
                    session.permanent = True
                else:
                    session.permanent = False
                return redirect(url_for('admin'))
            else:
                condition = True
                err = "Oops, the credentials don't match"
                return render_template('login.html', err=err, condition=condition)
        except:
            err = 'Something strange happened while trying to log in'
            return render_template('404.html', err=err, condition=condition)

@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('home'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', err=e), 404

@app.errorhandler(403)
def forbidden(e):
    return render_template('404.html', err=e), 403

@app.errorhandler(410)
def page_gone(e):
    return render_template('404.html', err=e), 410

@app.errorhandler(500)
def internal_error(e):
    return render_template('404.html', err=e), 500

if __name__ == "__main__":
    app.secret_key = "HopKIdf78/*9*PO72xQ89Fg??"
    app.run(debug=True)




















