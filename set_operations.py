#"union or |"it combines values form both sets but it takes unique values
s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}
s3={1,2,3,4,5,6}
print(s1.union(s2))
#intersection or &  will display only common values between set 
print("-----------intersection------")
print(s1.intersection(s2))
print(s1)
#intersection update  will display only common values between set and delete unwantes elemnts from original set 
print("-----------intersection update ------")
print(s1.intersection_update(s2))
print(s1)
print(s2)
#difference will print value that are present only in first set but not in second set
print("-----Difference----------")
s2={4,5,6,7,8,9}
s3={1,2,3,4,5,6}
print(s2.difference(s3))
#difference update will print value that are present only in first set but not in second set and remove unwanted elemnts from original set
print("-----Difference update----------")
print(s2.difference_update(s3))
print(s2)
print(s3)
#subset 
print("------subset-----")
sub={1,2,3,4}
sup={1,2,3,4,5,6,7,8,9}
print(sub.issubset(sup))
print(sup.issuperset(sub))
#disjoint set  if there are no common elements in both sets.
print("---------disjoint---------")
dis1={1,2,3,4}
dis2={5,6,7,8,9}
print(dis1.isdisjoint(dis2))
print(dis2.isdisjoint(dis1))
