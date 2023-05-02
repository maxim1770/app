import logging

import requests
from bs4 import BeautifulSoup

from app import schemas, enums, utils
from app.api import deps
from app.create.prepare.icon.common import _prepare_pravicon_icon_data_url
from app.create.prepare.icon.icons_saint import _find_year_desc, _split_city_and_year_title, _prepare_icon_city
from app.create.prepare.year import PrepareYearTitle

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def _collect_icon_data(session: requests.Session, *, pravicon_icon_id: int) -> str:
    r = session.get(_prepare_pravicon_icon_data_url(pravicon_icon_id))
    full_desc = BeautifulSoup(r.text, 'lxml').find(
        lambda tag: tag.name == 'b' and 'Описание:' == tag.text
    ).next_sibling
    return full_desc


def __prepare_icon_desс(full_desc: str) -> str | None:
    icon_desс: str = utils.clean_extra_spaces(full_desc)
    icon_desс = icon_desс.replace(' -', '-').replace('- ', '-')
    return icon_desс


def __split_and_prepare_icon_desс(full_desc: str, *, year_desc: str) -> str:
    desс = full_desc.replace(f'[{year_desc}]', '')
    desс: str = __prepare_icon_desс(desс)
    return desс


def get_icon_data_in(session: requests.Session, *, pravicon_icon_id: int) -> schemas.IconDataCreate:
    full_desc: str = _collect_icon_data(session, pravicon_icon_id=pravicon_icon_id)
    year_desc: str = _find_year_desc(full_desc)
    if not year_desc:
        year_in = None
        desс: str = __prepare_icon_desс(full_desc)
    try:
        desс: str = __split_and_prepare_icon_desс(full_desc, year_desc=year_desc)
        city, year_title = _split_city_and_year_title(year_desc)
        prepared_year_title: str = PrepareYearTitle(year_title).year_title
        year_in = schemas.YearCreate(title=prepared_year_title)
        if '(?)' in city:
            city_title = None
        else:
            city_title: enums.CityTitle = _prepare_icon_city(city)
    except ValueError as e:
        city_title = None
        year_in = None
    icon_in = schemas.IconCreate(
        desс=desс
    )
    icon_data_in = schemas.IconDataCreate(
        icon_in=icon_in,
        year_in=year_in,
        city_title=city_title
    )
    return icon_data_in


if __name__ == '__main__':
    session: requests.Session = next(deps.get_session())
    for pravicon_icon_id in [4029, 4044, 4046, 4047, 4048, 4070, 4082, 4083, 4084, 4085, 4086, 4087, 4088, 4089, 4090,
                             4098, 4117, 4124,
                             4125, 4126, 4139, 4140, 4150, 4163, 4165, 4168, 4169, 4174, 4176, 4178, 4179, 4180, 4181,
                             4182, 4185, 4186,
                             4187, 4192, 4193, 4195, 4196, 4201, 4204, 4205, 4206, 4207, 4208, 4209, 4210, 4216, 4218,
                             4219, 4223, 4224,
                             4225, 4231, 4237, 4250, 4252, 4253, 4262, 4280, 4289, 4294, 4296, 4297, 4298, 4299, 4300,
                             4301, 4316, 4320,
                             4321, 4326, 4327, 4328, 4329, 4330, 4332, 4338, 4339, 4341, 4343, 4344, 4351, 4365, 4367,
                             4373, 4379, 4380,
                             4386, 4391, 4392, 4395, 4396, 4400, 4401, 4402, 4403, 4404, 4406, 4407, 4408, 4411, 4412,
                             4413, 4414, 4415,
                             4422, 4428, 4429, 4430, 4431, 4432, 4433, 4434, 4435, 4455, 4456, 4466, 4467, 4468, 4469,
                             4470, 4471, 4472,
                             4474, 4475, 4489, 4490, 4491, 4492, 4494, 4495, 4502, 4503, 4504, 4505, 4508, 4513, 4514,
                             4515, 4516, 4517,
                             4518, 4519, 4520, 4530, 4532, 4540, 4541, 4542, 4558, 4559, 4560, 4561, 4562, 4563, 4566,
                             4567, 4568, 4577,
                             4585, 4608, 4609, 4611, 4612, 4613, 4614, 4624, 4625, 4626, 4629, 4633, 4634, 4635, 4636,
                             4639, 4659, 4661,
                             4663, 4666, 4671, 4672, 4701, 4702, 4703, 4704, 4707, 4711, 4712, 4714, 4715, 4722, 4737,
                             4739, 4743, 4756,
                             4757, 4758, 4759, 4763, 4767, 4773, 4774, 4775, 4776, 4777, 4778, 4779, 4780, 4784, 4786,
                             4787, 4789, 4803,
                             4810, 4820, 4821, 4822, 4825, 4839, 4840, 4841, 4845, 4846, 4847, 4857, 4858, 4864, 4865,
                             4868, 4869, 4870,
                             4871, 4872, 4874, 4875, 4883, 4885, 4898, 4899, 4900, 4902, 4903, 4909, 4910, 4911, 4914,
                             4915, 4926, 4927,
                             4945, 4946, 4947, 4948, 4950, 4951, 4952, 4953, 4961, 4962, 4963, 4973, 4974, 4975, 4976,
                             4977, 4978, 4980,
                             4981, 4984, 4985, 4987, 5010, 5011, 5021, 5029, 5031, 5032, 5036, 5040, 5041, 5042, 5043,
                             5044, 5046, 5047,
                             5048, 5049, 5050, 5085, 5086, 5087, 5108, 5109, 5110, 5112, 5113, 5125, 5126, 5127, 5128,
                             5129, 5130, 5151,
                             5152, 5153, 5162, 5163, 5167, 5173, 5174, 5175, 5176, 5177, 5178, 5179, 5181, 5183, 5185,
                             5186, 5187, 5195,
                             5197, 5198, 5200, 5211, 5214, 5215, 5216, 5217, 5218, 5219, 5220, 5221, 5222, 5223, 5224,
                             5228, 5229, 5230,
                             5231, 5232, 5238, 5239, 5240, 5241, 5242, 5243, 5244, 5252, 5253, 5254, 5255, 5259, 5260,
                             5261, 5262, 5263,
                             5264, 5275, 5276, 5281, 5282, 5283, 5284, 5288, 5307, 5308, 5309, 5311, 5314, 5315, 5316,
                             5328, 5331, 5337,
                             5339, 5340, 5341, 5342, 5343, 5349, 5350, 5351, 5352, 5356, 5360, 5364, 5366, 5368, 5379,
                             5380, 5381, 5383,
                             5384, 5385, 5386, 5387, 5388, 5393, 5396, 5397, 5400, 5414, 5416, 5417, 5419, 5420, 5421,
                             5425, 5430, 5434,
                             5436, 5437, 5438, 5439, 5440, 5441, 5442, 5444, 5445, 5446, 5455, 5456, 5457, 5459, 5461,
                             5465, 5478, 5479,
                             5490, 5491, 5492, 5493, 5494, 5495, 5496, 5497, 5498, 5499, 5500, 5522, 5523, 5524, 5525,
                             5529, 5532, 5536,
                             5537, 5538, 5539, 5540, 5543, 5544, 5545, 5547, 5554, 5557, 5560, 5577, 5578, 5580, 5581,
                             5585, 5587, 5591,
                             5592, 5594, 5595, 5598, 5599, 5602, 5603, 5607, 5608, 5609, 5610, 5611, 5617, 5618, 5619,
                             5632, 5633, 5634,
                             5635, 5642, 5645, 5646, 5647, 5655, 5656, 5665, 5666, 5667, 5668, 5672, 5674, 5675, 5679,
                             5680, 5684, 5685,
                             5693, 5694, 5695, 5696, 5697, 5698, 5699, 5700, 5701, 5702, 5703, 5705, 5706, 5707, 5708,
                             5712, 5713, 5717,
                             5718, 5719, 5722, 5723, 5724, 5731, 5732, 5734, 5735, 5737, 5738, 5739, 5740, 5744, 5747,
                             5748, 5750, 5752,
                             5753, 5754, 5757, 5763, 5764, 5766, 5767, 5768, 5769, 5772, 5776, 5778, 5780, 5781, 5785,
                             5786, 5787, 5788,
                             5790, 5791, 5792, 5793, 5795, 5796, 5797, 5798, 5799, 5801, 5802, 5803, 5811, 5812, 5813,
                             5817, 5818, 5819,
                             5820, 5824, 5825, 5826, 5828, 5835, 5836, 5837, 5838, 5840, 5844, 5853, 5854, 5856, 5857,
                             5858, 5862, 5863,
                             5864, 5865, 5866, 5867, 5880, 5881, 5882, 5884, 5894, 5907, 5908, 5910, 5911, 5912, 5923,
                             5924, 5925, 5926,
                             5933, 5936, 5937, 5941, 5942, 5944, 5945, 5952, 5953, 5954, 5983, 5984, 5985, 5986, 5987,
                             5990, 5992, 5993,
                             5994, 6002, 6003, 6004, 6006, 6007, 6008, 6009, 6011, 6012, 6016, 6020, 6022, 6023, 6024,
                             6027, 6028, 6029,
                             6031, 6032, 6034, 6035, 6036, 6042, 6043, 6045, 6046, 6047, 6050, 6056, 6057, 6060, 6061,
                             6063]:
        try:
            a = get_icon_data_in(session, pravicon_icon_id=pravicon_icon_id)
            logging.info(a)
        except AttributeError as e:
            continue
    # a = get_icon_data_in(session, pravicon_icon_id=6614)
    # print(a)
