# FHIR File Transfer

This is a package used to generating letters, forms and documents prefilled from FHIR records. It can create two types of files
* PDF
* Word

## Steps
* Clone the project and open it in Visual Studio Code or Pycharm.
* Activate the virtual environment `source venv/bin/activate`
* Run the *Demo.py* by command `python3 Demo.py`
* Open a web browser and go to http://127.0.0.1:5000/ to start

## Available API endpoints
| Download files with all patients |
| --- |  
| `GET`  */api/patients/pdf* |  
| `GET`  */api/patients/doc* |

(Example files have been contained here)
