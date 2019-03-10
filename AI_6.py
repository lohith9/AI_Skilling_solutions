my_dict= { 'pentagon' : [35,60,51,45,40],
                  'Rectangle': [20,29,71, 91],
                  'tri_angle': [17,9,19],
                  'Trapizeum': [25,60,50,44],
                  'triangle':[19,20,17],
                  'Square' :[23,26,27,22],
                  'Hexagon': [24,16,22,14,20,18],
                  'Rhombus' : [26,36,34,28]
               }
cost = 0
for i in (my_dict):
    print(my_dict[i])
print('Initial Position of s')
print('s moved in pentagon',min(my_dict['pentagon']))
cost+=min(my_dict['pentagon'])
print(cost)
if min(my_dict['Rectangle'] )==my_dict['Rectangle'][0] or min(my_dict['Rectangle'] )==my_dict['Rectangle'][1]  :     
    print('s moved in Rectangle',min(my_dict['Rectangle']))
    cost+=min(my_dict['Rectangle'])
else:
    print('s moved in Rectangle',my_dict['Rectangle'][0],min(my_dict['Rectangle']))
    cost+=min(my_dict['Rectangle'])+my_dict['Rectangle'][0]
print(cost)
if min(my_dict['tri_angle'] )==my_dict['tri_angle'][0]:
    print('s moved in tri_angle',min(my_dict['tri_angle']))
    cost+=min(my_dict['tri_angle'])
else:
    print('s moved in tri_angle',my_dict['tri_angle'][0],min(my_dict['tri_angle']))
    cost+=min(my_dict['tri_angle'])+my_dict['tri_angle'][0]
print(cost)
if min(my_dict['Trapizeum'] )==my_dict['Trapizeum'][0] or min(my_dict['Trapizeum'] )==my_dict['Trapizeum'][1]  :     
    print('s moved in Trapizeum',min(my_dict['Trapizeum']))
    cost+=min(my_dict['Trapizeum'])
else:
    print('s moved in Trapizeum',my_dict['Trapizeum'][0],min(my_dict['Trapizeum']))
    cost+=min(my_dict['Trapizeum'])+my_dict['Trapizeum'][0]
print(cost)
if min(my_dict['triangle'] )==my_dict['triangle'][0] :
    print('s moved in triangle',min(my_dict['triangle']))
    cost+=min(my_dict['triangle'])
else:
    print('s moved in triangle',my_dict['triangle'][0],min(my_dict['triangle']))
    cost+=min(my_dict['triangle'])+my_dict['triangle'][0]
print(cost)
if min(my_dict['Square'] )==my_dict['Square'][0] or min(my_dict['Square'] )==my_dict['Square'][1]  :     
    print('s moved in Square',min(my_dict['Square']))
    cost+=min(my_dict['Square'])
else:
    print('s moved in Square',my_dict['Square'][0],min(my_dict['Square']))
    cost+=min(my_dict['Square'])+my_dict['Square'][0]
print(cost)
if min(my_dict['Hexagon'] )==my_dict['Hexagon'][0] or min(my_dict['Hexagon'] )==my_dict['Hexagon'][1]  :     
    print('s moved in Hexagon',min(my_dict['Hexagon']))
    cost+=min(my_dict['Hexagon'])
else:
    print('s moved in Hexagon',my_dict['Hexagon'][0],min(my_dict['Hexagon']))
    cost+=min(my_dict['Hexagon'])+my_dict['Hexagon'][0]
print(cost)
if min(my_dict['Rhombus'] )==my_dict['Rhombus'][0] or min(my_dict['Rhombus'] )==my_dict['Rhombus'][1]  :     
    print('s moved in Rhombus',min(my_dict['Rhombus']))
    cost+=min(my_dict['Rhombus'])
else:
    print('s moved in Rhombus',my_dict['Rhombus'][0],min(my_dict['Rhombus']))
    cost+=min(my_dict['Rhombus'])+my_dict['Rhombus'][0]
print('Total cost to reach destination',cost)




 
