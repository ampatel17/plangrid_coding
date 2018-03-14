
To run the application
	python app.py
	
To run the unit test
	python http_endpoint_tests.py
	
To test application from command line using curl
1. curl localhost:5000/
	OUTPUT: Hello World

2. curl localhost:5000 -H "Accept: application/json"
	OUTPUT: {"message": "Good morning"}

3. curl -X POST http://127.0.0.1:5000/messages -d 'Test Data'
	OUTPUT: Test Data