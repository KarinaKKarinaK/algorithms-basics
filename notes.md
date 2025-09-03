# Notes for DSA
_Disclaimer: these notes are taken from online resources (like for e.g. W3 Schools) and LLM tools._

# Data Structures
###  Reasons to implement stacks using lists/arrays:
- Memory Efficient: Array elements do not hold the next elements address like linked list nodes do.
- Easier to implement and understand: Using arrays to implement stacks require less code than using linked lists, and for this reason it is typically easier to understand as well.

### A reason for not using arrays to implement stacks:
- Fixed size: An array occupies a fixed part of the memory. This means that it could take up more memory than needed, or if the array fills up, it cannot hold more elements.