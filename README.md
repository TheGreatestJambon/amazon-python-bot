# amazon-python-bot
This is a rudimentary python3 bot created within the PyCharm IDE, which is designed to take a product URL, max price and sign in details and check out the PS5 (Or other products) when it becomes available.

Why is it rudimentary?

The main difference between a bot like this and a premium retail bot which you would pay for is the use of proxy switching/user agent switching. Utilising these methods would mean you could run a bot constantly if you so desired, without risk of your IP being banned. However, proxies (which work) cost money, therefore this bot is only automated as long as you activate it yourself.

How would I know when to activate the bot?

There are certain discord/social media groups which have supplier insider information about the potential timing of drops, a popular choice being the PS5StockAlertUK Twitter or Discord. So within a couple minutes of the potential drop, you can activate the bot and not need to worry about your IP potentially being banned due to excessive page refreshing. To be honest I haven't heard being banned for this reason on Amazon is a big problem anyway, but you have been warned.

Why can't I start the bot after signing in manually, to save time?

The API used to remotely control the firefox browser creates a new session every time it launches, think like a incognito browser session. Therefore login details would not be stored from use to use. However, even if this was a possibility, once you are signed in there is no hiding your identity through proxy switching or messing with the session cookies. Therefore, you may end up getting IP banned.

How does the bot work?

The bot uses the Selenium API to remotely control a Firefox browser session. It also uses Tkinter for the API. On launch, a window will appear for you to specify the product URL, a max price, alongside your user details. These details are only temporariy stored within global variables, before being cleared on program exit. On submitting your details, the product page will load. The bot is looking for one of two things, either a buy now button or a 'see all buying options' button. The latter is because on previous ps5 drops, the product has been held within this area. The max price functionality stops the bot from clicking through on any product that is being resold at scalper price for example (GPUs). If the item is out of stock, or the price is too high, then the bot will refresh the page. Rinse and repeat. If the product is available, the bot will proceed through to the sign in page, enter your details and then proceed to checkout. Amazon makes it easy to store both payment and delivery specifics, so be sure these are filled in beforehand. Finally, the bot will checkout.

A few things to note...

If you enter a URL that is not an Amazon product page, the program will terminate and a console log will notify you.
If you enter an incorrect user or password, the program will also terminate.
Try not to mess with the wait time variable, as setting it too low could cause the program to fail due to an element being looked for on the next page before it has loaded. You have been warned.
Firefox will instantly recognise that the browser is being remotely controlled. Like I said before, unless you want to purchase and incorporate premium proxies, this is inevitable. Don't worry however, this will not lead to you getting banned on Amazon itself.

Enjoy!

Props to JahkRCode.
