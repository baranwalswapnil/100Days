country=("India", "Pakistan","Bangladesh","America")
temp=list(country)
temp.append("Russia")
temp.pop(4)
temp[2] = "China"
temp.insert(1,2)
country=tuple(temp)
print(country)