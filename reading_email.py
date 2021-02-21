import imapclient
import pyzmail

#pip install imapclient #pip install pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
print(conn.login('donakolab94@gmail.com', 'password'))

conn.select_folder('INBOX', readonly=True)

# Returns a list of uniques id representing mail
# Read up imap search keys Table 16-3
uids = conn.search(['SINCE 20-Aug-2015'])
print(uids)

rawMessage = conn.fetch([474], ['BODY[]', 'FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessage[4747] [b'BODY[]'])

print(message.get_subject())

message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('bcc')

print(message.text_part)
print(message.html_part)

message.text_part.get_payload().decode('UTF-8')
#get encoding
print(message.text_part.charset)