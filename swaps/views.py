
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import os
import json


from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException
from api.blockchain import substrate
from api.helpers import get_now
 

class PairViews(APIView):

    def get(self, request, format=None): 

        response_ = {}
        response_['timestamp'] = get_now()

        ticker = request.GET.get('ticker', '')
        detail = request.GET.get('detail', '')

        if ticker:
            response_['ticker'] = ticker
            if detail == 'orderbook':
                depth = request.GET.get('depth', '')
                
                response_['detail'] = 'orderbook'
                response_['data'] = get_pair_orderbook(ticker, depth)

            elif detail == 'historical':
                _type = request.GET.get('type', '')
                limit = request.GET.get('limit', '')
                start_time = request.GET.get('start_time', '')
                end_time = request.GET.get('end_time', '')
                
                response_['detail'] = 'historical'
                response_['data'] = get_pair_historical(ticker, _type, limit, start_time, end_time)

            else:
                response_['detail'] = 'detail'
                response_['data'] = get_pair_detail(ticker)
        else:
            response_['pairs'] = get_all_pairs()
        
        return JsonResponse(response_)


def get_all_pairs():
    all_pairs = []

    # result = substrate.query(
    #     module='Swap',
    #     storage_function='ListAll',
    #     params=[]
    # )

    
    return all_pairs

def get_pair_detail(pair_id):
    pair_detail = {}

    # result = substrate.query(
    #     module='Swap',
    #     storage_function='TickerDetail',
    #     params=[pair_id]
    # )

    return pair_detail

def get_pair_orderbook(pair_id, depth):
    pair_orderbook = {}

    if depth:
        depth_ = depth
    else:
        depth_ = 0

    # result = substrate.query(
    #     module='Swap',
    #     storage_function='TickerOrder',
    #     params=[pair_id, depth_]
    # )

    return pair_orderbook

def get_pair_historical(pair_id, _type, limit, start_time, end_time):
    pair_historical = {}

    # result = substrate.query(
    #     module='Swap',
    #     storage_function='TickerHistorical',
    #     params=[pair_id, _type, limit, start_time, end_time]
    # )    

    return pair_historical    