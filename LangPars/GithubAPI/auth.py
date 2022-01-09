token = ''
if token != '':
    header_dict = {'authorization': f"token {token}"}
else:
    header_dict = {}
