grades={'Alice':[3,1,2,8],'Mark':[9,1,10,4],'Anna':[1,2,3,4,5,6,7,8,9],'Pablo':[5,6,6,8,1]}
for key in grades:
    gradeslist=grades[key]
    gradeslist.sort(reverse=True)
    print(key+"'s highest grade: " + str(gradeslist[0]))
