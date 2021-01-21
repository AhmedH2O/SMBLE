# SMBLE
Introducing SMBLE
Simple Mark-up Boxing Language (Easy)

This project is a mark-up language replacment for programmers
it has a lot of features (not all of the are implemented yet).

To use this script you will submit a file with the disscussed format and
it will generate a standard HTML file.

To use this language you should choose the language :
    To choose a language use /// and the name of your language ///html
    (currently only supporting html, but css, php, and javascript is to be added in the 
    next update).
    
1- Tag 
Instead of <tag>content</tag> you will write [tag, content].
ex: 
  [em, this will be emphasaized] = <em> this will be emphasaized</em>
  
2- Self-closing tags
Instead of  <tag atr="value">  you will write [tag atr=value].
ex:
  [img src=google.com] = <img src="google.com">
  
3-  Styling
Instead of  <tag style="atr:value;">content</tag> you will write
[tag atr'value,content].
ex:
  [span color'red, this is red] = <span style="color:red;"> this is red</span>
 
4- Class
Instead of <tag class="class_name"> content</tag> you will write 
[tag .class_name, content].
ex:
  [p .describtion, this is a description of something] = <p class="describtion"> this is a description of something</p>
 
5-ID 
Instead of  <tag id="id_name">content</tag> you will write 
[tag ..id_name,content].
ex:
  [h2 ..subtitle, this is the subtitle] = <h2 id="subtitle"> this is the subtitle</h2>

6- In addition you don't need to write <!Doctype html> and anything before <body> it automaticaly writes it.
  
  
Future updates will have :

1- CSS

2- PHP

3- JavaScript

4- In HTML their will be escape sequence /this is escaped/.

5- In HTML their will be easier comments 'this is a comment'.

6- In HTML their will be multiple attributes assignment available.

7- In HTML their will be a list shortcut simply using the -(minus) at 
  the beginning of the line will use unordered list and 0- will use ordered list.
  
8- In CSS their will be a lot of shortcuts that are easier to remember and they
  will use logic rather than memorization.

Thanks for taking the time to read and remeber to report any bug or 
suggestion to contribute in the making of the final project.
 
