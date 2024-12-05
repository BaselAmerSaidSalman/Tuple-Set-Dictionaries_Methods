# Tuple_Methods ()

# 1. Type() النوع => print(type())
# 2. Count() كم مرة تكرر العنصر داخل التابل => Tuple.count(item)
# 3. Slice[] اقتطاع جزء من التابل وطباعته مثل list[][] => print(Tuple[item_index])
# 4. Index() موقع العنصر داخل التابل => print(Tuple.index(item))



# Set_Methods {item_1, item_2}

# 1. add() اضافة عناصر الى السيت ولكن يبقى المتكرر كما هو ولكن لا يمكن اضافة سيت جوا سيت اخرى بواسطتها => print(set.add(item))
# 2. update() اضافة عناصر الى السيت ولكن تحذف المتكرر وتبقى منه واحد فقط ويمكن اضافة سيت الى سيت اخرى بواسطتها => set_1.update(set_2) ثم print(set_1)
# 3. union()  نفس update() => print(variabe_1.union(variable_2))

# 4. difference = (-)  اخذ العناصر الموجودة في السيت الاولى مش موجودة في التانية ولكن تبقى السيت كما هي قبل الحذف بما بها من عناصر => print(set_1.difference(set_2)) => set_1 = set_1 before difference
# 5. difference_update()  مثل difference ولكن تجعل السيت محملة بناتج الطرح مش بالعناصر الاساسية => print(set_1.difference_update(set_2)) => set_1 = set_1 with difference
# 6. intersection() طباعة العناصر المشتركة فقط ولكن تجعل السيت بها هذه العناصر فقط دون غيرها
# 7. intersection_update() طباعة العناصر المشتركة فقط ولكن تجعل السيت بها هذه العناصر فقط دون غيرها
# 8. symmetric_difference() طباعة العناصر اللي مش مشتركة بين الاتنين ولكن تبقى السيت كما هي بما بها من عناصر قبل ذالك 
# 9. symmetric_difference_update() طباعة العناصر اللي مش مشتركة بين الاتنين ولكن تخزن هذه العناصر داخل السيت بدل من عناصرها الاساسية


# 10. copy() جعل المتغير يأخذ نسخة من المتغير التاني فيكونا متساويين ولكن اذا حدث تغير في المنسوخ لا يحدث ذالك التغير في الناسخ => variable_2 = variable_1.copy() => [variable_2 = variable_1], => variable_1.update(item) => [variable_2 != variable_1.update(item)]
# 11. remove() حذف عنصر من السيت ولكن يعطي خطأ عند عدم وجود العنصر المراد حذفه جوا السيت => set.remove(item) 
# 12. discard() حذف عنصر من السيت ولا يعطي خطأ عند عدم وجود العنصر المراد حذفه جوا السيت => set.discard(item) 

# Answer (True or False)
# 13. issuperset() التاكد من ان جميع عناصر السيت اللي بعدها موجودة جوا السيت اللي قبلها
# 14. issubset() التاكد من ان جميع عناصر السيت اللي قبلها موجودة جوا السيت اللي بعدها
# 15. isdisjoint() التاكد من ان كل سيت تحمل عناصر مختلفة عن العناصر التي تحمله السيت الاخرى وليس بينهما تشابه ولو في عنصر واحد




# Dictionaries_Methods {"key_1" : "value_1", "key_2" : "value_2"}

# 1. clear() حذف محتويات القاموس => dictionary.clear()
# 2. update() اضافة عنصر الى القاموس => dictionary.update({"" : ""})
# 3. copy() اخذ نسخة عن القاموس ولكن اذا تم التغيير في المنسوخ فلا يتغير في الناسخ
# 4. keys() طباعة keys اللي جوا القاموس => print(dictionary.keys())
# 5. values() طباعة values اللي جوا القاموس => print(dictionary.values())
# 6. setdefault("key", "value") البحث عن ما في الاقواس في القاموس ام لا فاذا وجده بيطبعه والا فيضاف الى القاموس => print(dictionary.setdefault("key", "value"))
# 7. popitem() طباعة اخر حاجه انضافت جوا القاموس => print(dictionary.popitem())
# 8. items() حفظ كل ما في القاموس جوا [] وحفظ كل عنصر بقيمته جو () => dictionary.items()
# 9. fromkeys(items, item ) جعل كل عنصر في المجموعة items تساوي قيمة item => print(dict.fromkeys(items, item)) 
# dict = dictionary















import time

number_1 = {1, 2, 3}
number_2 = {1, 2, 3, 4, 5}
print(number_1.issuperset(number_2))
print(number_1.issubset(number_2)) 
print(number_1.isdisjoint(number_2))


print("\n******************************** Tuple_Methods() ********************************\n")

# Type()

print("**************** Add()_Method ****************")
my_tuple_one = (1, 2, 3, 4, "Basel", 2.5, True)
my_tuple_two = 1, 2, 3, 4, "Basel", 2.5, True
one_item_tuple = 1,   
one_item_string = 1

print(my_tuple_one)
print(type(my_tuple_one))

print(my_tuple_two)
print(type(my_tuple_two))

print(one_item_tuple)
print(type(one_item_string))

print(one_item_string)
print(type(one_item_string))

print("\n")


# Count()

print("**************** Count()_Method ****************")
my_tuple_one = (1, 2, 3, 4, "Basel", 2.5, True, 2)
print(my_tuple_one.count(2))
print("\n")


# Slice[]

print("**************** Slice()_Method ****************")
my_tuple_one = (1, 2, 3, 4, "Basel", 2.5, True, 2)
print(my_tuple_one[2])
print("\n")


# index()

print("**************** Index()_Method ****************")
my_tuple_one = (1, 2, 3, 4, "Basel", 2.5, True, 2)
print(my_tuple_one.index("Basel"))
print("\n")




print("******************************** Set_Methods() ********************************")
# List[].append() = Set{}.add()

print("**************** Add()_Method ****************")

my_set_names = {"Basel", "Ahmed", "Seif", "Omar"}

print(my_set_names)
my_set_names.add("Ali")
print(my_set_names)
# my_set_names.add(my_set_numbers)
print("\n")


# update() 

print("**************** Update()_Method ****************")

my_set_names = {"Basel", "Ahmed", "Seif", "Omar", "Ali"}
print(my_set_names)

my_set_names_2 = {"Basel", "Ahmed", "Seif", "Ibrahim"}
print(my_set_names_2)

my_set_names.update(my_set_names_2)
print(my_set_names)
print("\n")


# union() نفس update()

print("**************** Union()_Method ****************")

my_set_numbers = {50, 7, 5, 10.9, 100, (0, 4, 2)}
my_set_names = {"Basel", "Ahmed", "Seif", "Omar"}

print(my_set_names)
print(my_set_numbers)
print("\nWay_1\n")
print(my_set_names.union(my_set_numbers))
print("\nWay_2\n")
print(my_set_numbers | my_set_names)
print("\n")



# copy()

print("**************** Copy()_Method ****************")

my_set_names = {"Basel", "Ahmed", "Seif", "Omar"}
print(my_set_names)

my_set_names_2 = my_set_names.copy()
print(my_set_names.union(my_set_numbers))
print(my_set_names)
print(my_set_names_2)
print("\n")


# remove()

print("**************** Remove()_Method ****************")

my_set_names = {"Basel", "Ahmed", "Seif", "Omar"}
print(my_set_names)

my_set_names.remove("Basel")
print(my_set_names)
# my_set_names.remove("Osama")
# print(my_set_names.union(my_set_numbers))
print("\n")


# discard()

print("**************** Discard()_Method ****************")

my_set_names = {"Basel", "Ahmed", "Seif", "Omar"}
print(my_set_names)

my_set_names.discard("Basel")
print(my_set_names)
my_set_names.discard("Osama")
print(my_set_names)
print("\n")


# difference() = (-)  اخذ العناصر الموجودة في السيت الاولى مش موجودة في التانية

print("**************** Difference()_Method ****************")
set_numbers_1 = {1,2,3,4,5}
set_numbers_2 = {1,4,10,5,20.5}
print(set_numbers_1)
print(set_numbers_1.difference(set_numbers_2))
print("\n")


# difference_update()

print("**************** Difference_update()_Method ****************")
set_numbers_1 = {1,2,3,4,5}
set_numbers_2 = {1,4,10,5,20.5}
print(set_numbers_1)
set_numbers_1.difference_update(set_numbers_2)
print(set_numbers_1)
print("\n")


# intersection()

print("**************** Intersection()_Method ****************")
set_numbers_1 = {1,2,3,4,5}
set_numbers_2 = {1,4,10,5,20.5}
print(set_numbers_1)
print(set_numbers_1.intersection(set_numbers_2))
print("\n")


#  intersection_update()

print("**************** Intersection_update()_Method ****************")
set_numbers_1 = {1,2,3,4,5}
set_numbers_2 = {1,4,10,5,20.5}
print(set_numbers_1)
set_numbers_1.intersection_update(set_numbers_2)
print(set_numbers_1)
print("\n")


# symmetric_difference()

print("**************** Symmetric_difference()_Method ****************")
set_numbers_1 = {1,2,3,4,5}
set_numbers_2 = {1,4,10,5,20.5}
print(set_numbers_1)
print(set_numbers_1.symmetric_difference(set_numbers_2))
print("\n")


# symmetric_difference_update()

print("**************** Symmetric_difference_update()_Method ****************")
set_numbers_1 = {1,2,3,4,5}
set_numbers_2 = {1,4,10,5,20.5}
print(set_numbers_1)
set_numbers_1.symmetric_difference_update(set_numbers_2)
print(set_numbers_1)
print("\n")

print(my_set_names)
print(my_set_numbers)
print(my_set_names.intersection(my_set_numbers))


# Dictionaries

# Way_1
languages = {
    "Python Information" : {
        "name" : "Python",
        "progress" : "95%"
    }, 
    "HTML Information" : {
      "name" : "HTML",
      "progress" : "89%"  
    }, 
    "CSS Information" : {
      "name" : "CSS",
      "progress" : "85%"  
    }
}

print(languages)
print(languages['Python Information']['progress'])
print(languages['CSS Information']['progress'])



# Way_2
Python_Information = {
        "name" : "Python",
        "progress" : "95%"
    }

HTML_Information = {
        "name" : "HTML",
        "progress" : "89%"
    }

CSS_Information = {
        "name" : "Python",
        "progress" : "85%"
    }

Programming_Languages = {
    "Python" : Python_Information,
    "Html" : HTML_Information,
    "Css" : CSS_Information
}

Programming_Language_name = input("Please enter a name of programming languages (Python, HTML, CSS)").capitalize()
while Programming_Language_name != "Python" and Programming_Language_name != "Html" and Programming_Language_name != "Css":
    print("Sorry, Invalid input")
    Programming_Language_name = input("Please enter a name of programming languages (Python, HTML, CSS)")

print(f"The {Programming_Language_name} information is: {Programming_Languages[Programming_Language_name]}")
print(Programming_Languages.keys())
#print(Programming_Languages['python'].values())
print(Python_Information.setdefault("name" , "Python"))
print(Python_Information)

a = ("x", "y", "z")
b = 20
print(dict.fromkeys(a, b))

time.sleep(3)