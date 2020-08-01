## Python alternative modules install prefix scheme


```python
set PYTHONPATH=<project-folder>\<module-folder>\Lib\site-packages

pip install --prefix=<project-folder>\<module-folder> module_name

```

## Or Download packages and do


```python
py setup.py install --prefix=<project-folder>\<module-folder>
```

## In your scripts



```python
sys.path.append(os.path.dirname(__file__) + <module-folder>\Lib\site-packages )
```
