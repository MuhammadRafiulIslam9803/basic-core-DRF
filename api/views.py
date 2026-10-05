from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET'])
def item_list(request):
    courses ={
        "course_name": "Python",
        "course_duration": "3 months",
        "course_fee": 3000
    }

    return Response(courses)

@api_view(['GET' , 'POST' ,'PUT' , 'PATCH' , 'DELETE' ])
def studentData(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    # এখানে আমরা request থেকে কিছু নিচ্ছি না।
    # প্রথমে Student.objects.all() দিয়ে database-এর সব student নিলাম 
    # এবং students-এর মধ্যে রাখলাম।
    # এরপর ওই student object-গুলোকে StudentSerializer দিয়ে JSON format-এর 
    # উপযোগী করলাম।
    # এখানে many=True দিলাম কারণ আমরা একজন না, অনেকগুলো student serialize করছি।
    # তারপর serializer.data দিয়ে সেই student-গুলোর data response হিসেবে return করলাম।

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    # এখানে আমরা request থেকে যে নতুন student-এর data এসেছে,
    # সেটা request.data দিয়ে নিলাম।
    # এরপর সেই data-টা StudentSerializer-এর মধ্যে দিয়ে serializer-এ রাখলাম।
    # তারপর serializer.is_valid() দিয়ে check করলাম যে request থেকে 
    # আসা data ঠিক আছে কিনা।
    # যদি data ঠিক থাকে, তাহলে serializer.save() দিয়ে 
    # সেই নতুন student-কে database-এ save করলাম।
    # তারপর serializer.data দিয়ে newly created student-এর data return করলাম
    # এবং status=201 দিলাম, কারণ নতুন data successfully তৈরি হয়েছে।
    # আর যদি data ঠিক না থাকে, তাহলে serializer.errors দিয়ে কোথায়
    # ভুল হয়েছে সেটা return করলাম এবং status=400 দিলাম।
    
    elif request.method == 'PUT':
        student_id = request.data.get('id')
        object = Student.objects.get(id=student_id)
        serializer = StudentSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    # প্রথমে request থেকে id নিলাম এবং student_id-এর মধ্যে রাখলাম।
    # এরপর Student.objects.get(id=student_id) দিয়ে 
    # database-এর মধ্যে ওই id-র সাথে যে student মিলে, 
    # সেই student object-টা object-এর মধ্যে রাখলাম।
    # এরপর StudentSerializer(object, data=request.data) দিয়ে বললাম—
    # এই যে database-এর পুরোনো student object, 
    # এটাকে request থেকে আসা নতুন data দিয়ে update করো।
    # তারপর serializer.is_valid() দিয়ে check করলাম নতুন data ঠিক আছে কিনা।
    # ঠিক থাকলে serializer.save() দিয়ে database-এর student-টাকে update করলাম।
    # এরপর updated data serializer.data দিয়ে return করলাম এবং status=200 দিলাম।
    # আর data ভুল হলে serializer.errors return করলাম এবং status=400 দিলাম।
    
    elif request.method == 'PATCH':
        student_id = request.data.get('id')
        object = Student.objects.get(id=student_id)
        serializer = StudentSerializer(object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    # প্রথমে request থেকে id নিলাম এবং student_id-এর মধ্যে রাখলাম।
    # এরপর Student.objects.get(id=student_id) দিয়ে 
    # database থেকে ওই id-র student object-টা বের করে object-এর মধ্যে রাখলাম।
    # এরপর StudentSerializer(object, data=request.data, partial=True) দিয়ে বললাম—
    # এই student object-টাকে request থেকে আসা data দিয়ে update করো।
    # এখানে partial=True দেওয়ার কারণে সব field পাঠাতে হবে না।
    # শুধু যে field পরিবর্তন করতে চাই, সেই field পাঠালেই হবে।
    # এরপর serializer.is_valid() দিয়ে data ঠিক আছে কিনা check করলাম।
    # ঠিক থাকলে serializer.save() দিয়ে database-এ update করলাম।
    # তারপর updated data serializer.data দিয়ে return করলাম এবং status=200 দিলাম।
    # আর ভুল হলে serializer.errors এবং status=400 return করলাম।
    
    elif request.method == 'DELETE':
        student_id = request.data.get('id')
        object = Student.objects.get(id=student_id)
        object.delete()
        return Response(status=204)

    # প্রথমে request থেকে id নিলাম এবং student_id-এর মধ্যে রাখলাম।
    # এরপর Student.objects.get(id=student_id) দিয়ে 
    # database থেকে ওই id-র student object-টা বের করে object-এর মধ্যে রাখলাম।
    # এরপর object.delete() দিয়ে বললাম—
    # এই student object-টাকে delete করো।
    # এরপর status=204 দিলাম।