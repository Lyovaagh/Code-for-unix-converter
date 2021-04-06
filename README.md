# Code-for-unix-converter
Prepare and converted web code for Unix

Այս ծրագիրը նախատեսված է 
- կայքերը վինդոուսից(windows) յունիքս(unix) տեղափոխելու համար
  - բոլոր դիրեկտորիաները(dirctories) դարձվում են փոքրատառ
  - ֆայլերի անունները մնում են նույնը
  - ֆայլերի մեջ հղումները (src=... href=...) ճշտվում են՝ դառնում են փոքրատառ
- ծրագիրը գրված է պայթոնով և չեմ օգրվել BeautifulSoup-ի հնարավորություններից
  որպեսզի խուսափեմ BeautifulSoup-ը python 3 - ում տեղադրելու անհարմարություններից
  նաև չեմ ուզել օգտվել Anaconda 3 -ից կամ ել օգտվել python 2 -ից։
- աշխատում է հետևյալ կերպ․
  - ծրագրի մուտքին տալիս ենք pբացարձակ path-ը
  - ծրագիրը (path, name) -ում և նրա բորոր դիրեկտորիաներում կարարում է անհրաժեշտ
    փոփոխությունները օգտվելով ռեկուրսիայի հնարավորություններից
- փոխադրվում են հիմնականում (html, htm, php, js) ֆայլերը
- բոլոր (.PHP|.html|.htm|.js|.css) ֆայլերը ելքում արդեն փոփոխված են։

Օրինակ՝
python PreparePythonCodeForUnix.py "C:/temp/test/test/aaaa"

Հուսով եմ, որ այն օգտակար կլինի Ձեզ
 
This program is designed for:
- moving websites from windows to unix
  - all directories become lowercase
  - filenames remain the same
  - the links in the files (src = ... href = ...) are becoming lower case
- the program is written with an explosion and I did not use the capabilities of 
  BeautifulSoup to avoid the inconvenience of installing BeautifulSoup in python 3 
  and I didn't use Anaconda 3 or python 2.
- works as follows ․
  - at the entrance of the program we give the absolute path
  - program (path, name) Makes the necessary changes in all its directories 
    using the recursion capabilities
- mainly (html, htm, php, js) files are transferred
- all (.PHP|.html|.htm|.js|.css) files have already been modified in the output. 

example։
python PreparePythonCodeForUnix.py "C:/temp/test/test/aaaa"

I hope you find it useful․
