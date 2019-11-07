# JSON-Merge

## Objective 
To merge a series of files containing JSON array of Objects into a single file containing a single JSON object. 

## Installation
Run the setup file to install the dependencies : 

```bash
python setup.py install
```

## Run the demo

```bash
python main.py $filepath$ $baseinfile$ $baseoutfile$ $maxfilesize$
```

## Run the unittest 

```bash
python unitTest.py
```
## Description 

Algorithm : We open each file in the increasing suffix order and keep dumping it into a local json object til maxFilesize is reached. Once it is reached, we write the previously copied content into a out file and reset the json object to take in new loads of json data. 

### Time Complexity : 

O(maxFilesize * number of files) and a better bound would be, $O(\sum_{i=1}^{N} fileSize_i)$

### Space Complexity : 

O(maxFilesize)
