# CodingProblems
The calendar problem was about building tree and using recursion to compare the exiting bookings and the new booking.

### Approach:
I started with one of the test case data, and observed that the logic is to build the tree. So, I started building the binary tree on paper one by one as per the logic written in the code and using recursion to compare the new date (Node) with the existing root and if present, leaf nodes of the tree.

I realized that the conditions to check and compare start and end date was incorrect. So, I changed the If and elif condition of the insert function and added else part as well. And I also changed the recursive call of if block.

So, after correcting, I did few more test cases which are commented in calender_fix.py;
Also, I have tested with the provided test case and its working fine.

