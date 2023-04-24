from flask import Flask, render_template, redirect, send_from_directory, request, make_response
from utils.RiotLogin import Auth
from utils.GetPlayer import player
from utils.Cache import updateCache
from utils.Weapon import weapon
import _thread

app = Flask(__name__)
app.template_folder = 'templates'


@app.route('/', methods=['GET'])
def home():
    if request.cookies.get('logged') == '1':
        return redirect('/market', 301)
    else:
        response = make_response(render_template(
            'index.html', loginerror=False))
        response.set_cookie('logged', '0', max_age=24*60*60*365*10)
    return response


@app.route('/market', methods=['GET'])
def market():
    cookie = request.cookies
    access_token = cookie.get('access_token')
    entitlement = cookie.get('entitlement_token')
    region = cookie.get('region')
    userid = cookie.get('user_id')
    user = player(access_token, entitlement, region, userid)
    weapon0, weapon1, weapon2, weapon3= {}, {}, {}, {}
    if user.auth:
        shop = user.shop['SkinsPanelLayout']    # Flite the daily skin
        weapon0 = weapon(shop['SingleItemStoreOffers'][0]['OfferID'],
                         shop['SingleItemStoreOffers'][0]["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"])
        weapon1 = weapon(shop['SingleItemStoreOffers'][1]['OfferID'],
                         shop['SingleItemStoreOffers'][1]["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"])
        weapon2 = weapon(shop['SingleItemStoreOffers'][2]['OfferID'],
                         shop['SingleItemStoreOffers'][2]["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"])
        weapon3 = weapon(shop['SingleItemStoreOffers'][3]['OfferID'],
                         shop['SingleItemStoreOffers'][3]["Cost"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"])
        return render_template('myMarket.html', market=True,
                               weapon0={
                                   "name": weapon0.name, "cost": weapon0.cost, "img": weapon0.base_img},
                               weapon1={
                                   "name": weapon1.name, "cost": weapon1.cost, "img": weapon1.base_img},
                               weapon2={
                                   "name": weapon2.name, "cost": weapon2.cost, "img": weapon2.base_img},
                               weapon3={"name": weapon3.name, "cost": weapon3.cost, "img": weapon3.base_img})
    else:   # Login Expired
        response = make_response(redirect('/', 302))
        for cookie in request.cookies:
            response.delete_cookie(cookie)
        return response


@app.route('/market/black', methods=['GET'])
def black():
    cookie = request.cookies
    access_token = cookie.get('access_token')
    entitlement = cookie.get('entitlement_token')
    region = cookie.get('region')
    userid = cookie.get('user_id')
    user = player(access_token, entitlement, region, userid)
    weapon0, weapon1, weapon2, weapon3, weapon4, weapon5 = {}, {}, {}, {}, {}, {}
    if user.auth:
        blackmarket = user.shop['BonusStore']
        weapon0 = weapon(blackmarket['BonusStoreOffers'][0]['Offer']['OfferID'], blackmarket['BonusStoreOffers'][0]['Offer']['Cost']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"],
                         blackmarket['BonusStoreOffers'][0]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"], blackmarket['BonusStoreOffers'][0]['DiscountPercent'])
        weapon1 = weapon(blackmarket['BonusStoreOffers'][1]['Offer']['OfferID'], blackmarket['BonusStoreOffers'][1]['Offer']['Cost']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"],
                         blackmarket['BonusStoreOffers'][1]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"], blackmarket['BonusStoreOffers'][1]['DiscountPercent'])
        weapon2 = weapon(blackmarket['BonusStoreOffers'][2]['Offer']['OfferID'], blackmarket['BonusStoreOffers'][2]['Offer']['Cost']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"],
                         blackmarket['BonusStoreOffers'][2]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"], blackmarket['BonusStoreOffers'][2]['DiscountPercent'])
        weapon3 = weapon(blackmarket['BonusStoreOffers'][3]['Offer']['OfferID'], blackmarket['BonusStoreOffers'][3]['Offer']['Cost']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"],
                         blackmarket['BonusStoreOffers'][3]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"], blackmarket['BonusStoreOffers'][3]['DiscountPercent'])
        weapon4 = weapon(blackmarket['BonusStoreOffers'][4]['Offer']['OfferID'], blackmarket['BonusStoreOffers'][4]['Offer']['Cost']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"],
                         blackmarket['BonusStoreOffers'][4]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"], blackmarket['BonusStoreOffers'][4]['DiscountPercent'])
        weapon5 = weapon(blackmarket['BonusStoreOffers'][5]['Offer']['OfferID'], blackmarket['BonusStoreOffers'][5]['Offer']['Cost']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"],
                         blackmarket['BonusStoreOffers'][5]['DiscountCosts']["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"], blackmarket['BonusStoreOffers'][5]['DiscountPercent'])
        print(weapon1.data)
        return render_template('myMarket.html', black=True,
                            weapon0={
                                "name": weapon0.name, "cost": weapon0.cost, "img": weapon0.base_img, "discount": weapon0.discount, "per": weapon0.per},
                            weapon1={
                                "name": weapon1.name, "cost": weapon1.cost, "img": weapon1.base_img, "discount": weapon1.discount, "per": weapon2.per},
                            weapon2={
                                "name": weapon2.name, "cost": weapon2.cost, "img": weapon2.base_img, "discount": weapon2.discount, "per": weapon2.per},
                            weapon3={
                                "name": weapon3.name, "cost": weapon3.cost, "img": weapon3.base_img, "discount": weapon3.discount, "per": weapon3.per},
                            weapon4={
                                "name": weapon4.name, "cost": weapon4.cost, "img": weapon4.base_img, "discount": weapon4.discount, "per": weapon4.per},
                            weapon5={
                                "name": weapon5.name, "cost": weapon5.cost, "img": weapon5.base_img, "discount": weapon5.discount, "per": weapon5.per})
    else:   # Login Expired
        response = make_response(redirect('/', 302))
        for cookie in request.cookies:
            response.delete_cookie(cookie)
        return response



@app.route('/EULA', methods=["GET", "POST"])
def EULA():
    return render_template('EULA.html')


@app.route('/api/login', methods=['POST'])
def RiotLogin():
    username = request.form.get('Username')
    password = request.form.get('Password')
    checked_rule = request.form.get('CheckedRule')
    checked_eula = request.form.get('CheckedEULA')
    if username == '' or password == '' or not checked_eula or not checked_rule:
        return render_template('index.html', infoerror=True)
    else:
        user = Auth(username, password)
        user.auth()
        if user.authed:
            response = make_response(render_template('myMarket.html'))
            response.set_cookie('access_token', user.access_token)
            response.set_cookie('entitlement_token', user.entitlement)
            response.set_cookie('region', user.Region)
            response.set_cookie('username', user.Name)
            response.set_cookie('tag', user.Tag)
            response.set_cookie('user_id', user.Sub)
            response.set_cookie('logged', '1')
            response.status_code = 200
        else:
            response = make_response(
                render_template('index.html', loginerror=True))
        return response


@app.route('/assets/<path:filename>')
def serve_static(filename):
    return send_from_directory('assets', filename)


if __name__ == '__main__':
    _thread.start_new_thread(updateCache, ())
    app.run(host='0.0.0.0', port=8080, debug=True)
