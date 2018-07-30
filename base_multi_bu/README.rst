=====================================
   Business Unit Base Module
=====================================

This package is the base module introducing the concept of ``business_unit``.

A Business Unit (BU) is a new way of grouping users within a company around a set of business rules.

As such BUs are accessible to administrative users through the **Settings > Users** menu.
It is composed of the following elements:

* a single related company
* a single partner entry used as a place holder for name, email, address and such.
* an accounting journal

Users belonging to more than one BU will see a BU Switcher widget appear in the top menu bar. This widget will allow them to switch between BUs and thus change the set of rule governing their access to data.

Installation notes
==================

The base module comes with a ready for production implementation of BU support for Contact (internally known as **res_partners**). It allows you to assign a BU to any contact and restrict access to said contact to only members of the given BU.

If you do not want this feature active you will have to render inactive the **Res Partner multi-BU** rule in **Settings > Technical > Security > Record Rules**.

This implementation is given as a template of how you can apply BUs to your own custom module. Namely you will have to:

1. extend your model by adding a business_unit_id as a M2O

2. add the business_unit_id to the associated view

3. create a `ir.rule` to filter CRUD access to your model.


Credits
=======

Contributors
------------

* Valentin Thirion <valentin.thirion@abakusitsolutions.eu>
* Paul Ntabuye Butera <paul.n.butera@abakusitsolutions.eu>

Maintainer
-----------

.. image:: http://www.abakusitsolutions.eu/wp-content/themes/abakus/images/logo.gif
   :alt: AbAKUS IT SOLUTIONS
   :target: http://www.abakusitsolutions.eu

This module is maintained by AbAKUS IT SOLUTIONS
