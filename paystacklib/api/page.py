import paystacklib
from paystacklib.base.baseapi import BaseApi
from paystacklib.util.utils import clean_params

class Page(BaseApi):
    object_type = '/page'
    def __init__(
            self, secret_key=None,
            uri=paystacklib.api_base + object_type, method=None, 
            headers=None, params=None):
        BaseApi.__init__(self, secret_key, uri, method, headers, params)

    @classmethod
    def create(
            cls, name, description=None, amount= None, slug=None,
            metadata=None, redirect_url=None, custom_fields=None): 
        params = clean_params(locals())
        uri = paystacklib.api_base + cls.object_type
        return cls(uri=uri, method='post', params=params).execute() 


    @classmethod
    def list(cls, perPage=None, page=None):
        params = clean_params(locals())
        uri = paystacklib.api_base + cls.object_type 
        return cls(uri=uri, method='get', params=params).execute()

    @classmethod
    def fetch(cls, id_or_slug):
        uri = paystacklib.api_base + \
            '{0}/{1}'.format(cls.object_type, str(id_or_slug))
        return cls(uri=uri, method='get').execute() 

    @classmethod    
    def update(
            cls, id_or_slug, name=None, description=None, amount=None,
            active=None): 
        params = clean_params(locals())
        uri = paystacklib.api_base + \
            '{0}/{1}'.format(cls.object_type, str(id_or_slug)) 
        return cls(uri=uri, method='put', params=params).execute()

    @classmethod
    def check_slug_availability(cls, slug):
        uri = paystacklib.api_base + \
            '{0}/{1}'.format(cls.api_base, slug)
        return cls(uri=uri, method='get').execute()

    @classmethod
    def add_products(page_id, products):
        """
        products is an array of product ids
        """
        params = clean_params(locals())
        del params['page_id']
        uri = paystacklib.api_base + \
            '{0}/{1}'.format(cls.object_type, str(page_id)) + '/product'
        return cls(uri=uri, method='post', params=params).execute()

