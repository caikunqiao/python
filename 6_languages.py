favorite_languages = {
    'joe': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'jack': 'python',
    }
#print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

#方法item()返回一个键值对列表
#for key,value in favorite_languages.items():
#    print("\nname: " + key.title())
#    print("\nlanguage: " + value.title())

#遍历字典默认遍历所有的键
#for name in favorite_languages.keys():
#for name in favorite_languages:
#    print(name.title())

#friends = ['phil', 'sarah']
#for name in friends:
#    if name in favorite_languages.keys():
#        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

#if 'erin' not in favorite_languages.keys():
#    print("please take our poll")

#for name in sorted(favorite_languages.keys()):
#    print(name.title() + ", thank you for taking the poll.")

#set集合不包含重复项
for language in set(favorite_languages.values()):
    print(language.title())