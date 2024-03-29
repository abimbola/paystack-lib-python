import paystacklib
from paystacklib.base.baseapi import BaseApi
from paystacklib.util.utils import clean_params

class TransferRecipient(BaseApi):
    object_type = '/transferrecipient'
    def __init__(
            self, secret_key=None,
            uri=paystacklib.api_base + object_type, method=None, 
            headers=None, params=None):
        BaseApi.__init__(self, secret_key, uri, method, headers, params)

    @classmethod
    def create(cls, tr_type, name, account_number=None, bank_code=None,
            metadata=None, currency=None, description=None, authorization_code=None): 
        params = clean_params(locals())
        params['type'] = params['tr_type'] #type is python builtin function
        del params['tr_type'] 
        uri = paystacklib.api_base + cls.object_type
        return cls(uri=uri, method='post', params=params).execute() 

    @classmethod
    def list(cls):
        params = clean_params(locals())
        uri = paystacklib.api_base + cls.object_type 
        return cls(uri=uri, method='get', params=params).execute()

    @classmethod    
    def update(cls, recipient_code_or_id, name=None, email=None):
        params = clean_params(locals())
        uri = paystacklib.api_base + \
            '{0}/{1}'.format(cls.object_type, str(recipient_code_or_id)) 
        return cls(uri=uri, method='put', params=params).execute()

    @classmethod
    def delete(cls, recipient_code_or_id):
        uri = paystacklib.api_base + '{0}/{1}'.format(cls.object_type, str(recipient_code_or_id))
        return cls(uri=uri, method='delete').execute()

