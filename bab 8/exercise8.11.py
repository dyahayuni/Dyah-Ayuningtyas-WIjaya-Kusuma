def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim: {current_message}")
        sent_messages.append(current_message)


texts = ['Halo!', 'Lagi apa?', 'Nanti malam jadi ketemu?']
sent_messages = []

send_messages(texts[:], sent_messages)

print("\nList texts:", texts)
print("List sent_messages:", sent_messages)