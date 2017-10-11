# FancyOut
Provides a nice look to terminal programs and logs.

<hr>

## How To Use
```python
from FancyOut include *
```

### Title Function
The title() function provides an easy way to display a nice looking title in the terminal.
For Example:
```python
title("hello world!")
```
Result in the terminal:
```terminal

##################################################
##                 HELLO WORLD!                 ##
##################################################

```
You can specify the width of the title block by adding the argument 'width=x'.  The default width is set to 50.
```python
title("hello world!", width=80)
```

### Output Function
The output() function provides a leader infront of any text you would like to print to screen.  There are a couple choices to choose from.
 - Indent
   - An Indent is 5 spaces
 - Arrow
   - An arrow is `---->`
 - Warning
   - A warning is `#####`

For Example:
```python
output("Preparing Data For Encryption", 'arrow')
output("  Data 1 of 154", 'indent')
output("  Data 2 of 154", 'indent')
output("  Data 3 of 154", 'indent')
output("Data Packet 4 is Corrupt!", 'warning')
```
Result in the terminal:
```terminal
----> Preparing Data For Encryption
        Data 1 of 154
        Data 2 of 154
        Data 3 of 154
##### Data Packet 4 is Corrupt!
```
