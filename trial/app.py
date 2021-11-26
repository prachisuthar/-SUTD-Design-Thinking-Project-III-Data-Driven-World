from flask import Flask, redirect, url_for, render_template, request
import math 
app = Flask(__name__)


if __name__ == "main":
    app.run(debug=True)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/task1", methods=["POST","GET"])
def task1data():
    if request.method == "POST":
        ans_continent = request.form["continent"]
        ans_si = request.form["stringency_index"]
        ans_si = float(ans_si)
        ans_newc = request.form["new_cases"]
        ans_newc = float(ans_newc)
        ans_days = request.form["days"]
        ans_days = float(ans_days)
 
        if ans_continent == "Africa":
            new_cases_norm_z = (ans_newc -4222.12637362637)/3103.15777856675
            stringency_idx_norm_z = (ans_si -55.8906611721612)/11.3800129174173
            days_norm_z = (ans_days -274.642857142857)/159.173296347053
            ans = 42.9000021718883 * new_cases_norm_z - 4.46498971886486 * stringency_idx_norm_z + 16.7382721249813 * days_norm_z +118.833333333333
            return render_template("task1.html", ans=ans)

        if ans_continent == "Asia":
            new_cases_norm_z = (ans_newc -118762.059459459)/104109.856300417
            stringency_idx_norm_z = (ans_si -63.9281132561132)/4.48168773289801
            days_norm_z = (ans_days -278.816216216216)/161.150014500101
            ans = 953.303955823045 * new_cases_norm_z + 52.4164432836236 * stringency_idx_norm_z + 305.31917121472 * days_norm_z + 1752.69009009009
            return render_template("task1.html", ans=ans)

        if ans_continent == "Europe":
            new_cases_norm_z = (ans_newc -97401.9694244604)/72841.9443102294
            stringency_idx_norm_z = (ans_si -57.7257571942446)/10.8329598975599
            days_norm_z = (ans_days -278.735611510791)/160.9601267557
            ans = 955.560232162802 * new_cases_norm_z + 977.286449234169 * stringency_idx_norm_z + 168.072295625687 * days_norm_z + 1997.62949640288
            return render_template("task1.html", ans=ans)

        if ans_continent == "North America":
            new_cases_norm_z = (ans_newc -92253.3956834532)/73950.9406693085
            stringency_idx_norm_z = (ans_si -69.0802617905675)/7.55126297777485
            days_norm_z = (ans_days -278.714028776978)/160.939536128713
            ans = 996.272320766661 * new_cases_norm_z + 629.541732543122 * stringency_idx_norm_z + 202.983092111427 * days_norm_z + 1856.72841726619
            return render_template("task1.html", ans=ans)

        if ans_continent == "South America":
            new_cases_norm_z = (ans_newc -52838.4128440367)/32637.8250449635
            stringency_idx_norm_z = (ans_si -71.6219021406726)/9.23395334035689
            days_norm_z = (ans_days -276.111926605505)/161.038199777698
            ans = 946.632798757314 * new_cases_norm_z + 693.70288152919 * stringency_idx_norm_z + 563.67238113726 * days_norm_z + 1675.84036697247
            return render_template("task1.html", ans=ans)

        if ans_continent == "Oceania":
            new_cases_norm_z = (ans_newc -183.001795332136)/402.247255196748
            stringency_idx_norm_z = (ans_si -64.0400000000001)/10.2857672671202
            days_norm_z = (ans_days -279)/160.936322811229
            ans = 2.1240508072714 * new_cases_norm_z + 1.19258966579852 * stringency_idx_norm_z - 0.899898710376497 * days_norm_z + 2.28366247755836

            return render_template("task1.html", ans=ans)
    else:
        return render_template("task1.html")


@app.route("/task2", methods=["POST","GET"])
def task2data():
    if request.method == "POST":
        new_cases = request.form["new_cases"]
        vacc_rate = request.form["vacc_rate"]
        total_deaths = request.form["total_deaths"]
        icu = 0.26303055 + 0.14382207* (float(new_cases)) + 0.01749679* (1 - float(vacc_rate)) + 0.04144739 * (- math.log(1 - float(vacc_rate))) + 0.13505927 *(math.log(float(total_deaths)))
        return render_template("task2.html", icu = icu)

    else:
        return render_template("task2.html")

