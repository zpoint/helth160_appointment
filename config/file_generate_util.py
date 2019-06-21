from check.location import CheckLocation
from check.hospital import CheckHospital


class ConfigFileGenerator(object):
    def __init__(self):
        self.city_name = self.city_id = self.hospital_id = None

    async def generate(self):
        pass

    async def get_city_info(self):
        print("正在获取城市信息...")
        location_check = CheckLocation()
        name_id_map = await location_check.check()

        while not self.city_id:
            result = input("请输入你要查询的城市中文名, 比如: 深圳")
            result = result.strip()
            if result in name_id_map:
                self.city_name, self.city_id = result, name_id_map[result]
            else:
                for name, id_ in name_id_map.items():
                    if result in name:
                        self.city_name, self.city_id = name, id_
                        break
            print("查询不到你所输入的城市:%s, 请重新输入" % (result, ))

    async def get_hospital_info(self):
        hospital_check = CheckHospital()

        while not self.hospital_id:
            keyword = input("请输入你要查询的医院名称关键字, 比如: 港大医院")
            keyword = keyword.strip()
            print("正在获取医院信息...")
            results = await hospital_check.check(keyword, self.city_id)
            for each in results:
                pass
