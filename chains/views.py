
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser

import os

from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

from api.blockchain import connect
from api.helpers import get_now
 
from chains.helpers.exchange import (
    get_all_pairs, get_a_pair, get_orderbook_for_a_pair, get_trades_for_a_pair, 
    create_buy_order, cancel_buy_order, get_all_buy_order,
    create_sell_order, cancel_sell_order, get_all_sell_order
)

from chains.helpers.referral import (
    find_account_by_code,
    find_code_by_account,
    check_code_set,
    check_number_of_references,
    check_registration,
    register_from_code,
    set_promoter_code      
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

from chains.helpers.wallet import (
    generate_wallet,
    check_wallet_balance,
    verify_phone,
    verify_phone_code,
    upload_evidence
)

from chains.helpers.bazaar import (
    get_bazaar_trader_id,
    get_bazaar_trader_detail,
    get_bazaar_trader_count,
    get_bazaar_trade,
    get_bazaar_trade_count,
    get_bazaar_completed_trade_count,
    get_bazaar_completed_trade_by_trader,
    get_bazaar_trade_initiated_count,
    get_bazaar_trade_initiated,
    get_bazaar_trade_initiated_by_trader,
    get_bazaar_trade_escrowed_count,
    get_bazaar_trade_escrowed,
    get_bazaar_trade_escrowed_by_trader,
    get_bazaar_trade_money_in_count,
    get_bazaar_trade_money_in,
    get_bazaar_trade_money_in_by_trader,
    get_bazaar_trade_money_in_confirmed_count,
    get_bazaar_trade_money_in_confirmed,
    get_bazaar_trade_money_in_confirmed_by_trader,
    bazaar_initiate_buy,
    bazaar_escrow_coin,
    bazaar_cancel_escrow,
    bazaar_transfer_money,
    bazaar_receive_money,
    bazaar_complete,
    bazaar_register_trader,
    bazaar_update_trader
)

from chains.helpers.bridge import (
    get_watchers,
    get_ether_issue,
    get_ether_issue_by_user,
    get_ether_issue_count,
    get_ether_unminted_issues,
    get_ether_redemption,
    get_ether_redemption_by_user,
    get_ether_redemption_count,
    get_ether_unburnt_redemptions,
    add_watcher,
    remove_watcher,
    create_issue,
    execute_issue,
    create_redemption,
    update_issue,
    update_redemption,          
    cancel_issue,
    cancel_redemption             
)


class ExchangeOrderViews(APIView):

    def get(self, request, format=None):

        response_ = {}
        response_['timestamp'] = get_now()

        ticker = request.GET.get('tickerId', '')
        order_type = request.GET.get('orderType', '')
        native = request.GET.get('native', '')
        
        if order_type == 'buy':
            if native:
                response_['data'] = get_all_buy_order(ticker, native=True)
            else:
                response_['data'] = get_all_buy_order(ticker)
        else:
            if native:
                response_['data'] = get_all_sell_order(ticker, native=True)
            else:
                response_['data'] = get_all_sell_order(ticker)

        return JsonResponse(response_)

    def post(self, request, format=None):

        response_ = {}
        response_['timestamp'] = get_now()

        ticker = request.GET.get('tickerId', '')
        order_type = request.GET.get('orderType', '')
        native = request.GET.get('native', '')

        _data = request.data 

        if order_type == 'buy':
            if native:
                response_['data'] = create_buy_order(ticker, _data, native=True)
            else:
                response_['data'] = create_buy_order(ticker, _data)
        else:
            if native:
                response_['data'] = create_sell_order(ticker, _data, native=True)        
            else:
                response_['data'] = create_sell_order(ticker, _data)        

        return JsonResponse(response_)  

    def delete(self, request, format=None):

        response_ = {}
        response_['timestamp'] = get_now()

        ticker = request.GET.get('tickerId', '')
        order_type = request.GET.get('orderType', '')
        order_id = request.GET.get('orderId', '')
        native = request.GET.get('native', '')
        _data = request.data 

        if order_type == 'buy':
            if native:
                response_['data'] = cancel_buy_order(ticker, order_id, _data, native=True)
            else:
                response_['data'] = cancel_buy_order(ticker, order_id, _data)
        else:
            if native:
                response_['data'] = cancel_sell_order(ticker, order_id, _data, native=True)        
            else:
                response_['data'] = cancel_sell_order(ticker, order_id, _data)        

        return JsonResponse(response_)                          


class ExchangePairViews(APIView):

    def get(self, request, format=None):

        response_ = {}
        response_['timestamp'] = get_now()

        ticker_id = request.GET.get('tickerId', '')
        native = request.GET.get('native', '')
        if ticker_id:
            detail = request.GET.get('detail', '')
            if detail == 'orderbook':
                depth = request.GET.get('depth', '')
                if native:
                    response_['data'] = get_orderbook_for_a_pair(ticker_id, detail, depth, native)
                else:
                    response_['data'] = get_orderbook_for_a_pair(ticker_id, detail, depth)
            elif detail == 'historical':
                limit = request.GET.get('limit', '')
                start_time = request.GET.get('startTime', '')
                end_time = request.GET.get('endTime', '')
                if native:
                    response_['data'] = get_trades_for_a_pair(ticker_id, detail, limit, start_time, end_time, native)
                else:
                    response_['data'] = get_trades_for_a_pair(ticker_id, detail, limit, start_time, end_time)
            else:
                if native:
                    response_['data'] = get_a_pair(ticker_id, native)
                else:
                    response_['data'] = get_a_pair(ticker_id)
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
            response_['data'] = transfer_token(token, _data)
 
        return JsonResponse(response_)       

class WalletViews(APIView):

    parser_classes = [FileUploadParser]

    def get(self, request, format=None):
        response_ = {}
        response_['timestamp'] = get_now()
        task = request.GET.get('task', '')

        if task == 'generateWallet':
            response_['data'] = generate_wallet()
        elif task == 'checkBalance':
            account_id = request.GET.get('accountId', '')
            checker_id = request.GET.get('checkerId', '')
            response_['data'] = check_wallet_balance(account_id, checker_id)

        return JsonResponse(response_)

    def post(self, request, format=None):
        response_ = {}
        response_['timestamp'] = get_now()
        _data = request.data 

        task = request.GET.get('task', '')

        if task == 'verifyPhone':     
            phone = request.GET.get('phone', '')       
            response_['data'] = verify_phone(phone, _data)
        elif task == 'verifyPhoneCode':            
            code = request.GET.get('code', '')
            phone = request.GET.get('phone', '')
            response_['data'] = verify_phone_code(phone, code, _data)        
 
        return JsonResponse(response_)    

    def put(self, request, format=None):
        response_ = {}
        file_object = request.data['file']
        task = request.GET.get('task', '')
        account_id = request.GET.get('accountId', '')
        evidence = request.GET.get('evidence', '')

        if task == 'uploadEvidence':
            response_['data'] = upload_evidence(file_object, account_id, evidence)

        return JsonResponse(response_)                     


class ReferralViews(APIView):

    def get(self, request, format=None):
        response_ = {}
        response_['timestamp'] = get_now()

        task = request.GET.get('task', '')

        if task == 'accountByCode':     
            code = request.GET.get('code', '')       
            response_['data'] = find_account_by_code(code)
        elif task == 'codeByAccount':            
            account_id = request.GET.get('accountId', '')
            response_['data'] = find_code_by_account(account_id)       
        elif task == 'codeSet':            
            account_id = request.GET.get('accountId', '')
            response_['data'] = check_code_set(account_id)   
        elif task == 'numberOfReferences':            
            account_id = request.GET.get('accountId', '')
            response_['data'] = check_number_of_references(account_id)   
        elif task == 'checkRegistration':            
            account_id = request.GET.get('accountId', '')
            response_['data'] = check_registration(account_id)                                          
 
        return JsonResponse(response_)    

    def post(self, request, format=None):
        response_ = {}
        response_['timestamp'] = get_now()
        _data = request.data 

        task = request.GET.get('task', '')
        code = request.GET.get('code', '')

        if task == 'register':         
            response_['data'] = register_from_code(code, _data)
        elif task == 'setCode':            
            response_['data'] = set_promoter_code(code, _data)        
 
        return JsonResponse(response_)    


class BazaarViews(APIView):

    def get(self, request, format=None):
        response_ = {}
        response_['timestamp'] = get_now()

        task = request.GET.get('task', '')   

        if task == 'bazaarTraderId':
            account_id = request.GET.get('accountId', '')   
            response_['data'] = get_bazaar_trader_id(account_id)
        elif task == 'bazaarTraderDetail':
            trader_id = request.GET.get('traderId', '')  
            response_['data'] = get_bazaar_trader_detail(trader_id)
        elif task == 'bazaarTraderCount':
            response_['data'] = get_bazaar_trader_count()

        elif task == 'bazaarTrade':
            trade_id = request.GET.get('tradeId', '')  
            response_['data'] = get_bazaar_trade(trade_id)
        elif task == 'bazaarTradeCount':
            response_['data'] = get_bazaar_trade_count()

        elif task == 'bazaarCompletedTradeCount':
            response_['data'] = get_bazaar_completed_trade_count()
        elif task == 'bazaarCompletedTradeByTrader':
            trader_id = request.GET.get('traderId', '') 
            response_['data'] = get_bazaar_completed_trade_by_trader(trader_id)

        elif task == 'bazaarTradeInitiatedCount':
            response_['data'] = get_bazaar_trade_initiated_count()
        elif task == 'bazaarTradeInitiated':
            account_id = request.GET.get('accountId', '')   
            response_['data'] = get_bazaar_trade_initiated(account_id)
        elif task == 'bazaarTradeInitiatedByTrader':
            trader_id = request.GET.get('traderId', '') 
            response_['data'] = get_bazaar_trade_initiated_by_trader(trader_id)

        elif task == 'bazaarTradeEscrowedCount':
            response_['data'] = get_bazaar_trade_escrowed_count()
        elif task == 'bazaarTradeEscrowed':
            account_id = request.GET.get('accountId', '')   
            response_['data'] = get_bazaar_trade_escrowed(account_id)
        elif task == 'bazaarTradeEscrowedByTrader':
            trader_id = request.GET.get('traderId', '') 
            response_['data'] = get_bazaar_trade_escrowed_by_trader(trader_id)

        elif task == 'bazaarTradeMoneyInCount':
            response_['data'] = get_bazaar_trade_money_in_count()
        elif task == 'bazaarTradeMoneyIn':
            account_id = request.GET.get('accountId', '')   
            response_['data'] = get_bazaar_trade_money_in(account_id)
        elif task == 'bazaarTradeMoneyInByTrader':
            trader_id = request.GET.get('traderId', '') 
            response_['data'] = get_bazaar_trade_money_in_by_trader(trader_id)

        elif task == 'bazaarTradeMoneyInConfirmedCount':
            response_['data'] = get_bazaar_trade_money_in_confirmed_count()
        elif task == 'bazaarTradeMoneyInConfirmed':
            account_id = request.GET.get('accountId', '')   
            response_['data'] = get_bazaar_trade_money_in_confirmed(account_id)
        elif task == 'bazaarTradeMoneyInConfirmedByTrader':
            trader_id = request.GET.get('traderId', '') 
            response_['data'] = get_bazaar_trade_money_in_confirmed_by_trader(trader_id)

        return JsonResponse(response_)  

    def post(self, request, format=None):
        response_ = {}
        response_['timestamp'] = get_now()
        _data = request.data    

        task = request.GET.get('task', '')        
        if task == 'initiateBuy':
            response_['data'] = bazaar_initiate_buy(_data)
        elif task == 'escrowCoin':
            response_['data'] = bazaar_escrow_coin(_data)
        elif task == 'transferMoney':
            response_['data'] = bazaar_transfer_money(_data)
        elif task == 'receiveMoney':
            response_['data'] = bazaar_receive_money(_data)
        elif task == 'complete':
            response_['data'] = bazaar_complete(_data)
        elif task == 'registerTrader':
            response_['data'] = bazaar_register_trader(_data)

        return JsonResponse(response_) 

    def put(self, request, format=None):
        response_ = {}
        response_['timestamp'] = get_now()
        _data = request.data    

        task = request.GET.get('task', '')
        if task == 'updateTrader':
            response_['data'] = bazaar_update_trader(_data) 

        return JsonResponse(response_)      

    def delete(self, request, format=None):
        response_ = {}
        response_['timestamp'] = get_now()
        _data = request.data    

        task = request.GET.get('task', '')
        if task == 'cancelEscrow':
            response_['data'] = bazaar_cancel_escrow(_data)

        return JsonResponse(response_)                                    

class BridgeViews(APIView):

    def get(self, request, format=None):
        response_ = {}
        response_['timestamp'] = get_now()

        task = request.GET.get('task', '')         
        if task == 'watchers':
            response_['data'] = get_watchers()
        elif task == 'issue':
            issue_id = request.GET.get('issueId', '')    
            response_['data'] = get_ether_issue(issue_id)
        elif task == 'issueByUser':
            account_id = request.GET.get('accountId', '')   
            response_['data'] = get_ether_issue_by_user(account_id)
        elif task == 'issueCount':
            response_['data'] = get_ether_issue_count()
        elif task == 'unmintedIssues':
            response_['data'] = get_ether_unminted_issues()
        elif task == 'redemption':
            redemption_id = request.GET.get('redemptionId', '')  
            response_['data'] = get_ether_redemption(redemption_id)
        elif task == 'redemptionByUser':
            account_id = request.GET.get('accountId', '')   
            response_['data'] = get_ether_redemption_by_user(account_id)
        elif task == 'redemptionCount':
            response_['data'] = get_ether_redemption_count()
        elif task == 'unburntRedemptions':
            response_['data'] = get_ether_unburnt_redemptions()
        return JsonResponse(response_) 

    def post(self, request, format=None):
        response_ = {}
        response_['timestamp'] = get_now()
        _data = request.data    

        task = request.GET.get('task', '')         
        if task == 'addWatcher':
            response_['data'] = add_watcher(_data)
        elif task == 'createIssue':
            response_['data'] = create_issue(_data)
        elif task == 'executeIssue':
            response_['data'] = execute_issue(_data)
        elif task == 'createRedemption':
            response_['data'] = create_redemption(_data)
        return JsonResponse(response_)   
        
    def put(self, request, format=None):
        response_ = {}
        response_['timestamp'] = get_now()
        _data = request.data  

        if task == 'updateIssue':
            response_['data'] = update_issue(_data)
        elif task == 'updateRedemption':
            response_['data'] = update_redemption(_data)          

        return JsonResponse(response_)

    def delete(self, request, format=None):
        response_ = {}
        response_['timestamp'] = get_now()
        _data = request.data  

        if task == 'cancelIssue':
            response_['data'] = cancel_issue(_data)
        elif task == 'cancelRedemption':
            response_['data'] = cancel_redemption(_data) 
        elif task == 'removeWatcher':
            response_['data'] = remove_watcher(_data)                     

        return JsonResponse(response_)        
                  