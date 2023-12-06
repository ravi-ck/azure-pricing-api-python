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