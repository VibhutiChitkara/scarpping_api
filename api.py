from flask import Flask, request
import json
from scraping import scrape_game

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """
    Base path to check if the service is running
    """
    return (str('Service is running')), 200



@app.route('/scraper', methods=['GET'])
def run_scraper():
    url=request.args['url']
    #base_url = request.args['base_url']
    #comp_id = request.args['comp_id']
    #match_id = request.args['match_id']
    #date = request.args['date']
    #url = base_url+"?comp_id="+comp_id+"&match_id="+match_id+"&date="+date

    print(url)
    
    status, output = scrape_game(url)
    
    if status:
        return (output), 200
    else:
        return ("ERROR"), 500

@app.errorhandler(500)
def server_error(e):
    """
    Handling errors with 500 error. 
    If more specific error handling is required, 
    it should be custom handles with each endpoint
    """
    
    #logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    """
    Running the Flask application in local.
    Set debug=True for local testing and False for deployments
    """
    app.run(host='0.0.0.0', port=5000, debug = True)  #PORT should 5000 as our cluster by default listen on 5000