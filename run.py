from configuration import config

from flask import Flask, jsonify, request
from textblob import TextBlob

app = Flask(__name__)
app.config["DEBUG"] = False


def authorize_request(request):
    print(request)
    if request.headers.get("Authorization") is not None:
        if request.headers.get("Authorization") != "Bearer " + config.auth_token:
            return app.response_class(
                response="Invalid access token provided",
                status=401
            )
        return True
    else:
        return app.response_class(
            response="No access token provided",
            status=401
        )


@app.route('/detect-language', methods=['POST'])
def detectLanguage():
    if (request.method == 'POST'):
        auth_result = authorize_request(request)
        if auth_result is not True:
            return auth_result
        else:
            if request.headers.get('Id') is not None and request.get_json() is not None and request.get_json() != {}:
                if request.headers.get('Id') in config.allowed_devices:
                    bodyData = request.get_json()
                    textToBeTested = bodyData['text']
                    if len(textToBeTested) >=500:
                        textToBeTested = textToBeTested[:100]
                    
                    textInTextBlob = TextBlob(textToBeTested)
                    langCode = textInTextBlob.detect_language()
                    
                    return jsonify({ "language" : langCode, "text" : "The language of this text is: "+ langCode})
                else:
                   return app.response_class(
                response="Invaild Device ID",
                status=401
            )

            else:
                return app.response_class(
                       response="Unprocessable Entity",
                       status=422)
    else:
        return app.response_class(
            response="Method Not Allowed",
            status=405
        )

@app.route('/')
def status():
    if (request.method == 'GET'):
        auth_result = authorize_request(request)
        if auth_result is not True:
            return auth_result
        else:
            return app.response_class(
            response="Service is running",
            status=200
        )
    else:
        return app.response_class(
            response="Method Not Allowed",
            status=405
        )

if __name__ == '__main__':    
    app.run(debug=True,host='0.0.0.0', port=5005)    
