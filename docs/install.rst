============
Installation
============

At the command line:

easy_install crawler

Or, if you have pip installed:

pip install crawler


   Hier kan irgendein Text stehen.
   Das kann auch eine sehr lange Textzeile sein die eigentlich zu lang zum lesen ist.

| so
| kann
| man 
| Zeilenumbrüche erstellen.

Bullet List:
        * Chapter 1

          - Unterkapitel 1

          - Unterkapitel 2

.. code-block:: python
   :linenos:

   from microbit import *

   x = 0
   for y in range(0, 5):
     display.set_pixel(x, y, 9)


.. _A cool website: http://sphinx-doc.org

Und hier nun eine url:
.. _http://www.ibm.com

  So kann man z.b besonderer Text hervorheben: ``soises`` würde der Deutsche Bundekanzler Anwärter 
  der in Baden-Würtenberg Minister Präsitent gewesen ist antworten. Eine `A cool website`_ sphinx.

  .. _A cool website: http://sphinx-doc.org

  
                A cool bit of code::

                        Hier steht dann irgendetwas

                .. code-block:: rst

                         A bit of **rst** which should be *highlighted* properly.


.. _reStructuredText: https://docutils.sourceforge.io/rst.html

.. compound::

   The 'rm' command is very dangerous.  If you are logged
   in as root and enter ::

       cd /
       rm -rf *

   you will erase the entire contents of your file system.

.. note::
        |        Beware ot the cat !
        |        or the Dog ?

.. contents::
        Machen wir mal Inhalt

---------------
 Section Title
---------------

*Section Title Wieso*
---------------------

-Section 2 Title Wieso-
-----------------------

Section 3 Title Wieso
---------------------

`````````````
Section Title
`````````````

`````````````
Section Title
`````````````

`````````````
Section Title
`````````````

Section Title
'''''''''''''

Section Title
'''''''''''''

Section Title
'''''''''''''
