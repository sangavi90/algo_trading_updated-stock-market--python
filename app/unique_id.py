from . imports import *
import http.client
import pyotp
import json
from rest_framework.views import APIView
from rest_framework.response import Response

class UniqueOrderid(APIView):
    def post(self, request):
        try:
            token = "AFH6577WNNSGC4TGXVLJWHVAQI"
            totp = pyotp.TOTP(token).now()
            # print(totp)
        except Exception as e:
            logger.error("Invalid Token: The provided token is not valid.")
            raise e

        # correlation_id = "abcde"
        data = smartApi.generateSession(username, pwd, totp)
        jwt_token = data['data']['jwtToken'] 

        conn = http.client.HTTPSConnection("apiconnect.angelbroking.com")

        payload = ''
        headers = {
            'Authorization': jwt_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-UserType': 'USER',
            'X-SourceID': 'WEB',
            'X-ClientLocalIP': '192.168.0.102',
            'X-ClientPublicIP': '49.205.151.46',
            'X-MACAddress': '80-38-FB-B9-EE-20',
            'X-PrivateKey': '4dPdQcGs'
        }

        response_data = []
        try:
            # Extract orders from the request data
            orders = request.data.get("orders", [])
           
            for order in orders:
                # Place the order using the payload
                conn.request("POST", "/rest/secure/angelbroking/order/v1/placeOrder", json.dumps(order), headers)
                res = conn.getresponse()
                data = res.read().decode("utf-8")
                order_response = json.loads(data)
                response_data.append(order_response)
        except Exception as e:
            # Handle exceptions
            return Response({"error": str(e)}, status=500)

        # Extract unique order IDs from the response and return them
        unique_order_ids = [order_response.get("data", {}).get("uniqueorderid") for order_response in response_data]
        return Response({"unique_order_ids": unique_order_ids})
