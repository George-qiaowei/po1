import pytest
import yaml


def analyze_data():
    with open("./data/data.yaml", "r") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


class TestLogin:

    # 188, 188123
    # 177, 177123
    # 166, 166123
    @pytest.mark.parametrize(("phone", "pwd"), analyze_data())
    def test_phone(self, phone, pwd):
        print(phone)
        print(pwd)

    # zs
    # ls
    def test_username(self):
        pass
