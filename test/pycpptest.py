import json

# VS Code runCommand parameters
# "CreateTestPy": "mkdir -p ${workspaceFolder}/test && cp -n ${homedir}/Project/template_code/competitive_programming/pycpptest.py ${workspaceFolder}/test/pycpptest.py &&  cp ${homedir}/Project/template_code/competitive_programming/test_run.py ${workspaceFolder}/test/test_${fileBasenameNoExtension}.py && chmod +x ${workspaceFolder}/test/test_${fileBasenameNoExtension}.py",
# "RunCppTest": "${workspaceFolder}/test/test_${fileBasenameNoExtension}.py",
# 
# `test_run.py` file is need as template for pytest

def get_problem(filename: str) -> str:
    ext_len = len(filename.split(".")[-1])+1
    if filename[:5] == "test_":
        return filename[5:-ext_len]
    else:
        return filename[:-ext_len]

def get_test_cases(cph_file: str|None) -> list[tuple[str, str]]:
    testcases = []
    if cph_file is not None:
        with open(cph_file, 'r') as f:
            cph = json.load(f)
            f.close()

        tests = cph["tests"]
        for test in tests:
            test_in = test["input"]
            test_out = test["output"]
            testcases.append((test_in , test_out))

    return testcases