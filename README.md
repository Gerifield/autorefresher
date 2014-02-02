AutoRefresher
=============

Everybody know what LiveReload is. This stuff is bit similar, but with multiple tools.
The project contains a Sublime Text plugin (tested with ST3), a Greasmonkey script (tested with Tampermonkey) and a small python server.

Background
----------
I like to learn new things and this project increased my Python, WebSocket and Sublime Text plugin skills. :)

The `AutoRefresher_server.py` starts two servers:
- WebSocket on port `9998`
- HTTP server on port `9999`

Every GET request to the HTTP server's `/refresh` page would send a `refresh` message to every clients on the WebSocket.
If you want, you could connect with multiple pages to the WebSocket and you could send get requests from everywhere.

The Greasemonkey script just opens a WebSocket and everytime it gets a `refresh` message it reloads the page.

The ST3 plugin just sends an HTTP request to the HTTP server.


That's all. :)



Installation
------------
1. Install the browser script and disable it! (It's necessary to disable and only enable on the pages you want to reload.)
2. Install the ST3 plugin.
3. Start the `AutoRefresher_Server.py` server.
4. Enable the "enabled" parameter to "true" tin the `AutoRefresher.sublime-settings`
5. PROFIT! :)


Everytime you save somethin in the editor, the page'll reload.


Credits
=======

Thanks to [opiate]{https://github.com/opiate} for the [Python SimpleWebSocketServer]{https://github.com/opiate/SimpleWebSocketServer}
[Tampermonkey]{https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo} plugin for Chrome
[Sublime Text 3]{http://www.sublimetext.com/3}