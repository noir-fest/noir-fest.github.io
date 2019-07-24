from mailchimp3 import MailChimp

api_key ='a7577134bdfab08d609ebf7f1fbb5813-us3'

 

client = MailChimp(mc_api=api_key, mc_user='s m')
list_id ='ebfc1a9039'


print(client.lists.all(get_all=True, fields="lists.name,lists.id")
)

def add_member(list_id, member_json):
  client.lists.members.create(list_id, member_json)

member_json = {
    'email_address': 'sabzotest@noir.com',
    'status': 'subscribed',
    'merge_fields': {
        'FNAME': 'John',
        'LNAME': 'Doe'}
}

print(add_member(list_id, member_json))
