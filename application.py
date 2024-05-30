from flask import Flask, render_template, request
from ifb import IFB_Feb2024
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.htm')

@app.route("/payout")
def payout():
    face_value=request.args.getlist("face_value")[0]
    if len(face_value) == 0:
        face_value = "50,000"
    ifb_inst = IFB_Feb2024(face_value=face_value)
    if ifb_inst.face_value == 0:
        ifb_inst.face_value = 50000
        ifb_inst.original_face_value = 50000
    interests = ifb_inst.interests
    earnings = ifb_inst.all_earnings
    amortization = ifb_inst.amortization
    if amortization:
        first_date_amo = amortization[0]["date"]
        first_amo = amortization[0]["amortized"]
        last_date_amo = amortization[1]["date"]
        last_amo = amortization[1]["amortized"]
    else:
        first_date_amo = ifb_inst.first_armotization["date"]
        first_amo = 0
        last_date_amo = ifb_inst.second_armotization["date"]
        last_amo = 0

    return render_template("payout.html", 
                           interests=interests, 
                           earnings=earnings, 
                           face_value=ifb_inst.original_face_value,
                           first_date_amo = first_date_amo,
                           first_amo = first_amo,
                           last_date_amo = last_date_amo,
                           last_amo = last_amo,
                           total_amortization = ifb_inst.total_amortization,
                           years_of_investment=int(len(interests)/2))

if __name__ == "__main__":
    app.run(debug=False, port=5000)
