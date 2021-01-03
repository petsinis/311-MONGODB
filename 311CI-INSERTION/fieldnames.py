# -*- coding: utf-8 -*-
int_type = list([
    "ssa", "zip_code", "ward", "police_district", "community_area", "historical_wards", "zip_codes", "community_areas",
    "census_tracts", "wards", "number_of_black_carts_delivered", "number_of_potholes_filled_on_black",
    "number_of_premises_baited", "number_of_premises_with_garbage", "number_of_premises_with_rats","days_as_parked"    
    ])

float_type = list([
    "x_coordinate", "y_coordinate"
    ])    

checked_type = int_type+float_type+list(["creation_date","completion_date","type_of_service_request","latitude","longitude"])