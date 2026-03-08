# pytest Capstone — QA Automation Portfolio

A clean pytest project demonstrating core QA automation skills: fixtures, parametrize, markers, coverage, and HTML reports.

## Skills Demonstrated

| Skill | Where |
|-------|-------|
| `@pytest.fixture` + `yield` teardown | `conftest.py` |
| Fixture chaining (fixture depends on fixture) | `conftest.py` → `admin_permissions` |
| `autouse=True` — automatic test logging | `conftest.py` → `log_test` |
| `@pytest.mark.parametrize` with `pytest.param` IDs | `test_validators.py` |
| `xfail` + `skip` on individual cases | `test_validators.py` |
| `pytest.raises()` for exception testing | `test_validators.py` |
| Custom markers: `smoke` + `regression` | `pytest.ini` + all test files |
| Fixture + parametrize combined | `test_permissions.py` |
| HTML report generation | `pytest.ini` |
| Coverage reporting | `pytest --cov` |

## Project Structure

```
pytest_capstone/
├── conftest.py               # shared fixtures (autouse log, db, admin_permissions)
├── pytest.ini                # config: markers, HTML report, testpaths
├── requirements.txt
├── src/
│   └── validators.py         # functions under test
└── tests/
    ├── test_validators.py    # password, age, divide — 17 test cases
    └── test_permissions.py   # login + permissions — 11 test cases
```

## Running the Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run full suite (generates report.html)
pytest

# Run smoke tests only
pytest -m smoke

# Run regression tests only
pytest -m regression

# Run with coverage
pytest --cov=src --cov-report=term-missing
```

## Test Count

| File | Tests | Markers |
|------|-------|---------|
| `test_validators.py` | 17 | smoke + regression |
| `test_permissions.py` | 11 | smoke + regression |
| **Total** | **28** | |

---

**Author:** Ahmed Hesham — SW Validation Engineer → QA Automation Engineer
**Stack:** Python · pytest · pytest-html · pytest-cov
