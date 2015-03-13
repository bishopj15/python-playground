class Equipment:
    def __init__(self, pkey, barcode, equipmentType, room, serialNumber, manufacturer, modelNumber, beginDate, cost, age):
        self.pkey = pkey;
		self.barcode = barcode;
		self.equipmentType = equipmentType;
		self.room = room;
		self.serialNumber = serialNumber;
		self.manufacturer = manufacturer;
		self.modelNumber = modelNumber;
		self.beginServiceDate = beginDate;
		self.cost = cost;
		self.age = age;

    
