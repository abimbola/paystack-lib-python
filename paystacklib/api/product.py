import paystacklib
from paystacklib.base.baseapi import BaseApi
from paystacklib.util.utils import clean_params

class Product(BaseApi):
    object_type = '/product'
    def __init__(
            self, secret_key=None,
            uri=paystacklib.api_base + object_type, method=None, 
            headers=None, params=None):
        BaseApi.__init__(self, secret_key, uri, method, headers, params)

    @classmethod
    def create(
            cls, name, description, price, currency, limited=None,
            quantity=None):
        params = clean_params(locals())
        uri = paystacklib.api_base + cls.object_type
        return cls(uri=uri, method='post', params=params).execute() 


    @classmethod
    def list(cls):
        params = clean_params(locals())
        uri = paystacklib.api_base + cls.object_type 
        return cls(uri=uri, method='get', params=params).execute()

    @classmethod
    def fetch(cls, product_id):
        uri = paystacklib.api_base + \
            '{0}/{1}'.format(cls.object_type, str(product_id))
        return cls(uri=uri, method='get').execute() 

    @classmethod    
    def update(
            cls, product_id, name=None, description=None, price=None, currency=None,
            limited=None, quantity=None): 
        params = clean_params(locals())
        uri = paystacklib.api_base + \
            '{0}/{1}'.format(cls.object_type, str(product_id)) 
        return cls(uri=uri, method='put', params=params).execute()

