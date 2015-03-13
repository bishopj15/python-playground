class EquipmentInformation:
    def __init__(pkey, barcode, equipmentFk, room, serialNumber, manufacturer, modelNumber, beginDate, cost, age):
        self.pkey = pkey;
		self.barcode = barcode;
		self.equipmentTypeFk = equipmentFk;
		self.room = room;
		self.serialNumber = serialNumber;
		self.manufacturer = manufacturer;
		self.modelNumber = modelNumber;
		self.beginServiceDate = beginDate;
		self.cost = cost;
		self.age = age;
