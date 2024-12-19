# Any of these should work:

# from expectify.expect import expect
# from expectify import expect
# from expectify import *

from expectify import expect, equal, be_true

expect("jeff").to(equal("jeff"))
expect("jeff").not_to(equal("geoff"))
expect(True).to(be_true)
