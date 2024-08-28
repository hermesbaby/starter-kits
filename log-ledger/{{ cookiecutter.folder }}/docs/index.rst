.. _doc_root:

Biomech - Software-Architektur-Design-Dokumentation ++
######################################################

.. toctree-only::
    :maxdepth: 2
    :hidden:

    00-Project-Manual/index
    01-Introduction-and-Goals/index
    02-Constraints/index
    03-Context-and-Scope/index
    04-Solution-Strategy/index
    05-Building-Block-View/index
    06-Runtime-View/index
    07-Deployment-View/index
    08-Crosscutting-Concepts/index
    09-Architectural-Decisions/index
    10-Quality-Scenarios/index
    11-Risks-and-Technical-Debt/index
    12-Glossary/index
    13-Component-Designs/index
    14-Engineering-Notebooks/index
    15-Meeting-Minutes/index
    16-Workflow-and-Collaboration/index
    99-Appendix/index
    html: genindex


Aktuelle Feinplanung
********************

.. uml:: 00-Project-Manual/_figures/feinplanung_24CW33_24CW39.gant
    :caption: :ref:`fig_feinplanung_24CW33_24CW39`
    :scale: 75%


Quicklinks
**********

`Project Activity <https://jira.vitronic.de/projects/PJBIO/summary>`__

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| JIRA / Planung und Verfolgung von Aufgaben:                                                                                                                                                                                   | JIRA / Definierende Inhalte:                                                                                                                            |
+===============================================================================================================================================================================================================================+=========================================================================================================================================================+
|| - `BigPicture <https://jira.vitronic.de/plugins/servlet/softwareplant-bigpicture/#/box/UB-348/g>`__ (Zeitplan als GANTT-Diagramm)                                                                                            || - `Stakeholder Requirements <https://jira.vitronic.de/plugins/servlet/com.easesolutions.jira.plugins.requirements/project?detail=PJBIO&folderId=40>`__ |
|| - Kanban-Board `Backend/Gui <https://jira.vitronic.de/secure/RapidBoard.jspa?rapidView=964#>`__                                                                                                                              || - `HW-Spezifikationen <https://jira.vitronic.de/browse/PJBIO-508?filter=31145>`__                                                                      |
|| - Kanban-Board `Recon/Model/Measure <https://jira.vitronic.de/secure/RapidBoard.jspa?rapidView=928#>`__                                                                                                                      || - `SW-Spezifikationen <https://jira.vitronic.de/browse/PJBIO-507?filter=30658>`__                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| `OneNote <onenote:///\\\\ntserver1\\Buero\\Projekt\\10xxxx\\1055xx\\105524-DE\\11_Documentation\C_OneNote\\Allgemein.one#section-id={B8F365C4-5616-4F23-8F0B-ACADC4AD39ED}&end>`__ (Projekt-Dokumentation der Projektleitung) |                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| `Projektordner auf NTSERVER1 <file://///NTSERVER1/Buero/Projekt/10xxxx/1055xx/105524-DE>`__                                                                                                                                   |                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

Die Inhalte dieses Dokumentes zusammen mit den obigen Quellen bilden die **Gesamtheit der Software-Entwicklungs-Dokumentation** des Projektes [#this-doc]_:


Orientierungshilfen
*******************

- :ref:`sec_readers_guide` [#readers]_
- :ref:`sec_writers_guide`


Nutzung und Weitergabe
**********************

.. attention::

    Die Inhalte dieses Dokumentes haben die |conf_confidential_level| [#confi-level]_ und dienen in erster Linie zur Kommunikation zwischen den :ref:`am Projekt beteiligten Personen <sec_project_participants>`.

    Bei Interesse, Inhalte anderweitig zu verwenden oder davon abzuleiten, stimme Dich vorher mit jemandem aus dem :ref:`Software-Team <sec_software_team>` ab.


.. rubric: Fußnoten

.. [#readers] Der Leserkreis ist durch die Zugriffsregelung auf dieses Dokument eingeschränkt. Im Anhang unter :ref:`sec_access_to_published_document` ist der aktuelle Leserkreis aufgeführt.

.. [#this-doc] Dieses Dokument ist Teil des Projekts "105524-DE (3D Bodyscan)" mit dem Arbeitstitel :term:`Biomech`. Der Hauptbestandteil ist die Software-Architektur-Design-Dokumentation (:term:`SWADD`), wobei es auch Inhalte umfasst, die eine klassische :term:`SWADD` übersteigt (deshalb das "++" im Titel). Weitere Infos zum Inhalt und der Struktur sind im :ref:`sec_readers_guide` zu finden.

.. [#confi-level] Siehe `AA Vertraulichkeitsstufen von Information <https://wiki.vitronic.de/index.php/AA_Vertraulichkeitsstufen_von_Information_/_WI_Confidentiality_levels_of_information>`__
