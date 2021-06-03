from flask import Flask,request,render_template
import pickle
from googleapiclient.discovery import build
from google.oauth2 import service_account
import os
from twilio.rest import Client

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("test.html")

database={'Samiya Jabbar':'girl','Muhammad Naufil':'boy'}

@app.route('/abc',methods=['POST','GET'])
def contact():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Package not Received':
            SERVICE_ACCOUNT_FILE = 'keys-food.json'
            SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
            creds = None
            creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
            # The ID and range of a sample spreadsheet.
            SAMPLE_SPREADSHEET_ID = '1DxYub7bbxV_h2AR2lAp8aaTyuy52bmKNsKY8nPTHCnw'
            service = build('sheets', 'v4', credentials=creds)

            #if button==button1:  
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="recording2!B1:B100").execute()
            value= result.get('values')
            number=value
            print(number)
            for sublist in number:
                for item in sublist:
                    print(item)

            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)

            call = client.calls.create(
                                    twiml='<Response><Say>Hey, This is Dennys calling from retail investment group. I saw you are an owner of retail property. The reason i am calling is I thought you might want an updated accurate evaluation of your propety free of charge. If you could return my call at 5412139338, once again that 5412139338. Or you can also text interested.!</Say></Response>',
                                    to=item,
                                    from_='+12408984424'
                                )

            print(call.sid)

            return '203' 

        if request.form['submit_button'] == 'Package Received':

            SERVICE_ACCOUNT_FILE = 'keys-food.json'
            SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
            creds = None
            creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
            # The ID and range of a sample spreadsheet.
            SAMPLE_SPREADSHEET_ID = '1DxYub7bbxV_h2AR2lAp8aaTyuy52bmKNsKY8nPTHCnw'
            service = build('sheets', 'v4', credentials=creds)

            #if button==button1:  
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="recording1!B1:B100").execute()
            value= result.get('values')
            number=value
            print(number)
            for sublist in number:
                for item in sublist:
                    print(item)

            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)

            call = client.calls.create(
                                    twiml='<Response><Say>Hey, This is Dennys calling from retail investment group. I saw you are an owner of retail property. The reason i am calling is I thought you might want an updated accurate evaluation of your propety free of charge. If you could return my call at 5412139338, once again that 5412139338. Or you can also text interested.!</Say></Response>',
                                    to=item,
                                    from_='+12408984424'
                                )

            print(call.sid)

            return '204' 

        



if __name__ == '__main__':
    app.run(threaded=True, port=5000)