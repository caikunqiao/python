#字典就是一系列键值对
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
#print(alien_0)
#print(alien_0['color'])
#print(alien_0['points'])
#print("You just earned " + str(alien_0['points']) + " points.")

#增加
alien_0['x_position'] = 0
alien_0['y_position'] = 25
#print(alien_0)

#修改
#alien_0['color'] = 'yellow'
#print(alien_0)

alien_0['speed'] = 'fast'
print(alien_0)
#print("Original x-position: " + str(alien_0['x_position']))
#x_increment = 0
#if alien_0['speed'] == 'slow':
#    x_increment = 1
#elif alien_0['speed'] == 'medium':
#    x_increment = 2
#elif alien_0['speed'] == 'fast':
#    x_increment = 3
#alien_0['x_position'] = alien_0['x_position'] + x_increment
#print("New x-position: " + str(alien_0['x_position']))

#删除
del alien_0['points']
print(alien_0)