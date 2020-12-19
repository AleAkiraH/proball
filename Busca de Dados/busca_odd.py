import betsapi_login
import facebook_login_get
import facebook_login_post
import betsapi_home
import bus_odd

result = betsapi_login.make_requests()
result = facebook_login_get.make_requests()
result = facebook_login_post.make_requests()
result = bus_odd.make_requests()
# result = betsapi_home.make_requests()


get_odds('')