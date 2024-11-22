s1 = {12,45,7,3}
s2 = {3,12,56}

print(s1.union(s2)) # {3, 7, 56, 12, 45}

print(s2.intersection(s1)) # {3, 12}

s4 = s1 - s2
print(s4) # {45, 7}

s5 = s2 - s1
print(s5) # {56}
