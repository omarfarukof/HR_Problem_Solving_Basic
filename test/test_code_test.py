#!/usr/bin/env -S uv run
import pytest # noqa: F401
import subprocess
import os
import pycpptest

# Get the name of the Python file
build_dir = "build"
filename = os.path.basename(__file__)
dirname = os.path.dirname(__file__)
working_dir = dirname[:-(len("test"))] if dirname[-(len("test")):] == "test" else dirname
problem : str = pycpptest.get_problem(filename)
build_problem : str = os.path.join(build_dir,problem)

# Extract test cases from cph file
cph_path = os.path.join(working_dir,".cph")
cph_file = None
files = os.listdir(cph_path)
for file in files:
    if file.startswith(f".{problem}"):
        cph_file = os.path.join(cph_path,file)
        break
testcases = pycpptest.get_test_cases(cph_file)

# make a build directory if it doesn't exist
if not os.path.exists(build_dir):
    os.makedirs(build_dir)

def run_problem(input: str  , problem=f"{build_problem}")->str:
    # give input te a subprocess and take stdout as output
    return subprocess.check_output([f"./{problem}"], input=input.encode('utf-8')).decode('utf-8')
def print_run_problem(input: str  , problem=f"{build_problem}")->str:
    print(run_problem(input , problem))


## [ Pytest ] ==================================
@pytest.mark.parametrize("test_in , test_out" , testcases)
def test_code(test_in , test_out):
    assert run_problem(test_in) == test_in

def test_gen():
    assert True



## [ Main ] (run from Script) ==================
if __name__ == "__main__":
    # compile cpp file
    subprocess.run(["g++","-fsanitize=address","-std=c++20",
        "-Wall","-Wextra","-Wshadow","-O2",
        f"./{problem}.cpp" , "-o", f"{build_problem}"])

    filepath = os.path.join(str(dirname),str(filename))
    os.system(f"pytest -vv {filepath}")