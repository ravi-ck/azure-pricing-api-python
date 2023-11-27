from .index import Filter
from .index import Pricing

__author__ = 'Ravi Rana'
__version__ = '1.0.0'

def get_pricing(filter: list):
    
    FILTER = Filter()
    try:
        if(FILTER._validate_filter(filter)):    
            FILTER._create_filter_string(filter)
            filter_string = FILTER._create_filter_string(filter)
            PRICING = Pricing(filter_string)
            items = PRICING._send_request()
            return items
    
    except Exception as e:
        raise Exception(str(e))
    
    
filter = [
    {
        "armRegionName": "uksouth",
        "serviceName": "Azure Database for MySQL"
    }
]

items = get_pricing(filter)
print(items)