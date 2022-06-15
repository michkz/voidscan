
from modules.classes import Asset

def create_original_asset_list(original_scope):
    # add og scope to main_asset property from class
    # figure out how to add validated to same asset
    # validate the main_asset and change to liking 
    scope_list_of_objects = []
    for asset in original_scope:
        asset.strip("\n")
        a = Asset(asset)
        a.add_customer_contact("Bedrijf X","+31 6 13243546")
        scope_list_of_objects.append(a)
    # return list of objects
    return scope_list_of_objects