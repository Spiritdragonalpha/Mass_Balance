from classes import Node, Stream
from utils import *


class MF(Node):
    def __init__(self,name,
                XR_percentage= 0.15,
                volume_btwn_ASBW=250,           #gal
                feed_to_waste_ASBW=10,          #gal/module
                feed_to_waste_FF=4,             #gal/module 
                module_surface_area=538,        #ft^2
                ASBW_duration=1,                #min
                ASBW_other_duration=0.5,        #min
                maintaince_clean_duration=50,   #hr
                n_units=1,
                n_modules_per_unit=10,
                 ):
        super().__init__(name)
        
        self.inputs = {
            'feed':None
            }
        
        self.outputs = {
            'filtrate': Stream(f'{name}_filtrate'),
            'XR': Stream(f'{name}_xr')
            }
        # ---User-defined parameters---
        self.XR_percentage = XR_percentage
        self.volume_btwn_ASBW = volume_btwn_ASBW
        self.feed_to_waste_ASBW = feed_to_waste_ASBW
        self.feed_to_waste_FF = feed_to_waste_FF
        self.module_surface_area = module_surface_area
        self.ASBW_duration = ASBW_duration
        self.ASBW_other_duration = ASBW_other_duration
        self.maintaince_clean_duration = maintaince_clean_duration
        self.n_units = n_units
        self.n_modules_per_unit = n_modules_per_unit


        # ---Calculated parameters---
        self.instant_flux = None
        self.avg_flux = None            #Need to define how to calculate this
        self.ASBW_frequency = None
        self.avg_module_flow = None
        self.n_modules_total = None
        self.ASBW_cycles = None
        self.ASBW_instant_flow = None
        self.ASBW_daily_avg = None
        self.XR_per_module_instant = None
        self.XR_instant_flow = None
        self.XR_daily_avg = None
        self.gross_feed_daily_avg = None
        self.gross_filtrate_daily_avg = None
        self.gross_feed_instant = None
        self.gross_filtrate_instant = None
        self.net_filtrate_discharged_daily_avg = None
        self.filter_service_factor = None
        self.hf_discharge_effluent = None



    def solve(self):
        feed = sum(stream.flow for stream in self.inputs.values() if stream is not None)
        filtrate = self.outputs['filtrate']
        XR = self.outputs['xr']

        XR.flow = feed.flow * self.XR_percentage
        filtrate.flow = feed.flow - XR.flow

        self.ASBW_frequency = self.volume_btwn_ASBW/(self.avg_flux*self.module_surface_area/(24*60-self.maintaince_clean_duration))
        self.instant_flux = (self.gross_filtrate_instant*1440)/self.module_surface_area/self.n_modules_total
        self.ASBW_cycles = (1440-self.maintaince_clean_duration)/(self.ASBW_frequency+self.ASBW_duration+self.ASBW_other_duration)
        self.ASBW_instant_flow = (self.feed_to_waste_ASBW+self.feed_to_waste_FF)/self.ASBW_duration*self.n_modules_per_unit
        self.ASBW_daily_avg = self.ASBW_cycles*(self.feed_to_waste_ASBW+self.feed_to_waste_FF)*self.n_modules_total
        self.XR_per_module_instant = self.XR_instant_flow/self.n_modules_total
        self.XR_instant_flow = self.gross_feed_instant - self.gross_filtrate_instant
        self.gross_feed_daily_avg = (self.gross_filtrate_daily_avg/(1-self.XR_percentage))
        self.gross_filtrate_daily_avg = self.avg_flux * self.module_surface_area * self.n_modules_total
        self.net_filtrate_discharged_daily_avg = self.gross_filtrate_daily_avg - self.ASBW_daily_avg
        self.filter_service_factor = ((1440-self.maintaince_clean_duration)-(self.ASBW_cycles*(self.ASBW_duration+self.ASBW_other_duration)))/60
        self.hf_discharge_effluent = self.net_filtrate_discharged_daily_avg + (27168/1400)


    def get_parameters(self):
                return {
            'XR_percentage': self.XR_percentage,
            'volume_btwn_ASBW': self.volume_btwn_ASBW,
            'feed_to_waste_ASBW': self.feed_to_waste_ASBW,
            'feed_to_waste_FF': self.feed_to_waste_FF,
            'module_surface_area': self.module_surface_area,
            'ASBW_duration': self.ASBW_duration,
            'ASBW_other_duration': self.ASBW_other_duration,
            'maintaince_clean_duration': self.maintaince_clean_duration,
            'n_units': self.n_units,
            'n_modules_per_unit': self.n_modules_per_unit,
            'ASBW_frequency': self.ASBW_frequency,
            'instant_flux': self.instant_flux,
            'avg_flux': self.avg_flux,
            'avg_module_flow': self.avg_module_flow,
            'n_modules_total': self.n_modules_total,
            'ASBW_cycles': self.ASBW_cycles,
            'ASBW_instant_flow': self.ASBW_instant_flow,
            'ASBW_daily_avg': self.ASBW_daily_avg,
            'XR_per_module_instant': self.XR_per_module_instant,
            'XR_instant_flow': self.XR_instant_flow,
            'XR_daily_avg': self.XR_daily_avg,
            'gross_feed_daily_avg': self.gross_feed_daily_avg,
            'gross_filtrate_daily_avg': self.gross_filtrate_daily_avg,
            'gross_feed_instant': self.gross_feed_instant,
            'gross_filtrate_instant': self.gross_filtrate_instant,
            'net_filtrate_discharged_daily_avg': self.net_filtrate_discharged_daily_avg,
            'filter_service_factor': self.filter_service_factor,
            'hf_discharge_effluent': self.hf_discharge_effluent

        }