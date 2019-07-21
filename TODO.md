To Do's
=======

In Progress
-----------

- [ ] Check if nvm is already installed and setup
- [ ] Create the NVM's directory if it doesn't already exist
    - Use $NVM_DIR to create the directory

Planned
-------

Future
------
- [ ] Detect if `$NVM_DIR` already exists & if it does don't set $NVM_DIR
    - Will be used to determine the ansible var `nvm_dir` should be used
    - `nvm_dir` should default to `$HOME/.nvm`
    - unfortunately the docker provider of molecule pulls all host environment vars
        - return and test it with ansible `nvm_dir` var setting an empty `$NVM_DIR`


Completed
---------