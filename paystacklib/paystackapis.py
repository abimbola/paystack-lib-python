
import paystacklib
from paystacklib.baseapi import BaseApi

class Transactions(BaseApi):
    def __init__(self, secret_key=None,uri='https://api.paystack.co/transaction', method=None, headers=None, params=None):
        BaseApi.__init__(self, secret_key, uri, method, headers, params)
    def rebase(self):
        self.uri = paystacklib.api_base + '/transaction'
        self.method = None
        self.params = {}

    def initialize(self, amount, email, callback_url=None, reference=None, plan=None, invoice_limit=None, metadata=None, subaccount=None, transaction_charge=None, bearer=None, channels=None):
        self.rebase()
        self.uri = self.uri + '/initialize'
        self.method = 'post'
        params = {'amount': amount, 'email': email, 'callback_url': callback_url, 'reference': reference, 'plan': plan, 'invoice_limit': invoice_limit, 'metadata': metadata, 'subaccount': subaccount, 'transaction_charge': transaction_charge, 'bearer': bearer, 'channels': channels}
        self.params = {item:params[item] for item in params.keys() if params[item] is not None}
        return self.execute()
        
    def verify(self, reference):
        self.rebase()
        self.uri = self.uri + '/verify/{0}'.format(reference)
        self.method = 'get'
        return self.execute()


    def list(self, per_page=50, page=1, customer=None, status=None, fr=None, to=None, amount=None):
        self.rebase()
        params = {'per_page': per_page, 'page': page, 'customer': customer, 'status': status, 'from': fr, 'to': to, 'amount': amount}
        self.params = {item:params[item] for item in params.keys() if params[item] is not None}
        self.method = 'get'
        return self.execute()
