from bardapi import Bard

token = 'XwjsURlfq-r2R6M7xYYnVNJ5VZyWLyblVoNuEejmqGMk4Z6v9KuislrHbK9V4oQXu8vhqQ.'
bard = Bard(token=token)
response=bard.get_answer("What is Machine learning?")['content']
print(response)