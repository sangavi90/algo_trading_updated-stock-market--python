from .imports import *


# #### it showing internal server error:


from rest_framework.views import APIView
from rest_framework.response import Response
import http.client
import json
import pyotp

# class Historical_data(APIView):
#     def __init__(self):
#         super().__init__()
#         self.order_history = []

#     def post(self, request):
#         try:
#             token = "AFH6577WNNSGC4TGXVLJWHVAQI"
#             totp = pyotp.TOTP(token).now()
#         except Exception as e:
#             return Response({"error": "Failed to generate OTP"}, status=500)

#         # Place order logic here
#         username = 'S2098754'
#         pwd = '2024'
#         smartApi = SmartConnect('4dPdQcGs')

#         data = smartApi.generateSession(username, pwd, totp)
#         jwt_token = data['data']['jwtToken']
#         conn = http.client.HTTPSConnection("apiconnect.angelbroking.com")
#         payload = {
#             "variety": "AMO",
#             "tradingsymbol": "FINNIFTY16APR2422100PE",
#             "symboltoken": "44040",
#             "transactiontype": "SELL",
#             "exchange": "NFO",
#             "ordertype": "LIMIT",
#             "producttype": "CARRYFORWARD",
#             "duration": "IOC",
#             "price": "2000.50",
#             "squareoff": "0",
#             "stoploss": "250",
#             "quantity": "40",
#             "triggerprice": "0",
#             "expirydate": "16APR2024",
#             "strikeprice": "2210000.000000"
#         }
#         headers = {
#             'Authorization': jwt_token,
#             'Content-Type': 'application/json',
#             'Accept': 'application/json',
#             'X-UserType': 'USER',
#             'X-SourceID': 'WEB',
#             'X-ClientLocalIP': '192.168.0.101',
#             'X-ClientPublicIP': '49.205.147.195',
#             'X-MACAddress': '80-38-FB-B9-EE-20',
#             'X-PrivateKey': '4dPdQcGs'
#         }
#         conn.request("POST", "/rest/secure/angelbroking/order/v1/placeOrder", json.dumps(payload), headers)
#         res = conn.getresponse()
#         order_data = json.loads(res.read().decode("utf-8"))

#         # Execute historical data retrieval and profit/loss calculation
#         historical_data_response = self.get_historical_data(order_data, request)

#         # Calculate total profit/loss across all legs
#         total_profit_loss_all_legs = sum(historical_data_response['profit_loss']['legs_profit_loss'].values())

#         response_data = {
#             "order_data": order_data,
#             "historical_data": historical_data_response['historical_data'],
#             "profit_loss": {
#                 "legs_profit_loss": historical_data_response['profit_loss']['legs_profit_loss'],
#                 "total_profit_loss_all_legs": total_profit_loss_all_legs
#             }
#         }

#         return Response(response_data)

#     def get_historical_data(self, order_data, request):
#         # Fetch live data
#         live_data = self.fetch_live_data(order_data)

#         # Extract open and close values from the place order data
#         order_open = float(order_data.get('price'))  # Assuming the price represents the open value
#         order_close = float(order_data.get('stoploss'))  # Assuming the stoploss represents the close value

#         # Load historical data from order data
#         order_legs = order_data.get('legs', [])
#         # Example data structure for demonstration
#         historical_data = {
#             "candle_data": [
#                 {"timestamp": "2021-02-08 09:00", "open": order_open, "close": order_close},
#                 {"timestamp": "2021-02-08 09:01", "open": order_close, "close": order_open},
#             ]
#         }

#         # Calculate profit/loss for each leg
#         legs_profit_loss = {}
#         for leg in order_legs:
#             leg_profit_loss = 0  # Placeholder calculation, replace with actual logic
#             legs_profit_loss[f"leg_{leg['id']}"] = leg_profit_loss

#         # Example response structure
#         response_data = {
#             "historical_data": historical_data,
#             "profit_loss": {
#                 "legs_profit_loss": legs_profit_loss
#             }
#         }

#         return response_data

#     def fetch_live_data(self, order_data):
#         try:
#             token = "AFH6577WNNSGC4TGXVLJWHVAQI"
#             totp = pyotp.TOTP(token).now()
#         except Exception as e:
#             return {"error": "Failed to generate OTP"}

#         username = 'S2098754'
#         pwd = '2024'
#         smartApi = SmartConnect('4dPdQcGs')

#         data = smartApi.generateSession(username, pwd, totp)
#         jwt_token = data['data']['jwtToken']
#         conn = http.client.HTTPSConnection("apiconnect.angelbroking.com")
#         payload = {
#             "exchange": "NSE",
#             "symboltoken": "3045",
#             "interval": "ONE_MINUTE",
#             "fromdate": "2021-02-08 09:00",
#             "todate": "2021-02-08 09:16"
#         }
#         headers = {
#             'X-PrivateKey': '4dPdQcGs',
#             'Accept': 'application/json',
#             'X-SourceID': 'WEB',
#             'X-ClientLocalIP': '192.168.0.103',
#             'X-ClientPublicIP': '49.205.144.36',
#             'X-MACAddress': '80-38-FB-B9-EE-20',
#             'X-UserType': 'USER',
#             'Authorization': jwt_token,
#             'Content-Type': 'application/json'
#         }
#         conn.request("POST", "/rest/secure/angelbroking/historical/v1/getCandleData", json.dumps(payload), headers)
#         res = conn.getresponse()
#         data = res.read()
#         return json.loads(data.decode("utf-8"))






# ############## it gives total profit and loss of each leg and also total leg
import http.client
import json
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd

class Historical_data(APIView):
    def fetch_live_data(self):
        try:
            token = "AFH6577WNNSGC4TGXVLJWHVAQI"
            totp = pyotp.TOTP(token).now()
            # print(totp)
        except Exception as e:
            logger.error("Invalid Token: The provided token is not valid.")
            raise e
        # Replace these values with your actual credentials
        username = 'S2098754'
        pwd = '2024'

        # Initialize SmartConnect with your API key
        smartApi = SmartConnect('4dPdQcGs')
        
        data = smartApi.generateSession(username, pwd, totp)
        jwt_token = data['data']['jwtToken']
        conn = http.client.HTTPSConnection("apiconnect.angelbroking.com")
        payload = "{\r\n     \"exchange\": \"NSE\",\r\n     \"symboltoken\": \"3045\",\r\n     \"interval\": \"ONE_MINUTE\",\r\n     \"fromdate\": \"2021-02-08 09:00\",\r\n     \"todate\": \"2021-02-08 09:16\"\r\n}"
        headers = {
            'X-PrivateKey': '4dPdQcGs',
            'Accept': 'application/json',
            'X-SourceID': 'WEB',
            'X-ClientLocalIP': '192.168.0.103',
            'X-ClientPublicIP': '49.205.144.36',
            'X-MACAddress': '80-38-FB-B9-EE-20',
            'X-UserType': 'USER',
            'Authorization': jwt_token ,
            'Content-Type': 'application/json'
        }
        conn.request("POST", "/rest/secure/angelbroking/historical/v1/getCandleData", payload, headers)
        res = conn.getresponse()
        data = res.read()
        return json.loads(data.decode("utf-8"))

    def calculate_profit_loss(self, row, live_data):
        # Check if 'open' key exists in live_data dictionary
        if 'open' in live_data:
            open_price = live_data['open']
        else:
            # Handle the case where 'open' key doesn't exist
            open_price = 0  # or any default value you want to use
        
        # Implement your calculation logic here based on live data
        purchase_price = row['Purchase Price']
        sale_price = row['Sale Price']
        quantity = row['Quantity']
        additional_costs = row['Additional Costs']

        # For demonstration purposes, let's use 'open' price for purchase and 'close' price for sale
        total_cost = purchase_price * quantity + additional_costs
        total_revenue = sale_price * quantity
        profit_loss = total_revenue - total_cost

        return profit_loss

    def get(self, request):
        # Fetch live data using the Angel Broking API
        live_data = self.fetch_live_data()

        # Example symbol
        symbol = 'AAPL'

        # Load historical data from CSV file or any other source
        # For demonstration purposes, let's create a DataFrame with mock data
        data = {
            'Leg ID': [1, 1, 2, 2],  # Example leg IDs
            'Type': ['Buy', 'Sell', 'Buy', 'Sell'],  # Example transaction types
            'Purchase Price': [live_data.get('open', 0), None, live_data.get('open', 0), None],  # Example purchase prices
            'Sale Price': [None, live_data.get('close', 0), None, live_data.get('close', 0)],  # Example sale prices
            'Quantity': [10, 10, 15, 15],  # Example quantities
            'Additional Costs': [10, 5, 15, 10]  # Example additional costs
        }

        historical_data = pd.DataFrame(data)

        # Apply the function to each row in the historical data to calculate profit/loss for each leg
        historical_data['Profit/Loss'] = historical_data.apply(
            lambda row: self.calculate_profit_loss(row, live_data), axis=1
        )

        # Separate buy and sell transactions
        buy_transactions = historical_data[historical_data['Type'] == 'Buy']
        sell_transactions = historical_data[historical_data['Type'] == 'Sell']

        # Calculate buy price profit and loss for each leg
        buy_profit_loss = buy_transactions.groupby('Leg ID')['Profit/Loss'].sum()

        # Calculate sell price profit and loss for each leg
        sell_profit_loss = sell_transactions.groupby('Leg ID')['Profit/Loss'].sum()

        # Combine buy and sell profit and loss for each leg
        total_profit_loss_legs = buy_profit_loss.add(sell_profit_loss, fill_value=0)

        # Calculate total profit and loss across all legs
        total_profit_loss_all_legs = total_profit_loss_legs.sum()

        # Display total profit and loss for each leg and across all legs
        return Response({
            "Total Profit/Loss for Each Leg": total_profit_loss_legs.to_dict(),
            "Total Profit/Loss Across All Legs": total_profit_loss_all_legs
        })








# ########### it gives order_data,historical data , profit and loss of each leg and also total leg:
from rest_framework.views import APIView
from rest_framework.response import Response
import pyotp
import http.client
import json
import pandas as pd

# class Historical_data(APIView):
#     def __init__(self):
#         super().__init__()
#         self.order_history = []

#     def post(self, request):
#         try:
#             token = "AFH6577WNNSGC4TGXVLJWHVAQI"
#             totp = pyotp.TOTP(token).now()
#         except Exception as e:
#             return Response({"error": "Failed to generate OTP"}, status=500)

#         # Place order logic here
#         username = 'S2098754'
#         pwd = '2024'
#         smartApi = SmartConnect('4dPdQcGs')

#         data = smartApi.generateSession(username, pwd, totp)
#         jwt_token = data['data']['jwtToken']
#         conn = http.client.HTTPSConnection("apiconnect.angelbroking.com")
#         payload = {
#             "variety": "AMO",
#             "tradingsymbol": "FINNIFTY16APR2422100PE",
#             "symboltoken": "44040",
#             "transactiontype": "SELL",
#             "exchange": "NFO",
#             "ordertype": "LIMIT",
#             "producttype": "CARRYFORWARD",
#             "duration": "IOC",
#             "price": "2000.50",
#             "squareoff": "0",
#             "stoploss": "250",
#             "quantity": "40",

#             "triggerprice": "0",
#             "expirydate": "16APR2024",
#             "strikeprice": "2210000.000000"
#         }
#         headers = {
#             'Authorization': jwt_token,
#             'Content-Type': 'application/json',
#             'Accept': 'application/json',
#             'X-UserType': 'USER',
#             'X-SourceID': 'WEB',
#             'X-ClientLocalIP': '192.168.0.101',
#             'X-ClientPublicIP': '49.205.147.195',
#             'X-MACAddress': '80-38-FB-B9-EE-20',
#             'X-PrivateKey': '4dPdQcGs'
#         }
#         conn.request("POST", "/rest/secure/angelbroking/order/v1/placeOrder", json.dumps(payload), headers)
#         res = conn.getresponse()
#         order_data = json.loads(res.read().decode("utf-8"))

#         # Execute historical data retrieval and profit/loss calculation
#         historical_data_response = self.get_historical_data(order_data, request)

#         # Calculate total profit/loss across all legs
#         total_profit_loss_all_legs = sum(historical_data_response['profit_loss']['legs_profit_loss'].values())

#         response_data = {
#             "order_data": order_data,
#             "historical_data": historical_data_response['historical_data'],
#             "profit_loss": {
            
#                 "legs_profit_loss": historical_data_response['profit_loss']['legs_profit_loss'],
#                 "total_profit_loss_all_legs": total_profit_loss_all_legs
#             }
#         }

#         return Response(response_data)

#     def get_historical_data(self, order_data, request):
#         # Fetch live data
#         live_data = self.fetch_live_data(order_data)

#         # Load historical data from order data
#         order_legs = order_data.get('legs', [])
#         # Example data structure for demonstration
#         historical_data = {
#             "candle_data": [
#                 {"timestamp": "2021-02-08 09:00", "open": 100, "close": 110},
#                 {"timestamp": "2021-02-08 09:01", "open": 110, "close": 115},
#             ]
#         }

#         # Calculate profit/loss for each leg
#         legs_profit_loss = {}
#         for leg in order_legs:
#             leg_profit_loss = 0  # Placeholder calculation, replace with actual logic
#             legs_profit_loss[f"leg_{leg['id']}"] = leg_profit_loss

#         # Example response structure
#         response_data = {
#             "historical_data": historical_data,
#             "profit_loss": {
#                 "legs_profit_loss": legs_profit_loss
#             }
#         }

#         return response_data

#     def fetch_live_data(self, order_data):
#         try:
#             token = "AFH6577WNNSGC4TGXVLJWHVAQI"
#             totp = pyotp.TOTP(token).now()
#         except Exception as e:
#             return {"error": "Failed to generate OTP"}

#         username = 'S2098754'
#         pwd = '2024'
#         smartApi = SmartConnect('4dPdQcGs')

#         data = smartApi.generateSession(username, pwd, totp)
#         jwt_token = data['data']['jwtToken']
#         conn = http.client.HTTPSConnection("apiconnect.angelbroking.com")
#         payload = {
#             "exchange": "NSE",
#             "symboltoken": "3045",
#             "interval": "ONE_MINUTE",
#             "fromdate": "2021-02-08 09:00",
#             "todate": "2021-02-08 09:16"
#         }
#         headers = {
#             'X-PrivateKey': '4dPdQcGs',
#             'Accept': 'application/json',
#             'X-SourceID': 'WEB',
#             'X-ClientLocalIP': '192.168.0.103',
#             'X-ClientPublicIP': '49.205.144.36',
#             'X-MACAddress': '80-38-FB-B9-EE-20',
#             'X-UserType': 'USER',
#             'Authorization': jwt_token,
#             'Content-Type': 'application/json'
#         }
#         conn.request("POST", "/rest/secure/angelbroking/historical/v1/getCandleData", json.dumps(payload), headers)
#         res = conn.getresponse()
#         data = res.read()
#         return json.loads(data.decode("utf-8"))

