from flask import Flask, render_template, request, redirect, url_for
import smart_rolladen

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'UG_SCHLAFEN AUF':
            smart_rolladen.up("UG_SCHLAFEN", 0.3)

        elif  request.form.get('action2') == 'UG_SCHLAFEN AB':
            smart_rolladen.down("UG_SCHLAFEN", 0.3)

        elif  request.form.get('action3') == 'UG_KIND AUF':
            smart_rolladen.up("UG_KIND", 0.3)

        elif  request.form.get('action4') == 'UG_KIND AB':
            smart_rolladen.down("UG_KIND", 0.3)

        elif  request.form.get('action5') == 'UG_KOCHEN_WOHNEN AUF':
            smart_rolladen.up("UG_KOCHEN_WOHNEN", 0.3)

        elif  request.form.get('action6') == 'UG_KOCHEN_WOHNEN AB':
            smart_rolladen.down("UG_KOCHEN_WOHNEN", 0.3)

        elif  request.form.get('action7') == 'OG_BUERO AUF':
            smart_rolladen.up("OG_BUERO", 0.3)

        elif  request.form.get('action8') == 'OG_BUERO AB':
            smart_rolladen.down("OG_BUERO", 0.3)

        elif  request.form.get('action9') == 'OG_SCHLAFEN AUF':
            smart_rolladen.up("OG_SCHLAFEN", 0.3)

        elif  request.form.get('action10') == 'OG_SCHLAFEN AB"':
            smart_rolladen.down("OG_SCHLAFEN", 0.3)

        elif  request.form.get('action11') == 'OG_KOCHEN AUF':
            smart_rolladen.up("OG_KOCHEN", 0.3)

        elif  request.form.get('action12') == 'OG_KOCHEN AB':
            smart_rolladen.down("OG_KOCHEN", 0.3)

        elif  request.form.get('action13') == 'OG_WOHNEN AUF':
            smart_rolladen.up("OG_WOHNEN", 0.3)

        elif  request.form.get('action14') == 'OG_WOHNEN AB':
            smart_rolladen.down("OG_WOHNEN", 0.3)

        elif  request.form.get('action15') == 'OG_BAD AUF':
            smart_rolladen.up("OG_BAD", 0.3)

        elif  request.form.get('action16') == 'OG_BAD AB':
            smart_rolladen.down("OG_BAD", 0.3)   

        else:
            pass # unknown
        return redirect(url_for("index"))
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")