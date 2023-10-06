import sys
import os
import inspect
import importlib
import lbh15
from lbh15.properties.interface import PropertyInterface
from scipy.optimize import minimize_scalar

def load_prop(module_name):
    #res = file_path.split("/")
    #module_name = res[-1][:-3]
    #module_path = file_path[:-len(res[-1])]
    #propertyObjectList = []
    #if module_path not in sys.path:
    #    sys.path.append(module_path)
    #print(module_name)
    propertyObjectList = []
    module = module_name
    for name, obj in inspect.getmembers(sys.modules[module]):
        if inspect.isclass(obj) and obj is not PropertyInterface and not inspect.isabstract(obj):
            if issubclass(obj, PropertyInterface):
                propertyObjectList.append(obj())
    return propertyObjectList


#prop_path = os.getcwd() + "/lbh15/properties/lead_properties.py"
props = load_prop('lbh15.properties.lead_properties')
props += load_prop('lbh15.properties.lead_thermochemical_properties.solubility_in_lead')
props += load_prop('lbh15.properties.lead_thermochemical_properties.diffusivity_in_lead')
props += load_prop('lbh15.properties.lead_thermochemical_properties.lead_thermochemical')
props += load_prop('lbh15.properties.lead_thermochemical_properties.lead_oxygen_limits')
props += load_prop('lbh15.properties.bismuth_properties')
props += load_prop('lbh15.properties.bismuth_thermochemical_properties.solubility_in_bismuth')
props += load_prop('lbh15.properties.bismuth_thermochemical_properties.diffusivity_in_bismuth')
props += load_prop('lbh15.properties.bismuth_thermochemical_properties.bismuth_thermochemical')
props += load_prop('lbh15.properties.lbe_properties')
props += load_prop('lbh15.properties.lbe_thermochemical_properties.solubility_in_lbe')
props += load_prop('lbh15.properties.lbe_thermochemical_properties.diffusivity_in_lbe')
props += load_prop('lbh15.properties.lbe_thermochemical_properties.lbe_thermochemical')
props += load_prop('lbh15.properties.lbe_thermochemical_properties.lbe_oxygen_limits')
props_dict = {}
for prop in props:
    key = prop.name + "_" + prop.correlation_name + "_" + prop.description
    key = key.replace(" ", "_")
    #print(key)
    prop_dict = {}
    min_vals = minimize_scalar(prop.correlation,
                                   bounds=prop.range,
                                   method="Bounded")
    prop_min = min_vals.fun
    prop_T_at_min = min_vals.x
    if prop_T_at_min - prop.range[0] < 5e-4:
        prop_T_at_min = prop.range[0]
        prop_min = prop.correlation(prop_T_at_min)

    def corr_reciprocal(T):
        return 1/prop.correlation(T)

    max_vals = minimize_scalar(corr_reciprocal,
                                bounds=prop.range,
                                method="Bounded")
    prop_max = prop.correlation(max_vals.x)
    prop_T_at_max = max_vals.x
    if prop.range[1] - prop_T_at_max < 5e-4:
        prop_T_at_max = prop.range[1]
        prop_max = prop.correlation(prop_T_at_max)

    prop_dict['min'] = prop_min
    prop_dict['T_at_min'] = prop_T_at_min
    prop_dict['max'] = prop_max
    prop_dict['T_at_max'] = prop_T_at_max
    props_dict[key] = prop_dict

import json
with open('result.json', 'w') as fp:
    json.dump(props_dict, fp, indent=3)
