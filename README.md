# paystack-lib-python
This library provides an implementation of the Paystack API with a focus on completeness, production readiness and ease of use.

## Installation
```
pip3 install --upgrade paystacklib
```

## Requirements
Python 3.5+

## Usage
The Paystack secret key should be defined in the Environment as `PAYSTACK_SK` or assigned to `paystacklib.api_key`

```
>>> import paystacklib
>>> paystacklib.secret_key = 'sk_your_paystack_secret_key' #or export secret key in environment as PAYSTACK_SK
>>> transaction = paystacklib.Transaction.initialize(500000, 'customer@customer.com')
>>> transaction
{'status': True, 'message': 'Authorization URL created', 'data': {'authorization_url': 'https://checkout.paystack.com/6rklpsq157c8bef', 'access_code': '6rklpsq157c8bef', 'reference': 'i1wdh5b2r3'}}
>>> transaction.status
True
>>> transaction.message
'Authorization URL created'
>>> transaction.data.authorization_url
'https://checkout.paystack.com/6rklpsq157c8bef'
>>> transaction.data.access_code
'6rklpsq157c8bef'
>>> transaction.data.reference
'i1wdh5b2r3'
>>> transaction['status']   #you can also access values this way
True
>>> transaction.whatever    #trying to access element that does exist will return a 'False' value
{}
```

