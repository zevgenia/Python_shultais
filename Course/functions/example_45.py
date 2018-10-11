# -*- coding: utf-8 -*-

#abc = ["a", "b", "c"]
abc = "abc"

vars = []
for i in abc:
    for j in abc:
        vars.append(i + j)

print(vars)

#print([i + j for i in abc for j in abc])
print([i + j for i in abc for j in abc if i != j])
