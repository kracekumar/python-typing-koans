### Python-typing-koans

A set of examples to learn optional static typing in Python.

### Install

- Install Python 3.9.4+.
- Install poetry - https://python-poetry.org/docs/#installation .
- Clone the repository and change the directory to the cloned one.
- Install requirements like `poetry install`.

- If you want to use pip, `pip install -r requirements.txt`.

### Idea

One of the best of ways to learn python-typing is to annotate the code. In this repo, `koans` directory
contains a set of files which will teach you python type-hints by fixing errors. The files carry a suffix from `100`
in the increasing order. By solving errors in the each file in the increasing suffix order, you will gain knowledge
about Python hints. It starts with simple variable annotation and covers topics `function annotation, generics, protocols, classes`.

### How to learn?

The existing files has no annotations or wrong annotation, as a learner, you run one file and fix each errors till there are no type-errors. In the next section, you will learn, how to list all koans and how to run the modified koan file.

### How to run?

- Display one koan file

``` bash
$cat koans/py/100-easy-variable-wrong-type.py
# msg variable is wrongly annotated as int, annotate it as string
msg: int = "hello world!"

# salary is annotated as int, annotate as float
salary: int = 2345.67

# Set is_active as bool
is_active: int = True
```

- Run one koan file

``` bash
$poetry run python cli.py one koans/py/100-easy-variable-wrong-type.py
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Running Mypy on koan file koans/py/100-easy-variable-wrong-type.py
──────────────────────────────────  Mypy errors in koan file koans/py/100-easy-variable-wrong-type.py ───────────────────────────────────
koans/py/100-easy-variable-wrong-type.py:2: error: Incompatible types in assignment (expression has type "str", variable has type "int")
    msg: int = "hello world!"
               ^
koans/py/100-easy-variable-wrong-type.py:5: error: Incompatible types in assignment (expression has type "float", variable has type
"int")
    salary: int = 2345.67
                  ^
Found 2 errors in 1 file (checked 1 source file)

────────────────────────────────────────────────────────────────── End ──────────────────────────────────────────────────────────────────
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

- Run after fixing the errors(riddles) in the file.

``` bash
$poetry run python cli.py one koans/py/100-easy-variable-wrong-type.py
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Running Mypy on koan file koans/py/100-easy-variable-wrong-type.py
No errors in koan file koans/py/100-easy-variable-wrong-type.py 👍
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```
- List all files: `poetry run python cli.py list`

``` bash
$poetry run python cli.py list
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
koans/py/100-easy-variable-wrong-type.py
koans/py/101-easy-tuple-value.py
koans/py/102-easy-list-homogenous.py
koans/py/103-easy-mixed-values.py
koans/py/104-easy-union-example.py
koans/py/105-easy-dictionary-example.py
koans/py/106-easy-function-example.py
koans/py/107-easy-typed-dict.py
koans/py/108-easy-type-alias.py
koans/py/109-easy-user-defined-class.py
koans/py/110-easy-class-variable.py
koans/py/111-medium-callable-annotate.py
koans/py/112-medium-type-as-example.py
koans/py/113-easy-builder-pattern.py
koans/py/114-medium-factory-pattern.py
koans/py/115-medium-protocol-covariant-dbapi-example.py
koans/py/116-easy-factory-example.py
koans/py/117-easy-protocol-across-objects.py
koans/py/118-medium-protocol-behave-like-dict.py
koans/py/119-medium-queue-genrics.py
koans/py/120-medium-decorator.py
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

- Print summary of all koan files.

``` bash
$poetry run python cli.py summary
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 Ran mypy in koan file: koans/py/100-easy-variable-wrong-type.py 👍
 Ran mypy in koan file: koans/py/101-easy-tuple-value.py 👎
 Ran mypy in koan file: koans/py/102-easy-list-homogenous.py 👎
 Ran mypy in koan file: koans/py/103-easy-mixed-values.py 👎
 Ran mypy in koan file: koans/py/104-easy-union-example.py 👎
 Ran mypy in koan file: koans/py/105-easy-dictionary-example.py 👎
 Ran mypy in koan file: koans/py/106-easy-function-example.py 👎
 Ran mypy in koan file: koans/py/107-easy-typed-dict.py 👎
 Ran mypy in koan file: koans/py/108-easy-type-alias.py 👎
 Ran mypy in koan file: koans/py/109-easy-user-defined-class.py 👎
 Ran mypy in koan file: koans/py/110-easy-class-variable.py 👎
 Ran mypy in koan file: koans/py/111-medium-callable-annotate.py 👎
 Ran mypy in koan file: koans/py/112-medium-type-as-example.py 👎
 Ran mypy in koan file: koans/py/113-easy-builder-pattern.py 👎
 Ran mypy in koan file: koans/py/114-medium-factory-pattern.py 👎
 Ran mypy in koan file: koans/py/115-medium-protocol-covariant-dbapi-example.py 👎
 Ran mypy in koan file: koans/py/116-easy-factory-example.py 👎
 Ran mypy in koan file: koans/py/117-easy-protocol-across-objects.py 👎
 Ran mypy in koan file: koans/py/118-medium-protocol-behave-like-dict.py 👎
 Ran mypy in koan file: koans/py/119-medium-queue-genrics.py 👎
 Ran mypy in koan file: koans/py/120-medium-decorator.py 👎
  Koans Summary
┏━━━━━━━━┳━━━━━━━┓
┃ Status ┃ Count ┃
┡━━━━━━━━╇━━━━━━━┩
│ Passed │ 1     │
│ Failed │ 20    │
└────────┴───────┘
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
```

### Resource for learning Python type-hints

- [Typing Docs](https://docs.python.org/3/library/typing.html)
- [MyPy website](https://mypy.readthedocs.io)
- [Optional Static Typing in Python Talk by Guido](https://www.youtube.com/watch?v=GiZKuyLKvAA&t=2521s)
- [Collection of awesome Python types, stubs, plugins, and tools to work with them](https://github.com/typeddjango/awesome-python-typing)

### How to contribute?

- If you feel, some examples will make a great learning material, add a new file in the format `1xx-<easy|medum|hard>-filename.py` and send a PR.
- If you feel some of the koan file is missing enough links or not well-defined please send a PR or raise an issue.
- If you feel some of the concepts needs a better examples or missing, open a PR or create an issue.

### To Support

- [ ] Add async example koans
- [ ] Add third party annotation koans like django, DRF in separate sub-directory in `koans/`.
