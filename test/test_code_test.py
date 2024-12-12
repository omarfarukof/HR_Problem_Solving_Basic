import pytest
import subprocess
import os

# Get the name of the Python file
filename = os.path.basename(__file__)
dirname = os.path.dirname(__file__)
ext_len = len(filename.split(".")[-1])+1

if filename[:5] == "test_":
    problem : str = filename[5:-ext_len]
else:
    problem : str = filename[:-ext_len]

subprocess.run(["g++","-fsanitize=address","-std=c++20","-Wall","-Wextra","-Wshadow","-O2",f"./{problem}.cpp" , "-o", f"./{problem}"])

def run_problem(input: str  , problem=problem)->str:
    # give input te a subprocess and take stdout as output
    return subprocess.check_output([f"./{problem}"], input=input.encode('utf-8')).decode('utf-8')


def test_code():
    assert True

def test_gen():
    assert [1,2] == [1,2]


if __name__ == "__main__":
    filepath = os.path.join(str(dirname),str(filename))
    # print(filepath)
    os.system(f"pytest -vv {filepath}")