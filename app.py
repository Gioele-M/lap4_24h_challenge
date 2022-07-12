from db import add_link, delete_link, get_long_link, get_links_by_ip, check_short_exists, check_number_clicks, add_clicked_to_link

from flask import Flask, request
from flask_cors import CORS
import random, string


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



@app.route('/', methods=['GET', 'POST'])
def home_route():
    if request.method == 'GET':
        # return render template home
        # use get_links_by_ip to see if anything has to be displayed
        return 'Home directory', 200
    if request.method == 'POST':
        #get long link from page form
        long = 'Temporary long'
        #generate short link
        short = generate_short_url()
        #Get user ip
        ip_addr = request.remote_addr
        #Initialise link
        add_link(long, short, ip_addr, 0)
        # Return rendered template same as in get
        return 'Home directory', 204


# Make route /<var> to redirect users+add click if get, delete if delete

