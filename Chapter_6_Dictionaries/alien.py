#一个简单的字典

#外星人的特点

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color': 'green'}

print(alien_0['color'])


alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']

print("You just earned " + str(new_points) + " points!")



#添加键-值对

alien_0 = {'color': 'green','points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)



#先创建一个空字典

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)


#修改字典中的值


alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + '.')



#例子：对一个能够以不同速度移动的外星人的位置进行跟踪

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x_position: " + str(alien_0['x_position']))

alien_0['speed'] = 'fast'   #将这个速度中等的外星人变成速度很快的外星人

#向右移动外星人
#据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的速度一定很快
    x_increment = 3


#新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x_position: " + str(alien_0['x_position']))



#删除键-值对

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)




























