import facebook


token="EAAHMASkfXIEBAM8PLqlzYZBt9nuV7u8l29OAL8hcnjysoJJZAUCboID0rPxeXik4TwUzjYs0JDmnrreCsISttH7s908d0FFep7OvAZA6VBJkZBmGZBc75hhAwirSheI8pRMZBV8YzyDZB92yWswOLIHkxhgIpcv1dkKndZCec1w0LKq9ZAGpba6R5S500INWJLTpvnGyd7opNvayUQc6ziOpaZBAZBBw9ZBzIxeIzZBs0V9qrSgZDZD"

graph = facebook.GraphAPI(access_token="your_token", version="2.12")

post=graph.get_connections(id='me', connection_name='friends')