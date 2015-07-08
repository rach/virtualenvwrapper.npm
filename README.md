##Npm plugin for virtualenvwrapper

###Install 

    pip install virtualenvwrapper.npm

###How it works

After activating a virtual environment any npm intalled will be inserted inside the active virtual env and the binary will be accessible via the PATH.
Inside the virtual env, the config is setup to install the package as global mode by default

###Example


    mkvirtualenv test
    workon test #if not already inside
    npm install -g gulp
    which gulp #> $VIRTUAL_ENV/bin/gulp

