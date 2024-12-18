# Any of these should work:

# from expectify.expect import expect
# from expectify import expect
# from expectify import *

from expectify import expect, equal

expect("jeff").to(equal("jeff"))
