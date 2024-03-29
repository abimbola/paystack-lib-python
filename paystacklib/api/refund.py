import paystacklib
from paystacklib.base.baseapi import BaseApi
from paystacklib.util.utils import clean_params

class Refund(BaseApi):
    object_type = '/refund'
    def __init__(
            self, secret_key=None,
            uri=paystacklib.api_base + object_type, method=None, 
            headers=None, params=None):
        BaseApi.__init__(self, secret_key, uri, method, headers, params)

    @classmethod
    def create(
            cls, transaction, amount=None, currency=None,
            customer_note=None, merchant_note=None):
        params = clean_params(locals())
        uri = paystacklib.api_base + cls.object_type
        return cls(uri=uri, method='post', params=params).execute() 


    @classmethod
    def list(
            cls, reference=None, currency=None): 
        params = clean_params(locals())
        uri = paystacklib.api_base + cls.object_type 
        return cls(uri=uri, method='get', params=params).execute()

    @classmethod
    def fetch(cls, reference):
        uri = paystacklib.api_base + \
            '{0}/{1}'.format(cls.object_type, str(reference))
        return cls(uri=uri, method='get').execute() 

