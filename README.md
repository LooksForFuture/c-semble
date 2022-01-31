# c-semble
If you have noticed, compiling c++ programs through the terminal and g++ is a difficult task because of the many arguments that g++ has and you have to change these arguments per each program.<br />
c-semble makes this job easier. You should pass a json file to it and it generates a command to terminal and compiles your code. But remember c-semble can only use g++ and it is still WIP, but many features will be added soon.<br />
An example of json file is:
```json
{
    "name":"main",
    "entry":"main.cpp",
    "include-dirs": ["lib"],
    "c++": "11",
    "pre-args": "-Wall"
}
```
This produces (g++ -std=c++11 -Wall -o main main.cpp -I "lib") and runs it inside the terminal.<br />
