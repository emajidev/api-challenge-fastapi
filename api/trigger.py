import sys
import pytest

result = pytest.main(["-v"])
exitCode = str(result).split('.')

if 'OK' in exitCode:
    sys.exit(1)
else:
    sys.exit(0)
