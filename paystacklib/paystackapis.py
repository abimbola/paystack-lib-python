
import paystacklib
from paystacklib.baseapi import BaseApi
from paystacklib.utils import clean_params

class Transactions(BaseApi):
    def __init__(self, secret_key=None,uri='https://api.paystack.co/transaction', method=None, headers=None, params=None):
        BaseApi.__init__(self, secret_key, uri, method, headers, params)
    def rebase(self):
        self.uri = paystacklib.api_base + '/transaction'
        self.method = None
        self.params = {}

    def initialize(self, amount, email, callback_url=None, reference=None, plan=None, invoice_limit=None, metadata=None, subaccount=None, transaction_charge=None, bearer=None, channels=None):
        self.rebase()
        self.params = locals()
        self.params = clean_params(self.params)
        self.uri = self.uri + '/initialize'
        self.method = 'post'
        return self.execute()
        
    def verify(self, reference):
        self.rebase()
        self.uri = self.uri + '/verify/{0}'.format(reference)
        self.method = 'get'
        return self.execute()


    def list(self, per_page=50, page=1, customer=None, status=None, fr=None, to=None, amount=None):
        self.rebase()
        self.params = locals()
        self.params['from'] = self.params['fr']
        del self.params['fr']
        self.params = clean_params(self.params)
        self.method = 'get'
        return self.execute()

    def fetch(self, transaction_id):
        self.rebase()
        self.uri = self.uri + '/{0}'.format(str(transaction_id))
        self.method = 'get'
        return self.execute()
    
    def charge(self, authorization_code, amount, email, reference=None, plan=None, currency=None, metadata=None, subaccount=None, transaction_charge=None, bearer=None, invoice_limit=None, queue=None):
        self.rebase()
        self.params = locals()
        self.params = clean_params(self.params)
        self.uri = self.uri + '/charge_authorization'
        self.method = 'post'
        return self.execute()

    def timeline(self, transaction_id):
        self.rebase()
        self.uri = self.uri + '/timeline/{0}'.format(str(transaction_id))
        self.method = 'get'
        return self.execute()

    def totals(self, fr=None, to=None):
        self.rebase()
        self.params = locals()
        self.params['from'] = self.params['fr']
        del self.params['fr']
        self.params = clean_params(self.params)
        self.uri = self.uri + '/totals'
        self.method = 'get'
        return self.execute()

    def export(self, fr=None, to=None, settled=None, payment_page=None, customer=None, currency=None, settlement=None, amount=None, status=None):
        self.rebase()
        self.params = locals()
        self.params['from'] = self.params['fr']
        del self.params['fr']
        self.params = clean_params(self.params)
        self.uri = self.uri +'/export'
        self.method = 'get'
        return self.execute() 
