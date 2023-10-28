0th test data:
keyIndices:
[0, 1]
result of method call ElemsFinder.IndicesOfSameKeys(l, keyIndices):
([[0, 2, 3], [1, 4], [5, 6]], True)
result of method call ElemsFinder.NestedValuesOfSameKeys(l, keyIndices):
([('Func1', [['argv1', None], ['argv2', 'int']], 'pass\n        '), ('Func1', [['argv1', None], ['argv2', 'int']], 'return "Func1"\n        '), ('Func1', [['argv1', None], ['argv2', 'int']], 'Nothing'), ('Func2', [['argv1', None], ['argv2', None], ['', None]], 'pass\n   '), ('Func2', [['argv1', None], ['argv2', None], ['', None]], 'return "Func2"'), ('Func1', [['argv1', None]], 'pass\n        '), ('Func1', [['argv1', None]], 'return "Func1"')], True)
----------------------------------------
1th test data:
keyIndices:
[0, 1, 2]
result of method call ElemsFinder.IndicesOfSameKeys(l, keyIndices):
([], False)
result of method call ElemsFinder.NestedValuesOfSameKeys(l, keyIndices):
([], False)
----------------------------------------
2th test data:
keyIndices:
[0, [1, 2]]
result of method call ElemsFinder.IndicesOfSameKeys(l, keyIndices):
([[0, 2, 3], [1, 4], [5, 6]], True)
result of method call ElemsFinder.NestedValuesOfSameKeys(l, keyIndices):
([('Func1', [['argv1', None], ['argv2', 'int']], 'pass\n        '), ('Func1', [['argv1', None], ['argv2', 'int']], 'return "Func1"\n        '), ('Func1', [['argv1', None], ['argv2', 'int']], 'Nothing'), ('Func1', [['argv1', None]], 'pass\n        '), ('Func1', [['argv1', None]], 'return "Func1"'), ('Func2', [['argv1', None], ['argv2', None], ['', None]], 'pass\n   '), ('Func2', [['argv1', None], ['argv2', None], ['', None]], 'return "Func2"')], True)
----------------------------------------
3th test data:
keyIndices:
[0, [1]]
result of method call ElemsFinder.IndicesOfSameKeys(l, keyIndices):
([[0, 2, 3], [1, 4], [5, 6]], True)
result of method call ElemsFinder.NestedValuesOfSameKeys(l, keyIndices):
([('Func1', [['argv1', None], ['argv2', 'int']], 'pass\n        '), ('Func1', [['argv1', None], ['argv2', 'int']], 'return "Func1"\n        '), ('Func1', [['argv1', None], ['argv2', 'int']], 'Nothing'), ('Func1', [['argv1', None]], 'pass\n        '), ('Func1', [['argv1', None]], 'return "Func1"'), ('Func2', [['argv1', None], ['argv2', None], ['', None]], 'pass\n   '), ('Func2', [['argv1', None], ['argv2', None], ['', None]], 'return "Func2"'), ('Func3', [['argv1', None]], 'pass\n        '), ('Func3', [['argv1', None], ['argv2', None]], 'pass\n        ')], True)
----------------------------------------
4th test data:
keyIndices:
[0, []]
result of method call ElemsFinder.IndicesOfSameKeys(l, keyIndices):
([[0, 2, 3], [1, 4], [5, 6]], True)
result of method call ElemsFinder.NestedValuesOfSameKeys(l, keyIndices):
[('Func1', [['argv1', None], ['argv2', 'int']], 'pass\n        '), ('Func1', [['argv1', None], ['argv2', 'int']], 'return "Func1"\n        '), ('Func1', [['argv1', None], ['argv2', 'int']], 'Nothing'), ('Func1', [['argv1', None]], 'pass\n        '), ('Func1', [['argv1', None]], 'return "Func1"'), ('Func2', [['argv1', None], ['argv2', None], ['', None]], 'pass\n   '), ('Func2', [['argv1', None], ['argv2', None], ['', None]], 'return "Func2"'), ('Func3', [['argv1', None]], 'pass\n        '), ('Func3', [['argv1', None], ['argv2', None]], 'pass\n        ')]
----------------------------------------
5th test data:
keyIndices:
[[], []]
result of method call ElemsFinder.IndicesOfSameKeys(l, keyIndices):
([[0, 2, 3], [1, 4], [5, 6]], True)
result of method call ElemsFinder.NestedValuesOfSameKeys(l, keyIndices):
[]
----------------------------------------
6th test data:
keyIndices:
[]
result of method call ElemsFinder.IndicesOfSameKeys(l, keyIndices):
[('Func1', [['argv1', None], ['argv2', 'int']], 'pass\n        '), ('Func2', [['argv1', None], ['argv2', None], ['', None]], 'pass\n   '), ('Func1', [['argv1', None], ['argv2', 'int']], 'return "Func1"\n        '), ('Func1', [['argv1', None], ['argv2', 'int']], 'Nothing'), ('Func2', [['argv1', None], ['argv2', None], ['', None]], 'return "Func2"'), ('Func1', [['argv1', None]], 'pass\n        '), ('Func1', [['argv1', None]], 'return "Func1"'), ('Func3', [['argv1', None]], 'pass\n        '), ('Func3', [['argv1', None], ['argv2', None]], 'pass\n        ')]
result of method call ElemsFinder.NestedValuesOfSameKeys(l, keyIndices):
[('Func1', [['argv1', None], ['argv2', 'int']], 'pass\n        '), ('Func2', [['argv1', None], ['argv2', None], ['', None]], 'pass\n   '), ('Func1', [['argv1', None], ['argv2', 'int']], 'return "Func1"\n        '), ('Func1', [['argv1', None], ['argv2', 'int']], 'Nothing'), ('Func2', [['argv1', None], ['argv2', None], ['', None]], 'return "Func2"'), ('Func1', [['argv1', None]], 'pass\n        '), ('Func1', [['argv1', None]], 'return "Func1"'), ('Func3', [['argv1', None]], 'pass\n        '), ('Func3', [['argv1', None], ['argv2', None]], 'pass\n        ')]
----------------------------------------
