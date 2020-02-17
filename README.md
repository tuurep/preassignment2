### Preassignment project

**Objectives:**

* Writing a minimalistic program focused on neat problem solving rather than using a lot of external dependencies
* Smart handling of data
* Display on an HTML interface

**Run locally:**

* Install Python 3
* Install pip
* `pip install bottle`
* `python app.py`
* Go to `http://localhost:8080/`

By default you will see the package data of my Ubuntu system as it was on 16.2.2020.

If you're on Debian/Ubuntu, you can use your own system's data by changing `input_file` on `app.py` to your local `/var/lib/dpkg/status` (text file).

**Publicly on the web:**

I'm hosting the app in an Amazon EC2 instance (AWS), which runs an Ubuntu 18.04 server. The python app is running on a [screen](https://www.gnu.org/software/screen/) session, so I don't need to be connected to the EC2 instance.

[Click here](http://ec2-13-48-30-59.eu-north-1.compute.amazonaws.com/) to see the app.
