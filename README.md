# MongoDB

How to run:
  This is a python file, so you can run this by using "python3 json_flat.py". 
  After runng it will ask for 2 option, 
  
  Option 1: Don't use api, In this option it will run the default given 'test.json' file. 'test.json' contains the json object given at the task. Just press 1 and Enter, it will flat the data object.
  
  Option 2: Use API: In this option you can paste any JSON web api, and after validating (whether it contains an array), it will flat the API objet. Press 2 and enter, then it will ask for API, paste API and press Enter.
  
  

Code Base:

  In order to run the API, I've added 2 methods. First one is sub_str(), this will remove 's' from 'https'. This has to be done other wise API's will not run on terminal because of SSL certificate security. 2nd method is api_method(), this uses sub_str() and returns contents of API. Some API's like SpaceX etc will not run on terminal because of higher security measures. please use the given API below for testing.
  
Rest of the methods are for validating and Flattening the JSON object.


NOTE: DON'T use Pipeline with this, because in order to add API functionality, I'd to made this mode user friendly. But ecery thing is provided, you don't need to input any thing. It will use default JSON file. I emailed your team a week ago, I didn't receive any response, that's why I am going with this version. 

API To TEST with,

https://api.coindesk.com/v1/bpi/currentprice.json


https://api.agify.io/?name=bella


THANKS...
  
  
