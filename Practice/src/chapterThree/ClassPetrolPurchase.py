class PetrolPurchase:

    def __init__(self, station_location: str, petrol_Type: str, petrol_Quantity: int, price_PerLiter: float,
                 percentage_discount: float):
        self._station_location = station_location
        self._petrol_Type = petrol_Type
        self._petrol_Quantity = petrol_Quantity
        self._price_PerLiter = price_PerLiter
        self._percentage_discount = percentage_discount

    def get_station_location(self):
        return self._station_location

    def set_age(self, station_location):
        self._station_location = station_location

    def get_petrol_Type(self):
        return self._petrol_Type

    def set_petrol_Type(self, petrol_Type):
        self._petrol_Type = petrol_Type

    def get_petrol_Quantity(self):
        return self._petrol_Quantity

    def set_petrol_Quantity(self, petrol_Quantity):
        self._petrol_Quantity = petrol_Quantity

    def get_price_PerLiter(self):
        return self._price_PerLiter

    def set_set_price_PerLiter(self, price_PerLiter):
        self._price_PerLiter = price_PerLiter

    def get_percentage_discount(self):
        return self._percentage_discount

    def set_percentage_discount(self, percentage_discount):
        self._percentage_discount = percentage_discount

    def get_purchase_Amount(self) -> float:
        net_Purchase = self._petrol_Quantity * self._price_PerLiter - self._percentage_discount
        return net_Purchase * self._petrol_Quantity * self._price_PerLiter * (1 - self._percentage_discount / 100)

    print()



