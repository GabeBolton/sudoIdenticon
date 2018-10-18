# sudoIdenticon
Generates a pixel grid from text. Somewhat like an identicon (**pseudo**Identicon), but allows the user to control and customize the output (**sudo**Identicon)     _ha ha very funny get to the point_
#### Geez, OK.
Basically all you need to do is run the script. 
* It will ask you for a text input phrase
* Give you a few row/column suggestions (interchangable of course), then ask you for columns/rows.
* From there it will create a grid with the designated columns and rows of 3x3 pixel minigrids, assign the 8 outer pixels of each minigrid to the ASCII binary (extended ASCII)of a the corrisponding character normalize the ASCII decimal for central pixel colour, and voila!
## TL;DR: An Example
This is the output from the text "I'm Gabe Bolton. I make stuff. Yeah." formatted in 6x6 grid:
![](https://avatars3.githubusercontent.com/u/33410751?s=400&u=c283527928bbf92b42a3ef7a7e129832731a708b&v=4)  
```
I'm Ga  
be Bol  
ton. I  
 make   
stuff. 
 Yeah.  
```   
Notice how the end squares on the third row match? They are both spaces, as is the bottom left. The ASCII binary for _space_ is 00100000, hence only the top right pixel of the minigrid will be colored.
