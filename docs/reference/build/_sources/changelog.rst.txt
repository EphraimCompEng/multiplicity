.. change_log:
=========
Changelog
=========

.. toctree::
    v0.3
    v0.2
    v0.1


.. _v0.3:
v0.3
=====

`v0.3.0 <https://github.com/EphraimCompEng/multiplied/releases/tag/v0.3.0>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Updates:

    - Secured multiplied on PyPi, test.PyPi and github
    - Assisted algorithm generation via patterns (not true automation)
    - Finalised structure and populated an Algorithm stage `#18 <https://github.com/EphraimCompEng/multiplied/issues/18>`_
    - Expanded mp.pretty formatting to all Multiplied types
    - Added to utils.char.py to clean up template generation
    - Generate templates from patterns using existing matrix

    Plus smaller bug fixes and improvements

Looking forward:

    [Main Focus]

    - Automatic algorithm generation via patterns
    - Applying algorithms to operands
    - Truth table generation via algorithm(s)

    [ Ongoing ]

    - Prepare for complex, custom, templates
    - Export to .parquet files
    - Continued development of the API reference site


.. _v0.2:
v0.2
====


`v0.2.0 <https://github.com/EphraimCompEng/multiplied/releases/tag/v0.2.0>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Updates:

    - API reference site complete and ready for population
    - Changed API ref theme to `breeze <https://github.com/aksiome/breeze>`_
    - Initial implementation for all algorithm related classes
    - Improved interoperability between classes
    - Resolve and produce rmaps for basic templates/matrices

Looking forward:

    [Main Focus]

    - Implement algorithms via built-in templates
    - Prepare for complex, custom, templates
    - Design ways to assist algorithm creation

    [ Ongoing ]

    - Implement exporting to parquet files
    - Continued development of the API reference site

.. _v0.1:
v0.1
====



`v0.1.1 <https://github.com/EphraimCompEng/multiplied/releases/tag/v0.1.1>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This patch is focused on documentation and testing the api reference site locally

Updates:

    - progress towards an online api reference site
    - Improved landing page and overall site layout
    - Scripts apidoc.sh and build.sh to automate syncing and creating the sphinx site
    - Added sphinx-rtd-theme
    - minimal additions to codebase, mostly outlining future functionality



`v0.1.0 <https://github.com/EphraimCompEng/multiplied/releases/tag/v0.1.0>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This release is a complete refactor of the original script, widening it's scope and turning it into a library.

Added:

    - Classes and a general focus on code reuse
    - Reduction templates for CSA and Adders
    - Initial Documentation

TODO:

    - Documentation and template implementation

For more info on future goals, check out the `roadmap <https://github.com/EphraimCompEng/multiplied/blob/master/ROADMAP.md>`_.
