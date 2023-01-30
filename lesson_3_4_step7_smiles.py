import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print("\n:3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # какие-то проверки
        assert abs(-42) == 42, "Should be absolute value of a number"


    def test_second_smiling_faces(self, prepare_faces):
        # какие-то проверки
        assert abs(-42) == 42, "Should be absolute value of a number"
