
import paystacklib
from paystacklib.baseapi import BaseApi
from paystacklib.utils import clean_params

class Transaction(BaseApi):
    def __init__(
            self, secret_key=None,
            uri='https://api.paystack.co/transaction', method=None, 
            headers=None, params=None):
        BaseApi.__init__(self, secret_key, uri, method, headers, params)

    @classmethod
    def initialize(
            cls, amount, email, 
            callback_url=None, reference=None, plan=None, 
            invoice_limit=None, metadata=None, subaccount=None, 
            transaction_charge=None, bearer=None, channels=None):
        params = locals()
        params = clean_params(params)
        uri = paystacklib.api_base + '/transaction/initialize'
        return cls(uri=uri, method='post', params=params).execute() 

    @classmethod    
    def verify(cls, reference):
        uri = paystacklib.api_base + '/transaction/verify/{0}'.format(reference)
        return cls(uri=uri, method = 'get').execute()

    @classmethod
    def list(
            cls, per_page=50, page=1, 
            customer=None, status=None, fr=None, 
            to=None, amount=None):
        params = locals()
        params['from'] = params['fr']
        del params['fr']
        params = clean_params(params)
        return cls(method='get', params=params).execute()

    @classmethod
    def fetch(cls, transaction_id):
        uri = paystacklib.api_base + '/transaction/{0}'.format(str(transaction_id))
        return cls(uri=uri, method='get').execute() 

    @classmethod    
    def charge(
            cls, authorization_code, amount, 
            email, reference=None, plan=None, 
            currency=None, metadata=None, subaccount=None, 
            transaction_charge=None, bearer=None, invoice_limit=None, 
            queue=None):
        params = locals()
        params = clean_params(params)
        uri = paystacklib.api_base + '/transaction/charge_authorization'
        return cls(uri=uri, method='post', params=params).execute()

    @classmethod
    def timeline(cls, transaction_id):
        uri = paystacklib.api_base + '/transaction/timeline/{0}'.format(str(transaction_id))
        return cls(uri=uri, method='get').execute()

    @classmethod
    def totals(cls, fr=None, to=None):
        params = locals()
        params['from'] = params['fr']
        del params['fr']
        params = clean_params(params)
        uri = paystacklib.api_base + '/transaction/totals'
        return cls(uri=uri, method='get', params=params).execute()

    @classmethod
    def export(
            cls, fr=None, to=None, 
            settled=None, payment_page=None, customer=None, 
            currency=None, settlement=None, amount=None, status=None):
        params = locals()
        params['from'] = params['fr']
        del params['fr']
        params = clean_params(params)
        uri = paystacklib.api_base +'/transaction/export'
        return cls(uri=uri, method='get', params=params).execute()

    @classmethod
    def request_reauthorization(
            cls, authorization_code, amount, email, reference=None, metadata=None):
        params = locals()
        params = clean_params(params)
        uri = paystacklib.api_base + '/transaction/request_reauthorization'
        return cls(uri=uri, method='post', params=params).execute()

    @classmethod
    def check_authorization(cls, authorization_code, amount, email, currency=None):
        params = locals()
        params = clean_params(params)
        uri = paystacklib.api_base + '/transaction/check_authorization'
        return cls(uri=uri, method='post', params=params).execute() 
