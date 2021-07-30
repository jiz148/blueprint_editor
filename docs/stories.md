# Blueprint Editor Dev Stories

> this file is for stories in developing Blueprint Dditor


## Contents

* [Model](#model)
  - [Operation](#operation)


<a name='model'></a>
## Model

* Should have [model](/model) directory

<a name='operation'></a>
### Operation

* Should have [operation](/model/operation) directory
* Should have [operation/implement](/model/operation/implement)director
* Should have [operation.py](/model/operation/operation.py) as an interface
* ```operation.py``` should have function ```generate_operation```. This function should take a json and return a string of code
* In implement directory, should have the implementation of each operation; For each operation, should have function **```generate_code```**, which takes a json, and returns a string of code

