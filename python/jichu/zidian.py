guiyuan1020s={'hashiqi':'sha','pangzi':'pang'}
print(guiyuan1020s['hashiqi'])      #输入字典中键对应的值
print("you are so "+guiyuan1020s['hashiqi'])
guiyuan1020s['piaochangming']='piao'#向字典里添加键-值对
print(guiyuan1020s)
for key,value in guiyuan1020s.items():#遍历字典键-值对并输出出来
    print(key)
    print(value)
A={'hashiqi':{            #字典中存储字典
        'feature1':'sha1',
        'feature2':'sha2',
        'location':'leshan'},
    'pangzi':{
        'feature1':'pang1',
        'feature2':'pang2',
        'location':'chengdu'}
}
for key1,value1 in A.items():
    print("My name is "+key1.title())
    feature=value1['feature1']+" and "+value1['feature2']
    location=value1['location']
    print("I'm the bigest feature is "+feature)
    print("I'm located in "+location)