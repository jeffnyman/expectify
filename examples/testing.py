# Any of these should work:

# from expectify.expect import expect
# from expectify import expect
# from expectify import *

from custom import have_content

from expectify import expect, equal, be_true, be_false

expect("jeff").to(equal("jeff"))
expect("jeff").not_to(equal("geoff"))
expect(True).to(be_true)
expect(False).to(be_false)

expect("jeff was here").to(have_content("jeff"))
