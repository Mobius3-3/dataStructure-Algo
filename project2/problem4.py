class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        
    def add_group(self, group):
        self.groups.append(group)
    
    def add_user(self, user):
        self.users.append(user)
    
    def get_groups(self):
        return self.groups
    
    def get_users(self):
        return self.users
    
    def get_name(self):
        return self.name



def is_user_in_group(user, group):
    if user in group.get_users():
        return True
    elif group.get_groups() == []:
        return False
    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True
    return False
        

### test cases

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child_user = "child_user"
child.add_user(child_user)
child.add_group(sub_child)
parent.add_group(child)

print("Case1:___________________________________________________________\n")
print("Expect result is True, True, True.\n")
res_1 = is_user_in_group(sub_child_user, parent)
res_2 =is_user_in_group(sub_child_user, child)
res_3 = is_user_in_group(sub_child_user, sub_child)
print("Output is {},{},{}.\n".format(res_1,res_2,res_3))

print("Case2:___________________________________________________________\n")
print("Expect result is False, True, True.\n")
res_4 = is_user_in_group(child_user, sub_child)
res_5 = is_user_in_group(child_user, child)
res_6 = is_user_in_group(child_user, parent)
print("Output is {},{},{}.\n".format(res_4,res_5,res_6))

print("Case3:___________________________________________________________\n")
print("Expect result is False.\n")
res_7 = is_user_in_group('fake', parent)
print("Output is {}.\n".format(res_7))