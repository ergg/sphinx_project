Installation

At the command line:

easy_install crawler

Or, if you have pip installed:

pip install crawler




Heading
=======

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

Und hier nun eine url:
.. _http://www.ibm.com

.. oder das: 

   *Hervorhebung*

   **strong Hervorhebung**

        .. class="highlights"
           Der Text ist hervorgehoben
           komplett ?

.. _reStructuredText: https://docutils.sourceforge.io/rst.html

