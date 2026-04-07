# Case-Trail

To start tests playwright must be installed
```
pip install pytest-playwright
playwright install
```

All dependencies in
```
*/casetrail/requirements.txt
```

Start dev server
```bash
cd /Users/**/PycharmProjects/casetrail/app
pytohn manage.py runserver
```

Start tests
```bash 
pytest --slowmo=400 --browser=firefox --headed app/tests/e2e/test_template.py
```