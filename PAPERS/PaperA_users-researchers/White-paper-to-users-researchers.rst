**************************************************
White paper to users, researchers and facilitators
**************************************************

Beginner-friendly communication for users/researchers/facilitators
===================================================================

:Authors:
 Anna Alber,\ :sup:`1`
 Joseph Creech,\ :sup:`2`
 Raffaella D'Auria,\ :sup:`3`
 Lev Gorenstein,\ :sup:`4`
 Manasvita Joshi,\ :sup:`5`
 Ian Kaufman,\ :sup:`6`
 Geoffrey Lentner,\ :sup:`7`
 Bryan Raney,\ :sup:`8`
 Aldo Romero,\ :sup:`9`
 William Warriner\ :sup:`10`

 :sup:`1` Chapman University;
 :sup:`2` George Washington University;
 :sup:`3` OARC/IDRE - University of California, Los Angeles;
 :sup:`4` Globus - University of Chicago;
 :sup:`5` Harvard University;
 :sup:`6` University of California, San Diego;
 :sup:`7` Purdue University;
 :sup:`8` Rice University;
 :sup:`9` West Virginia University;
 :sup:`10` University of Alabama at Birmingham.

:Version: 1.0
:Date: 2025-12-XX

.. attention:: NB to change actual date


Executive Summary
-----------------

Motivation
^^^^^^^^^^

In the spring of 2024 `Anaconda Inc. <https://www.anaconda.com/>`__ announced a major change in their `Terms of Service <https://web.archive.org/web/20240808124157/https://legal.anaconda.com/policies/en/>`__ governing the use of Anaconda-provided tools and software packages in educational settings. According to this update, which became effective in March 30, 2024:

    Educational Entities will be exempt from the paid license requirement, provided that the use of the Anaconda Offering(s) is solely limited to being used for a curriculum-based course. [#f1]_


The scope and nature of expected changes appeared to be affecting many academic research users and organizations, which led to creation of the `CaRCC Anaconda Transition Working Group <https://carcc.org/anaconda-transition-working-group/>`__ to analyze potential threats and workarounds. This paper is a product of the Working Group.

After the `CaRCC Anaconda Transition Working Group <https://carcc.org/anaconda-transition-working-group/>`__ expressed concerns with representatives from `Anaconda Inc. <https://www.anaconda.com/>`__  an `update on the ToS for academic and research use <https://www.anaconda.com/blog/update-on-anacondas-terms-of-service-for-academia-and-research>`__ was published in September 18, 2024. According to this update `conda <https://github.com/conda/governance>`__ and its ecosystem are fully open source, free for everyone, and governed independently of Anaconda Inc., though universities cannot mirror Anaconda servers without a license. The Community Repository on `anaconda.org <https://anaconda.org>`__ is free to use for installing and updating packages from community channels like conda-forge, but certain mirrored channels (main, r, msys2, anaconda) remain subject to `Anaconda’s Terms of Service <https://www.anaconda.com/legal/terms/terms-of-service>`__. The Anaconda Repository at `repo.anaconda.com <https://repo.anaconda.com/>`__ is also free for individuals, universities, and companies with fewer than 200 employees, but larger non-academic organizations—including research institutions and national labs—must obtain a license to use it.


.. admonition:: Is Anaconda still free?

          - Conda is and will always be free, but when choosing an installer and when subsequently downloading, installing, using or updating packages, users need to know the terms of service that apply to each installer and where those packages are hosted to determine if their use is free, as described in the guidelines above. 
          - If packages are hosted in community channels such as conda-forge, you can use all packages for free, provided you use Miniconda or any non-Anaconda installer such as Miniforge. (subject to the mirrored channels exception mentioned in guideline 2)
          - If a package is hosted in Anaconda channels, you can use conda for free, but downloading, installing, using and updating those packages may require a commercial fee license, which means:
              * The distribution of packages Anaconda builds and maintains remains free for individuals and small organizations, which is defined in the Terms of Service as having less than 200 employees or contractors. 
              * A paid license is required for large organizations, which is defined in the Terms of Service as having more than 200 employees or contractors. 
              * Anaconda is free for all educational entities—even those with 200 or more employees or contractors—when used in a course curriculum, including teaching, learning, and researching, at accredited universities worldwide. 
              * A paid license is always required for any individual or entity—even an educational entity—that is embedding, mirroring, or providing third parties access to our products. If you’re interested in pursuing an embedded use case, please contact our partner team at partnerships@anaconda.com. See the `Anaconda Terms of Service <https://anaconda.com/legal>`__ for details.

           -- Excerpt from: “Terms of Services Info.” Anaconda, Published: March 17, 2025. https://www.anaconda.com/pricing/terms-of-service-faqs. Accessed: May 9, 2025. Available at: https://web.archive.org/web/20250506034856/https://www.anaconda.com/web/20250506034856/https://www.anaconda.com/pricing/terms-of-service-faqs.

Note that the statement: “A paid license is always required for any individual or entity—even an educational entity—that is embedding, mirroring, or providing third parties access to our products” is problematic for research facilitators who maintain software in centralized locations as by performing central installations they may be considered providing third-party access to Anaconda products or by creating containers and sharing them on public archives they may be considered embedding the software. Moreover, the possibility of further changes in the ToS complicate the issue.

.. attention:: In https://www.anaconda.com/blog/update-on-anacondas-terms-of-service-for-academia-and-research:
	       **Does Anaconda require academic entities with 200 or more employees to purchase a business or enterprise license?**

	       No. Anaconda does not require academic institutions and universities to purchase a commercial fee license for our installers or for access to our package repository, regardless of their size, when used in course curricula. We maintain a free-use policy for educational entities when Anaconda is used in course curricula, including teaching, learning, and research at accredited educational institutions worldwide. This free-use policy applies even to large universities with 200 or more employees. The 200-employee threshold for paid licenses primarily applies to commercial organizations. **However, it’s important to note that paid licenses may be required for specific use cases within academic settings, such as embedding Anaconda’s products, mirroring them, or providing third-party access beyond standard educational use.**


Anaconda Inc. eventually published an Academic Policy with an effective date of July 14, 2025 (https://www.anaconda.com/legal/terms/academic also available at: https://web.archive.org/web/20250624202000/https://www.anaconda.com/web/20250624202000/https://www.anaconda.com/legal/terms/academic). 

.. rubric:: Footnotes
	    
.. [#f1] "Terms of Service."  Anaconda, Published: March 30, 2024. Retrieved from: https://web.archive.org/web/20240808124157/https://legal.anaconda.com/policies/en/.

	

Introduction
------------

This paper addresses the recent changes to Anaconda's Terms of Service (ToS) and their implications for academic researchers. Specifically, we:

- Provide background on the recent modifications to Anaconda's ToS and their timeline
- Direct readers to resources that help facilitators and researchers understand the impact and importance of these changes
- Highlight the key challenges these changes present for the research community

For broader considerations including terminology distinctions, licensing models, cost implications, and compliance requirements, please refer to the companion  introduction of the companion paper :doc:`/PaperB_institutional-leadership/White-paper-to-institutional-leadership`.



Compliance concerns
-------------------

Key questions remain unanswered:

- Does an “academic tier” exemption cover external collaborators (NSF- or DOE-funded researchers without formal university appointments)?

- Can the institution provide a single “proof of affiliation” to Anaconda, or must every individual user register separately?

- Exploring alternatives: Discussions are underway to evaluate alternative tools and approaches to manage software environments — Miniforge, Mamba, Pip, Pixi, and/or UV. Anaconda has not provided clarity on free distribution of containerization platforms such as Singularity/Apptainer or Docker.


Implications for Collaborations and Scientific Workflows
--------------------------------------------------------

Researchers rely on pre-built environments and shared workflows, which can be affected by recent Anaconda changes. These changes may complicate sharing and collaboration on projects that use conda environments.


Alternative Solutions and Recommendations
-----------------------------------------

- Miniforge (pulls from conda-forge by default)
- Pip (pulls from PyPI)
- Pip + venv
- Poetry / Pipenv / uv (pulls from multiple sources)

  
Overview Conda vs Mamba
-----------------------

`Conda <https://github.com/conda/conda>`__ and `Mamba <https://github.com/mamba-org/mamba>`__ are package managers and command-line tools, they can be used mostly interchangeably as Mamba was created as a drop-in replacement for Conda (with identical CLI). Both support channels like `conda-forge <https://github.com/conda-forge>`__ and `Anaconda’s defaults <https://www.anaconda.com/docs/tools/working-with-conda/reference/default-channels>`__. The use of Anaconda Inc.’s defaults channels is subjected to `Anaconda Inc.’s TOS <https://legal.anaconda.com/policies/en/>`__. 

Conda is written in Python and Mamba is written C/C++ and has a faster dependency resolution as it uses `libsolv <https://github.com/openSUSE/libsolv>`__, which is a fast dependency solver also used by Linux package managers, and it can also parallelize downloads speeding installation further. As of version `23.10.0 <https://conda.github.io/conda-libmamba-solver/user-guide/>`__ conda uses by default the `conda-libmamba-solver` plugin which allows conda to use the same `libsolv` solver used by mamba (see: https://conda.github.io/conda-libmamba-solver/user-guide/).

Conda can be used independently of the Anaconda distribution (which uses conda as its package manager but also includes tools such as `Spyder <https://www.spyder-ide.org/>`__).  Mamba was originally developed by `QuantStack <https://quantstack.net/>`__ and is distributed by QuantStack and Mamba contributors. Both package managers are open source and licensed under the BSD 3-Clause License. 

Conda and Mamba are general purpose package managers which offer support for: Python, R, C/C++, JavaScript/node, compilers, etc. Alternatives to conda and mamba are generally only available for Python (and for specific versions of Python) and do not cover system libraries.

There are numerous permutations of these tools for installers available that include different combinations of the components described here. These include “micromamba”, “mambaforge”, etc.


.. attention:: 
		SHOULD WE STILL DO THIS??? explore commercial or open-source, community-driven alternatives to Anaconda’s offerings, with attention paid to Python vs R vs other-centric environments.

  
Overview: Conda vs Miniforge and alternate conda package channels
-----------------------------------------------------------------

You can continue to use conda as a package manager, but would need to configure it to only install packages from community-provided sources that do not require a license.  Conda packages are organized into `channels <https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html>`__, where each channel is a different source for packaged software.

Conda typically comes configured to install packages from the "defaults" channel, which supplies packages from the Anaconda, Inc. repository.  Use of those packages may require a license from Anaconda, Inc.  A common alternative channel is "conda-forge" which provides a large collection of community-supplied packages.  Another commonly used community channel is "bioconda."

.. attention::

   According to: https://web.archive.org/web/20250506034856/https://www.anaconda.com/web/20250506034856/https://www.anaconda.com/pricing/terms-of-service-faqs we may not need to block Anaconda.com channels:
   
   Does Anaconda require academic entities with 200 or more employees to purchase a business or enterprise license?
   
   No. Anaconda does not require academic institutions and universities to purchase a business or enterprise license for access to our package repository, regardless of their size, when used in course curricula. We maintain a free-use policy for educational entities when Anaconda is used in course curricula, including teaching, learning, and research at accredited educational institutions worldwide. This free-use policy applies even to large universities with 200 or more employees. The 200-employee threshold for paid licenses primarily applies to commercial organizations. **However, it’s important to note that paid licenses may be required for specific use cases within academic settings, such as embedding Anaconda’s products, mirroring them, or providing third-party access beyond standard educational use.**


Important Update on the "defaults" Channel
------------------------------------------

- Conda-forge has released a transition guide for migrating away from the "defaults" channel in the context of miniforge. Note that:
  * The "defaults" channel has been deprecated
  * It is scheduled for removal in version 25.9


Resources
^^^^^^^^^

- Transition Guide: https://conda-forge.org/docs/user/transitioning_from_defaults/
- Deprecation Postponement Details: https://github.com/conda/conda/pull/14662

Additional recommendations if using conda-forge
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Using conda-forge, if you don't already have conda installed

  Install "Miniforge" instead of installing the Anaconda distribution.  Miniforge is a version of conda that is pre-configured to only access the "conda-forge" channel.  See https://conda-forge.org/download/ for this option.  The downside of Miniforge is that unlike the Anaconda distribution, Miniforge does not create a rich "base" environment with 300+ packages to get you started. Rather, Miniforge’s “base” environment is intentionally minimalistic and is meant to serve the functionality of the installer itself.  You will then need to either populate this “base” environment with packages of your choice, or to create additional conda environment(s) and specify which packages you want to use.  The command would look something like:

  .. code-block:: console
 
    $ conda create -n environment_name package1 package2 ... packageN

  For a more specific example:

  .. code-block:: console
 
   $ conda create -n mypandas numpy pandas

- Using conda-forge, if you already have conda installed

  You can see which channels it is configured to use like so:

  .. code-block:: console
 
   $ conda config --show channels
   channels:
     - defaults

  You can then swap one channel for the other like so:

  .. code-block:: console
 
   $ conda config --append channels conda-forge
   $ conda config --remove channels defaults
   $ conda config --show channels
   channels:
     - conda-forge

"Conda-forge" is a large community, but may not have every package you need.  If you are interested in a particular package, you can find if any channels offer it by searching for it on the anaconda.org website (note: not the same as anaconda.com). If you find a channel you want conda to install packages from, you can add it to the conda configuration as was done in the above example.

.. note::  While the community-provided packages are stored on Anaconda, Inc.'s servers as a courtesy, they are not owned or created by Anaconda, Inc. so do not fall under Anaconda's licensing terms.


Overview Conda vs Pip
---------------------       

.. attention:: ADD section to the fact that many project are now putting effort into creating wheels that allows for an easy installation of packages
	       
               - Call out a few examples: databases  / in cases you need to install dependencies (kafka stream / official kafka client works from conda but compiling from scratch can be intensive)
		 

Pip is appropriate for:

- Pure Python projects
- Access to the comprehensive PyPI repository
- Projects with Python-only dependencies

Comparison: Conda vs pip:

+-------------------+------------------------------------+-------------------+
|                   | pip                                | conda             |
+-------------------+------------------------------------+-------------------+
| Installs Packages | Wheel or source/requires compilers | Binaries/compiled |
+-------------------+------------------------------------+-------------------+
| Used for          | Python                             | Multiple languages|
+-------------------+------------------------------------+-------------------+
| Dependency check  | Some                               | Yes               |
+-------------------+------------------------------------+-------------------+


Virtual environments in Python
------------------------------

Virtual environments can be created via `Python’s venv module <https://docs.python.org/3/library/venv.html>`__, for convenience users may opt to store such environments in a centralized directory, conventionally named: `$HOME/.virtualenvs`, or in a directory within a user’s project directory, conventionally named: `.venv` or `venv`, (see also: `Install packages in a virtual environment using pip and venv <https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments>`):

.. code-block:: console
 
   $ python -m venv $HOME/.virtualenvs/<ENV_NAME>
   $ source $HOME/.virtualenvs/<ENV_NAME>/bin/activate
   # any successive installation via pip will occur in 
   # $HOME/.virtualenvs/<ENV_NAME> (no need to use `--user` flag):
   $ pip install --upgrade pip
   # a virtual environment can be deactivated with:
   $ deactivate

A Python environment can be created using a `requirements.txt file <https://pip.pypa.io/en/latest/user_guide/#requirements-files>`__:

.. code-block:: console
 
   $ python -m venv $HOME/.virtualenvs/<ENV_NAME>
   $ source $HOME/.virtualenvs/<ENV_NAME>/bin/activate
   $ python -m pip install -r requirements.txt

A `requirements.txt` file can be created with:

.. code-block:: console
 
   $ pip freeze > requirements.txt

A limitation of the `venv` module is that a) it is only limited to Python packages, and b) it can only create virtual environments with a Python version as the one used to create the Python environment. Other tools exist to overcome the latter limitation, such as conda, mamba, Poetry/Pipenv and UV.

References:
`Understanding Conda and Pip <https://www.anaconda.com/blog/understanding-conda-and-pip>`__
`Pip vs Conda: A Guide to Managing Python Packages for Data Scientists <

https://saturncloud.io/blog/pip-vs-conda-a-guide-to-managing-python-packages-for-data-scientists/#pip-vs-conda-key-differences
https://saturncloud.io/blog/pip-vs-conda-a-guide-to-managing-python-packages-for-data-scientists/
https://saturncloud.io/blog/pip-vs-conda-a-guide-to-managing-python-packages-for-data-scientists/#:~:text=Pip%20vs%20Conda%3A%20Key%20Differences&text=Pip%20installs%20packages%20from%20the,Anaconda%20distribution%20and%20other%20channels.>`__

`Install packages in a virtual environment using pip and venv <https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/>`__


Checking for Anaconda Repository Dependencies
---------------------------------------------

Get a list of your environments:

.. code-block:: console
 
   $ conda env list
   # conda environments:
   #
   myenv        /home/user/.conda/envs/myenv
   test         /home/user/.conda/envs/test
   base      *  /apps/software/Miniforge3/24.1.2-0

For each environment's path listed above, check where the installed packages came from:

.. code-block:: console

   $ conda list --explicit --prefix /home/user/.conda/envs/myenv | grep anaconda.com
   https://repo.anaconda.com/pkgs/main/linux-64/libgd-2.2.5-h8e06009_4.conda

If you see any packages listed from "repo.anaconda.com", these fall under the Anaconda Terms of Service and may require a license for continued use.


R and Anaconda
--------------

Anaconda can be useful to manage separate virtual environments and R versions. This functionality can be retained while avoiding paid channels by sticking to strict channel sources using bioconda and conda-forge. Pixi or miniforge are good options for this. Like with Python, some R packages may not be available in conda-forge but should be available in `CRAN <https://cran.r-project.org/>`__ or other non-conda repositories. Additionally, virtual environments are available within R itself via `renv <https://rstudio.github.io/renv/>`__. R also offers the ability to specify different package paths using R_LIBS_USER / .libPaths() which offers the functionality of virtual environments.

.. attention:: Should we remove the following points? Or address them?

	       - Provide guidance on evaluating and transitioning to new platforms.
	       - Suggest strategies for negotiating with Anaconda or seeking waivers/exemptions. The CaRCC Anaconda Transition working group has shouldered the burden here.
	       - Provide guidance on how facilitators can best educate their users.


User Education and Outreach
---------------------------

.. attention:: Does this section need to be here?

Conclusion
----------

.. attention:: 

   - Summarize the key takeaways and provide a call to action for academic research computing facilitators.
   - Encourage collaboration and advocacy to address this issue within the academic community.


Other alternatives
------------------

The primary motivating feature for many researchers from the beginning for the user of a tool like Anaconda was the ability to materialize a specific Python and its dependencies (Python and non-Python) on the local filesystem as an unprivileged user. This is what a virtual environment solution solves. Two new developments in recent times that alleviate the need for this in the first place are improvements and adoption of build-from-source package management (i.e. Spack) and containerization (e.g., Apptainer).

Spack
^^^^^

Spack is an HPC-centric package manager developed by the Department of Energy (DoE) national labs which allows users to instantiate one or more instances of itself, each of which can compile the whole world all the way down the dependency tree. This satisfies the need for getting specific Python versions onto the system for unprivileged users and/or non-Python dependencies. In fact, Spack has the ability to materialize proper virtual environments out of package requirements. The major downside here is in the combinatorial complexity of all the possibilities to satisfy these dependencies and the time cost for compiling everything. The initial setup of these instances can be a big lift but once done users can benefit from a shared build-cache and mirroring of packages to accelerate installation of packages.


Containers
^^^^^^^^^^

Entirely separate from the present discussion is the modern quest for reproducibility and reusability of research software driving the adoption of container technologies like Docker, Apptainer, Podman, etc. Again, with the goal being to allow unprivileged users to bring their own Python and install both Python and non-Python dependencies into a self-contained environment, container technologies satisfy this need simultaneously with their added benefits to reproducibility (single hashable file, registry, DOI, etc.), and reusability (relocating whole software environments to new users and computing systems). Tools like Anaconda stem in large part from the fact that researchers did not have admin rights to the computing systems they run on, and they wanted more than one distinct instance of the software stack. Containers give them this, entirely obviating the use-case for package managers like Anaconda.
