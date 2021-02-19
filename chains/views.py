
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import os

from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

from api.blockchain import substrate
from api.helpers import get_now
 
from chains.helpers.exchange import (
    get_all_pairs, get_a_pair, get_orderbook_for_a_pair, get_trades_for_a_pair,
    get_all_matched_order, get_a_matched_order,    
    create_buy_order, update_buy_order, cancel_buy_order, get_all_buy_order, get_a_buy_order,
    create_sell_order,update_sell_order, cancel_sell_order, get_all_sell_order, get_a_sell_order
)

from chains.helpers.token import (
    get_account_balance,
    get_a_token,
    get_all_token,
    transfer_token,
    get_total_supply,
    get_paused_status,
    get_banker
)


class ExchangeOrderViews(APIView):

    def get(self, request, format=None):

        response_ = {}
        response_['timestamp'] = get_now()

        ticker = request.GET.get('ticker', '')
        order_type = request.GET.get('orderType', '')
        
        if order_type == 'buy':
            order_id = request.GET.get('orderId', '')
            if order_id:
                response_['data'] = get_a_buy_order(ticker, order_id)
            else:
                response_['data'] = get_all_buy_order(ticker)
        elif order_type == 'sell':
            order_id = request.GET.get('orderId', '')
            if order_id:
                response_['data'] = get_a_sell_order(ticker, order_id)
            else:
                response_['data'] = get_all_sell_order(ticker)
        else:
            matched_id = request.GET.get('matchedId', '')
            if matched_id:
                response_['data'] = get_a_matched_order(ticker, matched_id)
            else:
                response_['data'] = get_all_matched_order(ticker)

        return JsonResponse(response_)

    def post(self, request, format=None):

        response_ = {}
        response_['timestamp'] = get_now()

        ticker = request.GET.get('ticker', '')
        order_type = request.GET.get('orderType', '')

        _data = request.data 

        if order_type == 'buy':
            response_['data'] = create_buy_order(ticker, _data)
        else:
            response_['data'] = create_sell_order(ticker, _data)        

        return JsonResponse(response_)  

    def put(self, request, format=None):

        response_ = {}
        response_['timestamp'] = get_now()

        ticker = request.GET.get('ticker', '')
        order_type = request.GET.get('orderType', '')
        order_id = request.GET.get('orderId', '')

        _data = request.data 

        if order_type == 'buy':
            response_['data'] = update_buy_order(ticker, order_id, _data)
        else:
            response_['data'] = update_sell_order(ticker, order_id, _data)

        return JsonResponse(response_)  

    def delete(self, request, format=None):

        response_ = {}
        response_['timestamp'] = get_now()

        ticker = request.GET.get('ticker', '')
        order_type = request.GET.get('orderType', '')
        order_id = request.GET.get('orderId', '')

        _data = request.data 

        if order_type == 'buy':
            response_['data'] = cancel_buy_order(ticker, order_id, _data)
        else:
            response_['data'] = cancel_sell_order(ticker, order_id, _data)        

        return JsonResponse(response_)                          


class ExchangePairViews(APIView):

    def get(self, request, format=None):

        response_ = {}
        response_['timestamp'] = get_now()

        ticker = request.GET.get('ticker', '')
        if ticker:
            detail = request.GET.get('detail', '')
            if detail == 'orderbook':
                depth = request.GET.get('depth', '')
                response_['data'] = get_orderbook_for_a_pair(ticker, detail, depth)
            elif detail == 'historical':
                limit = request.GET.get('limit', '')
                start_time = request.GET.get('startTime', '')
                end_time = request.GET.get('endTime', '')
                response_['data'] = get_trades_for_a_pair(ticker, detail, limit, start_time, end_time)
            else:
                response_['data'] = get_a_pair(ticker)
        else:
            response_['data'] = get_all_pairs()

        return JsonResponse(response_)
      

class TokenViews(APIView):

    def get(self, request, format=None):
        response_ = {}
        response_['timestamp'] = get_now()
        token = request.GET.get('tokenId', '')

        if token:
            task = request.GET.get('task', '')
            account_id = request.GET.get('accountId', '')
            if task == 'balance':
                response_['data'] = get_account_balance(token, account_id)
            elif task == 'supply':
                response_['data'] = get_total_supply(token)    
            elif task == 'paused':
                response_['data'] = get_paused_status(token)   
            elif task == 'banker':
                response_['data'] = get_banker(token)                                           
            else:
                response_['data'] = get_a_token(token)
        else:
            response_['data'] = get_all_token()

        return JsonResponse(response_)

    def post(self, request, format=None):
        response_ = {}
        response_['timestamp'] = get_now()
        _data = request.data 

        token = request.GET.get('tokenId', '')
        task = request.GET.get('task', '')

        if task == 'transfer':
            account_from = request.GET.get('from', '')
            account_to = request.GET.get('to', '')
            amount = request.GET.get('amount', '')
            response_['data'] = transfer_token(token, account_from, account_to, amount, _data)
 
        return JsonResponse(response_)        
