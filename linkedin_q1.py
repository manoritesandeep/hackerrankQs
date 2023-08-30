data = [x for x in range(5)]
temp = [x for x in range(7) if x in data and x %2==0]
print(temp)


print('abcefd'.replace('cd','12'))

y =8
z = lambda x:x*y
print(z(6))


a = max(False, -3,-4)
b = min(a,2,7)
print(b)

t =(9)
print(t*4)  # Output 36

def fn(var1):
    var1.pop(1)

var1=[1,2,3]
fn(var1)
print(var1)