<h1>Solution</h1>

<p>My solution for this lesson is described as followed! I first made a Student object containing a student id, lowest page number,  a latest page number and further the number of assignment scores, average score and how many submissions the student made.</p>
<p>First I had the first element of the list indicate how many instances that are taken in. I looped over my instances over the lines and appended it 
to a new list when splitting via white spaces.</p>
<p>I created a dictionary to store my data. Empty At first, I looped over the list that was given and check if that id (which should be unique) is not in the dictonary.
If so, I then added it to the dictionary. After adding it to the dictionary,
here is where the logic gets spicy.</p>

<p>First there are two conditions, if the student is not in the dictionary, add it to the dictionary, set its id and set its lowest
and current page number if the AccessCode is P. Otherwise if its access code is S, update its submission count by one and its score given in the input.</p>

<p>The second condition is fairly similar but checking if the existing students in the dictionary and follows the Accesscode check. However it tries to find the lowest page number or check to see if the lowest page number is zero to check for the lowest within the existing students.</p>
<p>Both conditions find the average score and once the checking is done it puts it into a list and sorts the list via average score, lowestPageNum and latest page num. I then made a loop to print out the attributes and seperate each output with a new line from each object.</p>

<p>My algorithmic solution took around O(s log(s) + L) since I had to loop over the intial list, and check if it follows the certain conditions. If the condition is when the item is not in the dictionary, it follows the first if statement, otherwise a new student is created as well.</p>

<p>I also asked Craig Barber for some clarification on some of my logic throughout my code. Some of my logic within my code for lesson 7 failed the guidelines but also once me and him took a look we were able to fix some logic correct and get my code to pass the gradescope tests</p>