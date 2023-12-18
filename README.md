# Azure Pricing API Python
azurepricingapi is a python wrapper around the Azure Retail Prices Rest API, which helps you to eaily get Azure Retail Prices using python.
We have tried to style it similar to the AWS pricing api.

## Installation
The pricing api could be easily installed by using the following command:

```bash
    pip3 install azurepricingapi
```

## Example

```
from azurepricingapi import get_pricing


filter = [
    {
        "armRegionName": "eastus",
        "serviceFamily": "Databases"
    }
]

results = get_pricing(filter)

for item in results:
    print(item)
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[Apache](https://choosealicense.com/licenses/apache-2.0/)
