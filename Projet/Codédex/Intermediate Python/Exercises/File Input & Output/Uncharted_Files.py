sent_message = 'Hey there! This is a secret message.'

with open('sent_message.txt', 'w') as file:
  file.write(sent_message)

with open('sent_message.txt', 'r+') as file:
  original_message = file.read()
  file.seek(0)
  unsent_message = 'This message has been unsent.'
  file.truncate(len(unsent_message))
  file.write(unsent_message)

print("Original message :",original_message)
print("Unsent message : ",unsent_message)
