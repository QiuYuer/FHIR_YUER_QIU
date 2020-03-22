import sys
import os
path = os.getcwd()
sys.path.insert(0, os.path.join(path[:len(path)-5], 'API'))
from flask import Flask, redirect, request, Response

from FHIR import FHIR_response
from TransferApi import *

app = Flask(__name__)

_fhir = FHIR_response()
_data = _fhir.get_all_patients()

@app.route('/')
def index():
    return """
    <h1> FHIR API demo </h1>
    """


@app.route('/api/patients/doc', methods=['GET'])
def download_word():
    testJSONtoWord(_data)
    return """
    <h3> Word download successful! </h3>        
    """


@app.route('/api/patients/pdf', methods=['GET'])
def download_PDF():
    testJSONtoPdf(_data)
    return """
     <h3> PDF download successful! </h3>            
     """


if __name__ == '__main__':
    app.run()
