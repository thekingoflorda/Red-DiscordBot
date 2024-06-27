# Report for Assignment 1

## Project chosen

Name: Red-DiscordBot

URL: https://github.com/Cog-Creators/Red-DiscordBot

Number of lines of code and the tool used to count it: 61662

Programming language: Python

## Coverage measurement

### Existing tool

We used coverage.py in combination with Pytest. The command entered was coverage run -m pytest tests followed by coverage report.

This resulted in:
![CleanShot 2024-06-22 at 12 05 00@2x](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/12137089-561f-4164-96a3-7ea73fb716e6)

### Your own coverage tool

Teammember: Luc

Function 1: set_balance

https://github.com/thekingoflorda/Red-DiscordBot/commit/186b53ae9a5832e0792aff2b3c01f06b8d4368bf

![CleanShot 2024-06-22 at 12 10 20@2x](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/598a28f8-a010-4241-9fc3-774edf66a025)
In this image you can see the result that the coverage tool put in a special file. I tagged each conditional branch, 500 - 506 are the ones related to this function.

Function 2: withdraw_credits

[<Provide the same kind of information provided for Function 1>](https://github.com/thekingoflorda/Red-DiscordBot/commit/186b53ae9a5832e0792aff2b3c01f06b8d4368bf

![CleanShot 2024-06-22 at 12 10 20@2x](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/598a28f8-a010-4241-9fc3-774edf66a025)
In this image you can see the result that the coverage tool put in a special file. I tagged each conditional branch, 507 - 509 are the ones related to this function.

Teammember: Bram

Function 1: get_account

https://github.com/thekingoflorda/Red-DiscordBot/commit/368e7067e209c3c11689d88cc2a3c57047d0614d

![image](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/9449b504-e45f-4446-8fc0-bf4cc13087a2)
In this image you can see the result of the coverage tool that has been put into branch_coverage.txt. The listed values are for each conditional branch, if the tests covered the branch, the value would change from False to True.
Currently the coverage reaches the 2nd, 3rd and 4th branches but not the 1st one.

Function 2: get_bank_name

https://github.com/thekingoflorda/Red-DiscordBot/commit/368e7067e209c3c11689d88cc2a3c57047d0614d

![image](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/48570454-2d62-49fa-97ec-1d09ecb1c248)
In this image you can see the result of the coverage tool that has been put into branch_coverage.txt. The listed values are for each conditional branch, if the tests covered the branch, the value would change from False to True.
Currently the coverage reaches only the 3rd one, with the 1st, 2nd and 4th not being reached.


Teammember: Ivan

Function: test_trivia_lists

With the dictionary branch_coverage we track if a specific branch was executed (initially all of them areset to False and, when they run set_branch_coverage method changes according branch's value to True. At the end of program execution I also want to right the report of how the coverage performed in branch_coverage_report.txt file.

## Coverage improvement

### Individual tests

Teammember: Luc

test_bank_set

https://github.com/thekingoflorda/Red-DiscordBot/commit/b037fa4fe0e9fe593ce0e1fdf4700504587e2108

![CleanShot 2024-06-22 at 12 10 20@2x](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/598a28f8-a010-4241-9fc3-774edf66a025)

![CleanShot 2024-06-22 at 12 08 04@2x](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/9b4e0186-d33d-41b5-8712-fc9a4425d06f)

With the original tests 3/6 conditional branches actually ran, my changes increased this by to 5/6, with the one left being a bit weird, since it runs the same piece of code regardless of the conditional path taken.
I improved the coverage by adding a new set of tests that test different kind of input errors, like inputting a string, inputting a negative value and going above the maximum value.

test_bank_set

https://github.com/thekingoflorda/Red-DiscordBot/commit/998fed24ce393340d4945c54b9f4c3013065daec

![CleanShot 2024-06-22 at 12 10 20@2x](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/598a28f8-a010-4241-9fc3-774edf66a025)

![CleanShot 2024-06-22 at 12 08 04@2x](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/9b4e0186-d33d-41b5-8712-fc9a4425d06f)

With the original tests 0/3 conditional branches where actually run, with the new tests all of them ran.
I achieved this by inputting a float value, a negative number and trying to withdraw so much that the value of the bank account went under 0.

Teammember: Bram

test_get_account:

https://github.com/thekingoflorda/Red-DiscordBot/commit/368e7067e209c3c11689d88cc2a3c57047d0614d

![image](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/286b4741-7a6f-47c5-988c-274b89cec642)

![image](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/4d44a551-3634-4ecb-9c3c-17d82f781edd)

With the original tests 3/4 conditional branches ran, with my implemented changes this increased to 4/4.
This was improved by simulating the called on bank being global and running the get_account function.

test_get_bank_name:

https://github.com/thekingoflorda/Red-DiscordBot/commit/368e7067e209c3c11689d88cc2a3c57047d0614d

![image](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/b4ac2c80-6e59-47a3-afe1-3e38ce49874c)
![image](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/ac063ed8-c23c-4fb4-92ca-332bdb5e7836)

With the original tests 1/4 conditional branches ran, with my implemented changes this increased to 4/4.
This was improved by simulating the called on bank being global and running the get_bank_name function, and also by supplying the function with a bank's name variable being None.

Teammember: Ivan

In my new test cases:
  1. test_trivia_lists_empty_list_names function tests the condition where get_core_lists returns an empty list;
  2. test_trivia_lists_invalid_list_error_yaml function tests the InvalidListError with a YAML error cause;
  3. test_trivia_lists_invalid_list_error_schema function tests the InvalidListError with a Schema error cause.

Mocking is used to simulate different return values and exceptions from the methods get_core_lists and get_list.

Coverage report is also put in the branch_coverage_report.txt file.


### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

Luc:
Forked the code and altered the github page to comply with the assignment requirements. 

Ivan:
Completed own part and tried to help others as mush as could.

Bram:
Completed own part and helped others when neccessary.
