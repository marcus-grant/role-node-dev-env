Notes (TO BE MOVED TO NOTES OR DOCUMENTATION)
=============================================

Init the Project
----------------

Easy enough, just use the molecule app with command `init` like below:

```sh
molecule init role -r role-node-dev-env
```

### Molecule Scenarios

Molecule creates a folder called `molecule` within the role base project filetree that stores all of the functionality molecule uses on this project. Molecule uses the concept of [scenarios][02] which are a top-level configuration syntax that stores a single set of testing configurations that can be customized. The `init` command creates a single scenario `default` inside the molecule directory that has the default testing configs.


### Scenario Layouts

The default scenario has a number of root files and directories:

```sh
ls
defaults  handlers  meta  molecule  README.md  tasks  vars
```

- Docker is the default **driver**, *i.e. the system used for testing which could also be Vagrant for example*, and it's a Jinja template allowing to use ansible variables to template the dockerfile.
- `INSTALL.rst` are instruction on any additional software or scripting needed to have this scenario's driver interface correctly with the role.
- `molecule`.yml is the configuration entrypoint for the scenario, it gets used to configure each tool molecule uses when testing the role.
- `playbook.yml` is the playbook file that gets called to test the role, it will look like any regular playbook but tuned for testing.
- `tests` is the testing directory that is a part of [TestInfra][03] which is the default [Verifier][04]. Verifiers are a molecule concept that gets used for setting up test verifications after executing the role.


### molecule.yml

The `molecule.yml` file is for configuring Molecule. It's a YAML file where the keys represent high level components/modules that Molecule provides and their different properties. These include:

- The [Dependency][05] manager for the role. This just defines already developed roles that this one depends on, which by default is handled by [Ansible Galaxy][06], but it could also be a custom repository
- The [Driver][07] provider defines the testing system driver, by default it's Docker. There are plenty others as well including cloud IaaS providers like Azure, EC2, GCE, and Digital Ocean.
- The [Lint][08] provider, which is by default YAMLLint, it's used to standardize the linting rules for anyone developing this role and to help individual developers write more clean and well functioning roles.
- The [Platform][09] definitions, which specifies to molecule which instances to create, names them, and groups them. Useful particularly if the role needs to work on multiple OSs, distributions or environments.
- The [Scenario][10] is used to specify parameters and the sequencing of the scenario's tests.
- The [Verifier][11] framework specifications that is used to define what the expected results of this role should be and verifies that's what they are. By default [TestInfra][03] is the framework used.


References
----------

1. [Molecule Documentation: Getting Started][01]
2. [Molecule Documentation: Scenarios][02]
3. [TestInfra Documentation: Overview][03]
4. [Molecule Documentation: Verifier][04]
5. [Molecule Documentation: Dependency][05]
6. [Ansible Documentation: Ansible Galaxy][06]
7. [Molecule Documentation: Driver][07]
8. [Molecule Documentation: Lint][08]
9. [Molecule Documentation: Platforms][09]
10. [Molecule Documentation: Scenario][10]


[01]: https://molecule.readthedocs.io/en/stable/getting-started.html "Molecule Documentation: Getting Started"
[02]: https://molecule.readthedocs.io/en/stable/configuration.html#root-scenario "Molecule Documentation: Scenarios"
[03]: https://testinfra.readthedocs.io/en/latest/index.html "TestInfra Documentation: Overview"
[04]: https://molecule.readthedocs.io/en/stable/configuration.html#verifier "Molecule Documentation: Verifier"
[05]: https://molecule.readthedocs.io/en/stable/configuration.html#dependency "Molecule Documentation: Dependency"
[06]: https://docs.ansible.com/ansible/latest/reference_appendices/galaxy.html "Ansible Documentation: Ansible Galaxy"
[07]: https://molecule.readthedocs.io/en/stable/configuration.html#driver "Molecule Documentation: Driver"
[08]: https://molecule.readthedocs.io/en/stable/configuration.html#linters "Molecule Documentation: Lint"
[09]: https://molecule.readthedocs.io/en/stable/configuration.html#platforms "Molecule Documentation: Platforms"
[10]: https://molecule.readthedocs.io/en/stable/configuration.html#root-scenario "Molecule Documentation: Scenario"


Role Name
=========

A brief description of the role goes here.





Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should
be mentioned here. For instance, if the role uses the EC2 module, it may be a
good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including
any variables that are in defaults/main.yml, vars/main.yml, and any variables
that can/should be set via parameters to the role. Any variables that are read
from other roles and/or the global scope (ie. hostvars, group vars, etc.) should
be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in
regards to parameters that may need to be set for other roles, or variables that
are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: role-node-dev-env, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).
