#1
names = ['John','Josh','Rocky']
print(names[0])
print(names[1])
print(names[2])

#2
vehicles = ['auto','plane','bicycle','boat']
print("I would like to buy a",vehicles[2])

#3 
years_list = [1996, 1997, 1998, 1999, 2000, 2001]
print(years_list[3])
years_list.append(2002)
print(years_list)

#4
things = ["wallet","mirror","umbrella"]
print(things[2].capitalize())
print(things[2].upper())
things.remove('umbrella')
print(things)

#5
languages = ["Ukrainian", "French", "Bulgarian", "Norwegian", "Latvian"]
print(languages)
languages.sort()
print(languages)
print(sorted(languages))
languages.reverse()
print(languages)

#6
numbers = [2, -1, 9, 6]
print(sum(numbers))

#7
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
cities.insert(-1,'and')
print(f"{cities[0]}, {cities[1]}, {cities[2]}, {cities[3]}, {cities[4]} {cities[5]} {cities[6]}")

#8
nums = list(range(1,6))
new_nums = sorted(nums)
new_nums.reverse()
print(nums)
print(new_nums)
print(sum(new_nums))


