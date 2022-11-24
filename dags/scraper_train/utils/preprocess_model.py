import json
import pandas as pd
from pydantic import BaseModel
from typing import Literal, Optional

class Property(BaseModel):
    area: int
    property_type: Literal["HOUSE", "APARTMENT"]
    zip_code: int
    rooms_number: int
    furnished: Optional[bool] = None
    garden: Optional[bool] = None
    garden_area: Optional[int] = None
    equipped_kitchen: Optional[bool] = None
    full_address: Optional[str] = None
    land_area: Optional[int] = None
    building_state: Optional[Literal[
        "NEW",
        "GOOD",
        "TO_RENOVATE",
        "JUST_RENOVATED",
        "TO_REBUILD"]] = None
    open_fire: Optional[bool] = None
    facades_number: Optional[int] = None
    swimming_pool: Optional[bool] = None
    terrace: Optional[bool] = None
    terrace_area: Optional[int] = None

def preprocess(input_data:Property):
    """
    Function that takes an element as a json like file, and transforms it into an array
    """
    #DICTIONARY OF STATE OF BUILDING
    state_of_the_building_dict = {
        "NEW": 1.0,
        "GOOD": 0.79285,
        "TO RENOVATE": 0.56664,
        "JUST RENOVATED": 0.93115,
        "TO REBUILD": 0.46920
        }

    # data = jsonable_encoder(input_data)
    data = json.dumps(input_data)
    df = pd.DataFrame(data=data, index=[0])

    df.loc[df["area"] < 10, "area"] = 10
    
    df.loc[df["zip_code"] < 1000, "zip_code"] = 1000
    df.loc[df["zip_code"] > 9999, "zip_code"] = 9999
    
    df.loc[df["rooms_number"] < 0, "rooms_number"] = 0

    df["equipped_kitchen"] = df["equipped_kitchen"].astype(bool)

    df["building_state"] = df["building_state"].map({
    "NEW": 1.0,
    "JUST_RENOVATED": 0.75,
    "GOOD": 0.5, #"GOOD"
    "TO_RENOVATE": 0.25,
    "TO_REBUILD": 0.25,
    None: 0.87252
    })

    df.loc[df["facades_number"].isnull(), "facades_number"] = 2
    df["open_fire"] = df["open_fire"].astype(bool)
    df["swimming_pool"] = df["swimming_pool"].astype(bool)
    df["terrace"] = df["terrace"].astype(bool)
    df.loc[df["terrace"] == False, "terrace_area"] = 0
    
    translated_property_data = {
    "number_of_bedrooms": df["rooms_number"].get(0),
    "surface": df["area"].get(0),
    "fully_equipped_kitchen": boolean_to_integer(df["equipped_kitchen"].get(0)),
    "open-fire": boolean_to_integer(df["open_fire"].get(0)),
    "facades_number": df["facades_number"].get(0),
    "swimming_pool": boolean_to_integer(df["swimming_pool"].get(0)),
    "terrace": boolean_to_integer(df["terrace"].get(0)),
    "terrace_surface": df["terrace_area"].get(0),
    "state_of_the_building": df["building_state"].get(0),
    "zip_code_ratio": get_zip_ratio(df["zip_code"].get(0)),
    'HOUSE': 1 if df['property_type'].get(0) == 'HOUSE' else 0,
    'APARTMENT': 1 if df['property_type'].get(0) == 'APARTMENT' else 0
    }
    return list(translated_property_data.values())

def boolean_to_integer(value:bool) -> int:
    if(value == True):
        return 1
    else:
        return 0

def get_zip_ratio(zip_code:int):
    #DICTIONARY OF ZIP CODE VALUES 
    zip_code_dict_xx = {
    'be_zip_10': 1.53,
    'be_zip_11': 1.68,
    'be_zip_12': 1.66,
    'be_zip_13': 1.29,
    'be_zip_14': 1.18,
    'be_zip_15': 1.24,
    'be_zip_16': 1.31,
    'be_zip_17': 1.23,
    'be_zip_18': 1.22,
    'be_zip_19': 1.5,
    'be_zip_20': 1.53,
    'be_zip_21': 1.17,
    'be_zip_22': 1.13,
    'be_zip_23': 1.12,
    'be_zip_24': 1.03,
    'be_zip_25': 1.24,
    'be_zip_26': 1.27,
    'be_zip_27': 1.11, 
    'be_zip_28': 1.22,
    'be_zip_29': 1.3,
    'be_zip_30': 1.58,
    'be_zip_31': 1.18,
    'be_zip_32': 1.1,
    'be_zip_33': 1.07,
    'be_zip_34': 0.87,
    'be_zip_35': 1.13,
    'be_zip_36': 1.0,
    'be_zip_37': 0.9,
    'be_zip_38': 0.94,
    'be_zip_39': 1.0,
    'be_zip_40': 0.93,
    'be_zip_41': 0.85,
    'be_zip_42': 0.86,
    'be_zip_43': 0.87,
    'be_zip_44': 0.81,
    'be_zip_45': 0.76,
    'be_zip_46': 0.95,
    'be_zip_47': 0.98,
    'be_zip_48': 0.85,
    'be_zip_49': 0.94,
    'be_zip_50': 0.97,
    'be_zip_51': 1.0,
    'be_zip_52': 0.77,  
    'be_zip_53': 0.87,
    'be_zip_54': 0.77,
    'be_zip_55': 0.76,
    'be_zip_56': 0.67,
    'be_zip_57': 0.77,
    'be_zip_58': 0.77,
    'be_zip_59': 0.77,
    'be_zip_60': 0.64,
    'be_zip_61': 0.74,
    'be_zip_62': 0.78,
    'be_zip_63': 0.69,
    'be_zip_64': 0.66,
    'be_zip_65': 0.67,
    'be_zip_66': 0.91,
    'be_zip_67': 0.97,
    'be_zip_68': 0.84,
    'be_zip_69': 0.83,
    'be_zip_70': 0.8,
    'be_zip_71': 0.69,
    'be_zip_72': 0.67,
    'be_zip_73': 0.58,
    'be_zip_75': 0.86,
    'be_zip_76': 0.66,
    'be_zip_77': 0.79,
    'be_zip_78': 0.91,
    'be_zip_79': 0.66,
    'be_zip_80': 1.34,
    'be_zip_81': 1.25,
    'be_zip_82': 1.32,
    'be_zip_83': 2.12,
    'be_zip_84': 1.43,
    'be_zip_85': 1.06,
    'be_zip_86': 1.61,
    'be_zip_87': 1.16,
    'be_zip_88': 0.98,
    'be_zip_89': 0.95,
    'be_zip_90': 1.46,
    'be_zip_91': 1.13,
    'be_zip_92': 1.11,
    'be_zip_93': 1.03,
    'be_zip_94': 1.0,
    'be_zip_95': 0.96,
    'be_zip_96': 0.94,
    'be_zip_97': 1.11,
    'be_zip_98': 1.27,
    'be_zip_99': 1.16
    }

    return zip_code_dict_xx['be_zip_'+str(zip_code)[:2]]