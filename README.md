This exists solely as a convenient way to share this code with the AppDynamics team.

The bug in question is the inability for async http requests to show up in a drill down
view through the AppD interface.

Get Setup
=========

- Open bash/zsh (assuming you are running this on *nix. Let me know otherwise)
- Run the following commands

        $ git clone https://github.com/brianmego/app_dynamics_async_bug.git
        $ cd app_dynamics_async_bug

Non AppD Testing
================

        $ make run

This should allow you to download the dependencies and start the server running. By default
this runs on port 2000. That means, after it's running, you can navigate to
http://localhost:2000/sync and http://localhost:2000/async in a browser and
see the results.

Both result in the same response, but the async one uses python's asyncio framework
to run the requests.get call in the background.


With AppD
=========

If you drop an appdynamic config file into appd.config at the root of the repo, you can then run

        $ make run_with_appd

This should run the server while communicating with App Dynamics. After generating some traffic,
you should see /sync shows the full trace of the requests call, while /async simply shows
a line like EpollSelector::select - python3.6/selectors.py:428 - 350ms with no http drill
down information.

