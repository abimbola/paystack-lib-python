import paystacklib
from paystacklib.base.baseapi import BaseApi
from paystacklib.util.utils import clean_params

class PaymentSessionTimeout(BaseApi):
    object_type = '/payment_session_timeout'
    def __init__(
            self, secret_key=None,
            uri=paystacklib.api_base + object_type, method=None, 
            headers=None, params=None):
        BaseApi.__init__(self, secret_key, uri, method, headers, params)


    @classmethod
    def fetch(cls):
        uri = paystacklib.api_base + \
            '/integration{0}'.format(cls.object_type)
        return cls(uri=uri, method='get').execute()

    @classmethod    
    def update(cls, timeout):
        params = clean_params(locals())
        uri = paystacklib.api_base + \
            '/integration{0}'.format(cls.object_type)
        return cls(uri=uri, method='put', params=params).execute()


