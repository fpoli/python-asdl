python-asdl
=================

.. image:: https://travis-ci.org/fpoli/python-asdl.svg?branch=master
    :target: https://travis-ci.org/fpoli/python-asdl

A copy of the ASDL parser used in CPython 3.5, cleaned a bit and packaged here.


Installation
------------

.. code-block:: bash

    $ pip install asdl


Usage
-----

.. code-block:: python

    from asdl import ASDLParser, parse

    syntax = """
        module Lambda {
            term =
                Lambda(name x, term body) |
                Apply(term function, term argument) |
                Variable(name x)
        }
    """

    print(ASDLParser().parse(syntax))

    print(asdl.parse("./test/Python.asdl"))

Output:

    Module(Lambda, [Type(term, Sum([Constructor(Lambda, [Field(name, x), Field(term, body)]), Constructor(Apply, [Field(term, function), Field(term, argument)]), Constructor(Variable, [Field(name, x)])]))])

    Module(Python, [Type(mod, Sum([Constructor(Module, [Field(stmt, body, seq=True)]), Constructor(Interactive, [Field(stmt, body, seq=True)]), Constructor(Expression, [Field(expr, body)]), Constructor(Suite, [Field(stmt, body, seq=True)])])), Type(stmt, Sum([Constructor(FunctionDef, [Field(identifier, name), Field(arguments, args), Field(stmt, body, seq=True), Field(expr, decorator_list, seq=True), Field(expr, returns, opt=True)]), ...


License
-------

Same as CPython: Python Software Foundation License (LICENSE file included
here).
