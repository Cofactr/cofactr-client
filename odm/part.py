from typing import Any, Dict, List, Set
from unicodedata import name
from xmlrpc.client import boolean

from dataclass import dataclass

somepart = Part(cpid="XYZ123", load_properties=[labels, alianses, mpn, img])
somepart.mpn

mpn(somepart)

somepart.calc_overage(quant)

calc_overage(somepart, quant)

somepart.mpn

@dataclass
class Part():
    labels: List[Dict]
    aliases: List[Any]
    statements: List[Any]
    offers: List[Any]

    def json(self) -> Dict:
        return {
            "specs": self.specs,
            "mpn": self.mpn,
            "mfg": self.mfg,
        }

    def __repr__(self) -> str:
        return ""

    @property
    def specs(self):
        #list of 
        #dicts each contain: property name (dimension_width), property name for display in GUI (Width (mm)), property value (2), property value for display in gui (2mm)
        return #dict
    
    @property
    def hero_image(self) -> str:
        return #url of image
    
    @property
    def mpn(self) -> str:
        return #best/canonical MPN
    
    @property
    def mfg(self) -> str:
        return self.statements["mfg"] #best/canonical manufacturer name

    @property
    def classification(self) -> str:
        return None

    @property
    def documents(self):
        return #

    @property
    def msl(self) -> str:
        return #msl defaults to 1

    @property
    def package(self) -> str:
        return

    @property
    def terminations(self) -> int:
        return #number of pins

    @property
    def data_age(self):
        return #timestamp of oldest piece of offer data

    @property
    def alternate_mpns(self):
        return
    
    @property
    def availability(self):
        return {
            "buyable": 0,
            "quotable": 0,
            "maybe": 0
        }
    
    def calc_overage(quant: int) -> int:
        return quant

    

#Part class
    #Array of Offer Objects
    #Array of doc dicts
    #Specs array
    #image, mpn, mfg, classification, etc



#Offer Class
    #Seller object associated
    #normal offer stuff (price dict, lead time, etc)

    def __init__(self, part):
        self.part = part

    @property
    def seller(self) -> Seller:
        return self.seller
    
    @property
    def stock(self) -> int:
        return #int for physical unit quantity

    @property
    def lead(self) -> int:
        return #int calendar days for part to arrive with fastest possible ship speed

    @property
    def moq(self) -> int:
        return #minimum order quant
    
    @property
    def multiple(self) -> int:
        return #multiple

    @property
    def authorized(self) -> bool:
        return #is this supplier authorized for this manufacturer

    @property
    def foreign(self) -> bool:
        return #was this price originally in a different currency then USD
    
    @property
    def ship_from_country(self) -> str:
        return #2 letter country code for current location of this part
    
    @property
    def prices(self) -> Dict[int, float]:
        return #dict with keys as the break quant, values as the price in USD per unit at that quant or greater
    
    @property
    def reported_on(self):
        return #timestamp that we received/cached this offer data

    def calculate_tariffs(quant, destination_country) -> float:
        return #estimated tar
    
    def is_exportable(destination_country) -> bool:
        return


#Seller Class
    @property
    def name(self) -> str:
        return #best/canonical name of company
    
    @property
    def accuracy_score(self) -> int:
        return
    
    @property
    def quality_score(self) -> int:
        return
    
    @property
    def additional_markup(self) -> float:
        return
    
    @property
    def additional_fee(self) -> float:
        return

    @property
    def certifications(self) -> Set[str]:
        return

    @property
    def buyable(self) -> bool:
        # There should be an override in the KB. A separate flag for "buyable" that's independent from accuracy.
        return




img = prop("img")

msl = get_property(somepart, "msl")

somepart = part_from_cpid(cpid="somecpid", load_data=[mpn, img, mfg]) #somepart is a dataclass or dict of some sort
response = {
    "mpn": mpn(somepart),
    "mfg": mfg(somepart),
    "specs": specs_array(somepart, unit="metric")
}

somepart = part_from_cpid(cpid="somecpid", load_data=[mpn, img, mfg]) #somepart is a object
response = {
    "mpn": somepart.mpn, #property decorator
    "mfg": somepart.mfg, #property decorator
    "specs": somepart.specs_array(unit="metric") #class function
    "msl": somepart.get_property("msl")
}
