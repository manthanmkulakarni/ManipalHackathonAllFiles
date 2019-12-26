from firebase import firebase

firebase = firebase.FirebaseApplication('https://calenderapp-357c0.firebaseio.com/', None)
data =  "manthan"
result = firebase.put('/doctor/','message',data)
result = firebase.put('/patients/','message',data)
print(result)
