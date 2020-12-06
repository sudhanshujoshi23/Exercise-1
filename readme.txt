API:

1) http://127.0.0.1:5000/register -- Use for registering to the web-application. All the users registering from the domain of sapient.com will be the admin user and all others will be non-admin users.

2) http://127.0.0.1:5000/login -- Used for logging in to the web-application.

3) http://127.0.0.1:5000/Funds -- List of all the funds. This can be viewed by all the logged in user irrespective of their roles.

4) http://127.0.0.1:5000/Fund/New -- Add new funds. Can be accessed by only admin users.

5) http://127.0.0.1:5000/Fund/{int: FundID}/update -- Update the details of a particular fund. Can be accessed by admin users only.

6) http://127.0.0.1:5000/Investors -- List of all the investors along with their total investment. This can be viewed by all the logged in user irrespective of their roles.

7) http://127.0.0.1:5000/Investor/New -- Create a new investor. Can be accessed by only admin users.

8) http://127.0.0.1:5000/Investor/1/update -- Edit the details of an existing investor. Can be accessed by admin users only.

9) http://127.0.0.1:5000/AddInvestment -- Add a new investment for an investor. Can be accessed by only admin users.

10) http://127.0.0.1:5000/login -- Logout the current user. 

