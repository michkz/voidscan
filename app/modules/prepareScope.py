from app.modules.classes import Asset


def create_original_asset_list(original_scope):
    # Create list to store objects in
    scope_list_of_objects = []
    for asset in original_scope:
        asset.strip("\n")
        # Create an Asset() for every asset found in original scope
        a = Asset(asset)
        # Add customer contact information to each asset
        a.add_customer_contact("Bedrijf X", "+31 6 13243546")
        scope_list_of_objects.append(a)
    # Return the list of assets as objects
    return scope_list_of_objects
