# Acquisition
Overview
The purpose of this document is to provide a guide for those institutions that wish to migrate acquisition data from the current system to FOLIO. In general, the migration process consists of extracting, transforming, and importing those records that you will consider necessary on the FOLIO platform to continue working properly on the acquisition workflow process.

An EBSCO consultant can guide you for a correct migration according to the information you have in your current system.

The library acquisition migration team must decide which acquisition data would you like to migrate to FOLIO. (in the case that you have questions about which acquisition data can be migrated, in FOLIO you could migrate data such as vendors, funds, ledger, fiscal years, budgets, orders, and 

Recommendation before migrating Acquisition data
General recommendations that we suggest you before migrating acquisition data to FOLIO
Basic knowledge of FOLIO and current system key concepts and architecture about acquisitions. Further information: https://wiki.folio.org/display/RM/Acquisitions+Small+Group

FOLIO: Settings Related to Acquisitions Apps  (sharepoint) 
-  FOLIO: Setting Related to Acquisitions Apps (docs google)Backup. 
-  Before export acquisition data a backup must be taken by the library.
-  Normalize vendor's codes. Organizations(vendors) records cannot have the same ID or code. (not duplicated name or codes). Please check the strategy we have chosen when the migration team finds vendors with the same code on this document section. (General Key concept to Migrate Acquisition data.).
-  Clean up old/inconsistent data: do not export or remove purchase orders that are old tests or drafts; also, do not export or remove invoices that are old drafts or tests. (optional).
-  Clean-up orders have been inactive for years. (optional).

FINANCES. Clean-up budgets have been inactive for years. We recommend creating the fund's structure manually in FOLIO.

FISCAL YEAR:
-  Some questions that you should ask the clients:
-  What date could you stop editing vendor (organization) records on the current system?
-  What date could you stop new acquisitions on the current system?
-  What date could you stop updating/creating bibliographic data (inventory, holdings)?
-  Do they want to link the Purchase Order title with instance records in FOLIO?
-  What date could you extract the Acquisition data from your current system?

General Key concept to Migrate Acquisition data.


Organizations. 
The FOLIO vendor records must be stored in the organization application, the organization code must be unique then to ensure a unique organization code on migration, the migration will check if VENDOR_CODE is unique. The VENDOR_ID field will be appended to the org code or we will create a prefix or suffix string if needed. for example, for the supplier with the code: “1107601401”, we will create a new code 1107601401VENDOR_CODE or 110760140101; 110760140102,
It is possible to merge vendors that have the same vendor code in the current system into a single organization in FOLIO. If vendors are merged, vendor account information from all merged vendors will be stored in the organization account section but everything else is kept from the first vendor record found in the export file.

NOTE: Do you want to merge vendors? If yes, please check in which fields you want storage vendor account information and come to an agreement with the FOLIO implementing consultant. 


