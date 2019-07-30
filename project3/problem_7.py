# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler = None, not_found_handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode('root handler')
        self.not_found_handler = not_found_handler
        
    def insert(self, path, leave_handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        cur = self.root 
        if path == '' or path == '/':
            cur.handler = leave_handler
            return 
        
        path_list = path[:-1].split('/') if path.endswith('/') else path.split('/')

        for r in path_list:
            if r not in cur.children:
                cur.children[r] = RouteTrieNode()
            cur = cur.children[r]
        cur.handler = leave_handler
        cur.is_leave = True

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        cur = self.root
        if path == '' or path == '/':
            return cur.handler
        path_list = path.split('/')[:-1] if path.endswith('/') else path.split('/')
        
        for r in path_list:
            if r not in cur.children:
                return self.not_found_handler
            cur = cur.children[r]
        return cur.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler
        self.is_leave = False

    def insert(self, router_content, handler_content=None):
        # Insert the node as before
        node = RouteTrieNode(handler_content)
        node.is_leave = True
        self.children[router_content] = node
        self.is_leave = False

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler_content=None, not_found_handler = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie(handler_content, not_found_handler)
        
    def add_handler(self, path, handler = None):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        return self.routes.insert(path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        return self.routes.find(path)

    def split_path(self,path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split('/')[:-1] if path.endswith('/') else path.split('/')

# Here are some test cases and expected outputs you can use to test your implementation
print('—'*20,'Case1:','—'*20,)
# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

# create the router and add a route
print('—'*20,'Case2:','—'*20,)
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/for/me", "me handler")  # add a route

# some lookups with the expected output
print(router.lookup("")) # should print 'root handler'
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'not found handler' or None
print(router.lookup("/home/about/")) # should print 'not found handler' or None
print(router.lookup("/home/for/me")) # should print 'me handler' 

print('—'*20,'Case3:','—'*20,)
router1 = Router("", "not found handler") 
router1.add_handler("/home/contact", "")  # add a route
router1.add_handler("/home/department/resources", "resources handler")  # add a route

print(router1.lookup("")) # should print should print 'root handler'
print(router1.lookup("/home")) # should print None 
print(router1.lookup("/home/contact/")) # should print '' 
print(router1.lookup("/home/department/resources")) # should print 'resources handler' 
router1.add_handler("/home", "Home Page")
print(router1.lookup("/home")) # should print 'Home Page' 

router1.add_handler("", "Landing Page")
print(router1.lookup("/")) # should print 'Landing Page' 
print('\nAll pass!')