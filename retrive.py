from firebase import firebase

firebase = firebase.FirebaseApplication('https://calenderapp-357c0.firebaseio.com/', None)
result = firebase.get('/doctor/', '')
print(result['message'])

result = firebase.get('/patients/', '')
print(result['message'])