from db import add_link, delete_link, get_long_link, get_links_by_ip, check_short_exists, check_number_clicks, add_clicked_to_link

from flask import Flask, request, send_file, redirect, jsonify, render_template
from flask_cors import CORS
import random, string
import json

import qrcode
from io import BytesIO


app = Flask(__name__)

CORS(app)


def generate_short_url():
    viable_chars = string.ascii_letters + string.digits
    result = ''
    for _ in range(5):
        result += random.choice(viable_chars)
    exists = check_short_exists(result)
    if not exists:
        return result
    else:
        return generate_short_url()

# Route to generate QR code
@app.route('/generateQRCode/<url>', methods=['GET'])
def generate_qrcode(url):
    buffer = BytesIO()
    img = qrcode.make(f'https://shortboi.herokuapp.com/{url}')
    img.save(buffer)
    buffer.seek(0)

    response = send_file(buffer, mimetype='image/png')
    return response



# Home route
@app.route('/', methods=['GET', 'POST'])
def home_route():
    ip_addr = request.remote_addr
    if request.method == 'GET':
        # return render template home
        # use get_links_by_ip to see if anything has to be displayed
        status = 200
    if request.method == 'POST':
        #get long link from page form
        long = request.form['input']
        #generate short link
        short = generate_short_url()
        #Get user ip
        #Initialise link
        add_link(long, short, ip_addr, 0)
        # Return rendered template same as in get
        status = 204
    user_specific_links = get_links_by_ip(ip_addr)
    return render_template('results.html', user_specific_links=user_specific_links)
    # return jsonify(user_specific_links), status


# Make route /<var> to redirect users+add click if get, delete if delete
@app.route('/<short>', methods=['GET', 'DELETE'])
def redirect_and_delete(short):
    if request.method == 'GET':
        to_redirect = get_long_link(short)
        if to_redirect == False:
            return '404 page!', 404
        add_clicked_to_link(short)
        return redirect(to_redirect)
    if request.method == 'DELETE':
        deleted = delete_link(short)
        return str(deleted), 204
