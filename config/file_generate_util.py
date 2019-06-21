from check.location import CheckLocation
from check.hospital import CheckHospital


class ConfigFileGenerator(object):
    def __init__(self):
        self.city_name = self.city_id = self.hospital_id = None

    async def generate(self):
        pass

    async def get_city_info(self):
        print("���ڻ�ȡ������Ϣ...")
        location_check = CheckLocation()
        name_id_map = await location_check.check()

        while not self.city_id:
            result = input("��������Ҫ��ѯ�ĳ���������, ����: ����")
            result = result.strip()
            if result in name_id_map:
                self.city_name, self.city_id = result, name_id_map[result]
            else:
                for name, id_ in name_id_map.items():
                    if result in name:
                        self.city_name, self.city_id = name, id_
                        break
            print("��ѯ������������ĳ���:%s, ����������" % (result, ))

    async def get_hospital_info(self):
        hospital_check = CheckHospital()

        while not self.hospital_id:
            keyword = input("��������Ҫ��ѯ��ҽԺ���ƹؼ���, ����: �۴�ҽԺ")
            keyword = keyword.strip()
            print("���ڻ�ȡҽԺ��Ϣ...")
            results = await hospital_check.check(keyword, self.city_id)
            for each in results:
                pass
