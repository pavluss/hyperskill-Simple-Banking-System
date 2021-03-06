# Simple Banking System
<h1>TASK 1</h1>
<h2>Description</h2>

<p>We live busy lives these days. Between work, chores, and other things in our to-do lists, it can be tough to catch your breath and stay calm. Credit cards are one of the things that save us time, energy, and nerves. From not having to carry a wallet full of cash to consumer protection, cards make our lives easier in many ways. In this project, you will develop a simple banking system with a database.</p>

<p>If you’re curious about business, technology, or how things around you work, you'll probably enjoy learning how credit card numbers work. These numbers ensure easy payments, and they also help prevent payment errors and fraud. Card numbers are evolving, and they might look different in the near future.</p>

<p>Let's take a look at the anatomy of a credit card:</p>

<p style="text-align: center;"><img alt="" height="409" src="https://lh3.googleusercontent.com/ZgkQv6hMeNkbBrSeSsnb2t6GLkawQFKJNaXapTAaFmy-WPWPPtFp5MpnvlzSFzn3R-0zAvOEUriCg6bGeX_stXdG8L0WSeASnwvqFLLFyeQO4JcbfH4yjh2QdHBEdQyZy2k72q4V" width="602"></p>

<p>The very first digit is the <strong>Major Industry Identifier (MII),</strong> which tells you what sort of institution issued the card.</p>

<ul>
	<li>1 and 2 are issued by airlines</li>
	<li>3 is issued by travel and entertainment</li>
	<li>4 and 5 are issued by banking and financial institutions</li>
	<li>6 is issued by merchandising and banking</li>
	<li>7 is issued by petroleum companies</li>
	<li>8 is issued by telecommunications companies</li>
	<li>9 is issued by national assignment</li>
</ul>

<p>In our banking system, credit cards should begin with 4.</p>

<p>The first six digits are the <strong>Issuer Identification Number (IIN)</strong>. These can be used to look up where the card originated from. If you have access to a list that provides detail on who owns each IIN, you can see who issued the card just by reading the card number.</p>

<p>Here are a few you might recognize:</p>

<ul>
	<li>Visa: 4*****</li>
	<li>American Express (AMEX): 34**** or 37****</li>
	<li>Mastercard: 51**** to 55****</li>
</ul>

<p>In our banking system, the IIN must be 400000.</p>

<p>The seventh digit to the second-to-last digit is the <strong>customer account number</strong>. Most companies use just 9 digits for the account numbers, but it’s possible to use up to 12. This means that using the current algorithm for credit cards, the world can issue about a trillion cards before it has to change the system.</p>

<p>We often see 16-digit credit card numbers today, but it’s possible to issue a card with up to 19 digits using the current system. In the future, we may see longer numbers becoming more common.</p>

<p>In our banking system, the customer account number<strong> </strong>can be any, but it should be unique. And the whole card number should be 16-digit length.</p>

<p>The very last digit of a credit card is the<strong> check digit</strong> or <strong>checksum</strong>. It is used to validate the credit card number using the Luhn algorithm, which we will explain in the next stage of this project. For now, the checksum can be any digit you like.</p>

<h2>Objectives</h2>

<p>You should allow customers to create a new account in our banking system.</p>

<p>Once the program starts, you should print the menu: </p>

<pre><code class="language-no-highlight">1. Create an account
2. Log into account
0. Exit</code></pre>

<p>If the customer chooses ‘Create an account’, you should generate a new card number which satisfies all the conditions described above. Then you should generate a PIN code that belongs to the generated card number. A PIN code is a sequence of any 4 digits. PIN should be generated in a range from 0000 to 9999.</p>

<p>If the customer chooses ‘Log into account’, you should ask them to enter their card information. Your program should store all generated data until it is terminated so that a user is able to log into any of the created accounts by a card number and its pin. You can use an array to store the information.</p>

<p>After all information is entered correctly, you should allow the user to check the account balance; right after creating the account, the balance should be 0. It should also be possible to log out of the account and exit the program.</p>



<h1>TASK 2</h1>
<h2>Description    </h2>

<p>In this stage, we will find out what the purpose of the checksum is and what the Luhn algorithm is used for.</p>

<p>The main purpose of the check digit is to verify that the card number is valid. Say you're buying something online, and you type in your credit card number incorrectly by accidentally swapping two digits, which is one of the most common errors. When the website looks at the number you've entered and applies the Luhn algorithm to the first 15 digits, the result won't match the 16th digit on the number you entered. The computer knows the number is invalid, and it knows the number will be rejected if it tries to submit the purchase for approval, so you're asked to re-enter the number. Another purpose of the check digit is to catch clumsy attempts to create fake credit card numbers. Those who are familiar with the Luhn algorithm, however, could get past this particular security measure.</p>

<p><strong>Luhn Algorithm in action</strong></p>

<p>The Luhn algorithm is used to validate a credit card number or other identifying numbers, such as Social Security. The Luhn algorithm, also called the Luhn formula or modulus 10, checks the sum of the digits in the card number and checks whether the sum matches the expected result or if there is an error in the number sequence. After working through the algorithm, if the total modulus 10 equals zero, then the number is valid according to the Luhn method.</p>

<p>While the algorithm can be used to verify other identification numbers, it is usually associated with credit card verification. The algorithm works for all major credit cards.</p>

<p>Here is how it works for a credit card with the number 4000008449433403:</p>

<p><img alt="" src="https://ucarecdn.com/b2ca8ed0-d7ec-4d72-9043-f60ba6a6cd8b/"></p>

<p> </p>

<p>If the received number is divisible by 10 with the remainder equal to zero, then this number is valid; otherwise, the card number is not valid. When registering in your banking system, you should generate cards with numbers that are checked by the Luhn algorithm. You know how to check the card for validity. But how do you generate a card number so that it passes the validation test? It's very simple!</p>

<p>First, we need to generate an Account Identifier, which is unique to each card. Then we need to assign the Account Identifier to our BIN (Bank Identification Number). As a result, we get a 15-digit number 400000844943340, so we only have to generate the last digit, which is a checksum. </p>

<p>To find the checksum, it is necessary to find the control number for 400000844943340 by the Luhn algorithm. It equals 57 (from the example above). The final check digit of the generated map is <code class="java">57+X</code>, where <code class="java">X</code> is checksum. In order for the final card number to pass the validity check, the check number must be a multiple of 10, so <code class="java">57+X</code> must be a multiple of 10. The only number that satisfies this condition is 3. </p>

<p>Therefore, the checksum is 3. So the total number of the generated card is 4000008449433403. The received card is checked by the Luhn algorithm.</p>

<p>You need to change the credit card generation algorithm so that they pass the Luhn algorithm.</p>

<h2>Objectives</h2>

<p>You should allow customers to create a new account in our banking system.</p>

<p>Once the program starts you should print the menu: </p>

<p>1. Create an account<br>
2. Log into the account<br>
0. Exit</p>

<p>If the customer chooses ‘Create an account’, you should generate a new card number that satisfies all the conditions described above. Then you should generate a PIN code that belongs to the generated card number. PIN is a sequence of 4 digits; it should be generated in the range from 0000 to 9999.</p>

<p>If the customer chooses ‘Log into account’, you should ask to enter card information.</p>

<p>After the information has been entered correctly, you should allow the user to check the account balance; after creating the account, the balance should be 0. It should also be possible to log out of the account and exit the program.</p>


<h1>TASK 3</h1>
<h2> Description</h2>

<p>It's very upsetting when the data about registered users disappears after the program is completed. To avoid this problem, you need to create a database where you will store all the necessary information about the created credit cards. We will use SQLite to create the database.</p>

<p>SQLite is a database engine. It is a software that allows users to interact with a relational database. In SQLite, a database is stored in a single file — a trait that distinguishes it from other database engines. This allows for greater accessibility: copying a database is no more complicated than copying the file that stores the data, and sharing a database implies just sending an email attachment.</p>

<p>You can use the <code class="language-java">sqlite3</code> module to manage SQLite database from Python. You don't need to install this module. It is included in the standard library.</p>

<p>To use the module, you must first create a <code class="language-java">Connection</code> object that represents the database. Here the data will be stored in the <code class="language-java">example.s3db</code> file:</p>

<pre><code class="language-java">import sqlite3
conn = sqlite3.connect('example.s3db')</code></pre>

<p>Once you have a <code class="language-java">Connection</code>, you can create a <code class="language-java">Cursor</code> object and call its <code class="language-java">execute()</code> method to perform SQL queries:</p>

<pre><code class="language-python">cur = conn.cursor()

# Executes some SQL query
cur.execute('SOME SQL QUERY')

# After doing some changes in DB don't forget to commit them!
conn.commit()</code></pre>

<p>To get data returned by SELECT query you can use <code class="language-java">fetchone()</code>, <code class="language-java">fetchall()</code> methods:</p>

<pre><code class="language-python">cur.execute('SOME SELECT QUERY')

# Returns the first row from the response
cur.fetchone()

# Returns all rows from the response
cur.fetchall()</code></pre>

<h2>Objectives</h2>

<p>In this stage, create a database named <code class="language-java">card.s3db</code> with a table titled <code class="language-java">card</code>. It should have the following columns:</p>

<ul>
	<li>id INTEGER</li>
	<li>number TEXT</li>
	<li>pin TEXT</li>
	<li>balance INTEGER DEFAULT 0</li>
</ul>

<p>Pay attention: your database file should be created when the program starts if it hasn’t yet been created. And all created cards should be stored in the database from now.</p>

<p><div class="alert alert-primary">Do not forget to commit your DB changes right after executing a query!</div></p>

<h1>TASK 4</h1>
<h2>Description</h2>

<p>You have created the foundation of our banking system. Now let's take the opportunity to deposit money into an account, make transfers and close an account if necessary.</p>

<p>Now your menu should look like this:</p>

<pre><code class="language-no-highlight">1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit</code></pre>

<p>If the user asks for <code class="java">Balance</code>, you should read the balance of the account from the database and output it into the console.</p>

<p><code class="java">Add income</code> item should allow us to deposit money to the account.</p>

<p><code class="java">Do transfer</code> item should allow transferring money to another account. You should handle the following errors:</p>

<ul>
	<li>If the user tries to transfer more money than he/she has, output: <code class="java">Not enough money!</code></li>
	<li>If the user tries to transfer money to the same account, output the following message: <code class="java">You can't transfer money to the same account!</code></li>
	<li>If the receiver's card number doesn’t pass the Luhn algorithm, you should output: <code class="java">Probably you made a mistake in the card number. Please try again!</code></li>
	<li>If the receiver's card number doesn’t exist, you should output: <code class="java">Such a card does not exist.</code></li>
	<li>If there is no error, ask the user how much money they want to transfer and make the transaction.</li>
</ul>

<p>If the user chooses the <code class="java">Close account</code> item, you should delete that account from the database.</p>

<p><div class="alert alert-primary">Do not forget to commit your DB changes right after executing a query!</div></p>


