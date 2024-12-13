import time

import psutil
import pytest

from .exec import exec, exec_get_output, exec_in_background


def test_exec():
    rtn = exec("ls")
    assert rtn == 0

    with pytest.raises(SystemExit) as e:
        exec("xxxx")
    assert e.type == SystemExit
    assert e.value.code != 0

    rtn = exec("xxxx", check=False)
    assert rtn != 0


def test_exec_get_output():
    result = exec_get_output("echo 世界")
    assert result.returncode == 0
    assert result.stdout == "世界\n"

    with pytest.raises(SystemExit) as e:
        exec_get_output("xxxx")
    assert e.type == SystemExit
    assert e.value.code != 0

    result = exec_get_output("xxxx", checked=False)
    assert result.returncode != 0


def find_process(name: str = None, arg: str = None):
    """Find process with a specified name"""
    for process in psutil.process_iter():
        if process.name() == name:
            for one_arg in process.cmdline():
                if one_arg == arg:
                    return True
    return False


def test_exec_in_background():
    exec_in_background('python3 -c "import time; time.sleep(1)"')

    time.sleep(0.1)
    assert find_process("python3", "import time; time.sleep(1)")

    time.sleep(1)
    assert find_process("python3", "import time; time.sleep(1)") == False
