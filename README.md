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

![image](https://github.com/thekingoflorda/Red-DiscordBot/assets/122359361/7eca1a22-a642-42ff-83d6-d43e3e655e92)

In this image you can see the result of the coverage tool that has been put into branch_coverage.txt. The listed values are for each conditional branch, if the tests covered the branch, the value would change from False to True.
Currently the coverage reaches the 2nd, 3rd and 5th branches but not the 1st and the 4th one.

Function 2: get_bank_name

https://github.com/thekingoflorda/Red-DiscordBot/commit/368e7067e209c3c11689d88cc2a3c57047d0614d

![image](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/48570454-2d62-49fa-97ec-1d09ecb1c248)
In this image you can see the result of the coverage tool that has been put into branch_coverage.txt. The listed values are for each conditional branch, if the tests covered the branch, the value would change from False to True.
Currently the coverage reaches only the 3rd one, with the 1st, 2nd and 4th not being reached.


Teammember: Ivan

Functions: test_trivia_lists, _get_error_message

With the dictionary branch_coverage we track if a specific branch was executed (initially all of them areset to False and, when they run set_branch_coverage method changes according branch's value to True. At the end of program execution I also want to right the report of how the coverage performed in branch_coverage_report.txt file.

With the initial coverage tool I have got the following results:

![image](https://github.com/thekingoflorda/Red-DiscordBot/assets/122359361/a57e1e19-a8c1-473f-ad19-8a7cd97b29a2)



Teammember: Zenno

Function 1: is_command

https://github.com/thekingoflorda/Red-DiscordBot/commit/82f19155b3fe8138d679ae80d0ace062c460e7ba

<img width="265" alt="Screenshot 2024-06-27 at 20 01 08" src="https://github.com/thekingoflorda/Red-DiscordBot/assets/78911539/ff125494-5731-4918-be11-8ee4776f44ea">

In this image we see the result the branch coverage wrote to the branch_coverage_zenno.txt file, the first 2 are relevant for the is_command function, as we can see none of the branches get covered yet.

Function 2: get_prefix

https://github.com/thekingoflorda/Red-DiscordBot/commit/bc309899c6dfe48be830502d22fad0269cbb5f02

<img width="265" alt="Screenshot 2024-06-27 at 20 01 08" src="https://github.com/thekingoflorda/Red-DiscordBot/assets/78911539/b2fc23c6-083d-45ae-8032-422d080ab15f">

In this image we see the result the branch coverage wrote to the branch_coverage_zenno.txt file, the last 2 are relevant for the get_prefix function, as we can see none of the branches get covered yet. 

## Coverage improvement

### Individual tests

Teammember: Luc

test_bank_set

https://github.com/thekingoflorda/Red-DiscordBot/commit/b037fa4fe0e9fe593ce0e1fdf4700504587e2108

Original:
![CleanShot 2024-06-22 at 12 10 20@2x](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/598a28f8-a010-4241-9fc3-774edf66a025)

New:
![CleanShot 2024-06-27 at 19 50 22@2x](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/ca02dd36-3dc0-417e-b379-5915b9087707)

With the original tests 3/6 conditional branches actually ran, my changes increased this by to 6/6.
I improved the coverage by adding a new set of tests that test different kind of input errors, like inputting a string, inputting a negative value and going above the maximum value.

test_bank_set

https://github.com/thekingoflorda/Red-DiscordBot/commit/998fed24ce393340d4945c54b9f4c3013065daec

Original:
![CleanShot 2024-06-22 at 12 10 20@2x](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/598a28f8-a010-4241-9fc3-774edf66a025)

New:
![CleanShot 2024-06-27 at 19 50 22@2x](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/c49ea789-a5a1-4b48-aa28-21d8caa29a06)

With the original tests 0/3 conditional branches where actually run, with the new tests 3/3 conditional branches where actually run.
I achieved this by inputting a float value, a negative number and trying to withdraw so much that the value of the bank account went under 0.

Teammember: Bram

test_get_account:

https://github.com/thekingoflorda/Red-DiscordBot/commit/368e7067e209c3c11689d88cc2a3c57047d0614d

![image](https://github.com/thekingoflorda/Red-DiscordBot/assets/122359361/0e13b602-0600-4096-8d41-25b5ccf24ec5)

![image](https://github.com/thekingoflorda/Red-DiscordBot/assets/122359361/2545c3d5-c4f9-47c0-b9b6-8437897b237d)

With the original tests 3/5 conditional branches ran, with my implemented changes this increased to 4/5.
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

After improving the coverage tool I have got the following results:

![image](https://github.com/thekingoflorda/Red-DiscordBot/assets/122359361/1105a680-45a4-4d05-b79e-0187586283eb)


Teammember: Zenno

Test 1: test_is_command

https://github.com/thekingoflorda/Red-DiscordBot/commit/c3ba787328cf46596c7434c20307b34415e18eec

<img width="265" alt="Screenshot 2024-06-27 at 20 01 08" src="https://github.com/thekingoflorda/Red-DiscordBot/assets/78911539/644c90ef-755b-4c83-9d30-52db318d5a38">

<img width="322" alt="Screenshot 2024-06-27 at 20 00 49" src="https://github.com/thekingoflorda/Red-DiscordBot/assets/78911539/5c21cc56-b4eb-4ab3-a1e7-833bd82b04eb">

With the original testing this function was not covered so I created a new test. My new tests increased this to 2/2 conditional branches ran. I achieved this improvement by simulating a bot object and its get_command method. By controlling the return value of get_command I was able to test all branches of the is_command function.

Test 2: test_get_prefix

https://github.com/thekingoflorda/Red-DiscordBot/commit/bc309899c6dfe48be830502d22fad0269cbb5f02

<img width="265" alt="Screenshot 2024-06-27 at 20 01 08" src="https://github.com/thekingoflorda/Red-DiscordBot/assets/78911539/d1d24158-ab87-4c09-aee8-8601148904e4">

<img width="322" alt="Screenshot 2024-06-27 at 20 00 49" src="https://github.com/thekingoflorda/Red-DiscordBot/assets/78911539/cb0969c5-f950-436e-8d18-d99995527f32">

With the original testing this function was not covered so I created a new test. My new tests increased this to 2/2 conditional branches ran. This was improved by creating a mock message with controlled content and a mock bot with a specific command prefix. By doing this I was able to test both the scenario where the message content starts with a prefix and the scenario where it does not, covering all branches of the get_prefix function.


### Overall

![CleanShot 2024-06-22 at 12 05 00@2x](https://github.com/thekingoflorda/Red-DiscordBot/assets/64592718/12137089-561f-4164-96a3-7ea73fb716e6)

After our improvements the relevant areas now looks like this:

Bram and Luc worked in bank.py:

![image](https://github.com/thekingoflorda/Red-DiscordBot/assets/122359361/16723ed4-ae1a-4eb9-afcc-4af06e5da363)

Ivan worked in test_trivia.py:

![image](https://github.com/thekingoflorda/Red-DiscordBot/assets/122359361/3ed0c9c0-673e-4c53-880b-604074c3b702)

Zenno worked in alias.py:

![image](https://github.com/thekingoflorda/Red-DiscordBot/assets/122359361/465b4a8f-94bb-4e11-ae5b-90217a13aca9)

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

Luc:
Forked the code and altered the github page to comply with the assignment requirements. 

Ivan:
Completed own part and tried to help others as mush as could.

Bram:
Completed own part and helped others when neccessary.

Zenno:
Completed own part of the assignment and tried to assist others where possible.


