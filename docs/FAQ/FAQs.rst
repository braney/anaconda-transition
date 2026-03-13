FAQs
====

Q: What prompted the creation of this information and the transition efforts?
-----------------------------------------------------------------------------

The need for this discussion comes from Anaconda’s recently updated Terms of Service (ToS).
These changes create immediate risks for the infrastructure used in university research and teaching.
Anaconda Inc. revised its ToS to indicate that free access to their core distribution or their standard package channel ("defaults channel") might stop for large, non-commercial academic research institutions (defined as having over 200 employees or contractors).
These updated terms were effective as of July 15, 2025.

Q: Who is addressing these issues for the academic community?
-------------------------------------------------------------

The Anaconda Transition Working Group (ATWG), which operates under the umbrella of the Campus Research Computing Consortium (CaRCC), was formed to help the Research Computing and Data (RCD) community ensure compliance with the changes proposed by Anaconda Inc. and explore alternative solutions for package management.

Licensing and Cost Implications for Academia
--------------------------------------------

Q: Is Conda still free to use?
''''''''''''''''''''''''''''''

Yes. Conda (the package manager) is free and open-source. However, when choosing specific flavor of an installer and subsequently downloading, installing, using, or updating packages, users need to know the terms of service that apply to where those packages are hosted.

Q: Which organizations require a paid license under the updated ToS?
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The distribution of packages Anaconda builds and maintains remains free for individuals and small organizations (defined as having less than 200 employees or contractors). A paid license is required for large organizations defined in the Terms of Service as having more than 200 employees or contractors.

Q: Are accredited academic institutions exempt from the licensing fee, even if they have more than 200 employees?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Yes. Anaconda is free for all educational institutions—even those with 200 or more employees or contractors—when used in a course curriculum, including teaching, learning, and researching, at accredited universities worldwide.

Q: Are there scenarios where an educational institution still requires a paid license?
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Yes. A paid license is always required for any individual or entity—even an educational entity—that is embedding, mirroring, or providing third parties access to Anaconda products. This specific clause is highly problematic for data center software maintainers because central installations might be seen as providing third-party access, and creating/sharing containers might be seen as embedding the software.

Compliance and Operational Challenges
-------------------------------------

Q: What compliance ambiguities remain regarding academic use?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Key questions remain unanswered, particularly concerning external collaborations and institutional management:
External Collaborators: Does the "academic tier" exemption cover external collaborators (e.g., NSF- or DOE-funded researchers without formal university appointments)?

Affiliation Proof: Can the institution provide a single "proof of affiliation" to Anaconda, or must every individual user register separately? Anaconda's Academic Policy suggests an institution should reach out to initiate an institution-wide agreement.

Q: How do the ToS impact sharing research through containers (Docker/Apptainer)?
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Anaconda Inc.'s Terms of Service prevent "embedding" (incorporating Anaconda Content into another product or service) and prevent "distribut[ing] the Platform or any Offering to anyone other than your Users". Sharing a container image (like Docker or Apptainer) that includes restricted Anaconda Inc. packages may be considered "embedding" or "distribution" outside the originating institution, potentially violating the terms. The only solution identified is to ensure that restricted Anaconda Inc. packages are not included in any containers.

Q: How can I check if my existing environments use licensed packages from Anaconda?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

You can determine if your packages originate from Anaconda channels (which may require a license) by using the Conda package manager command line tool command line:

List environments: Use `$ conda env list`.

Check package sources for a specific environment: Use `$ conda list --explicit --prefix /path/to/environment | grep anaconda.com`.

If you see packages listed from "repo.anaconda.com", these fall under the Anaconda Terms of Service and may require a license for continued use.

Alternative Solutions and Migration Strategies

Q: How can I use Conda while avoiding packages that require a commercial license?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

You can configure Conda to only install packages from community-provided sources that do not require a license. Conda packages are organized into channels, and the "defaults" channel supplies packages from the Anaconda, Inc. repository.

Switching Channels: You can configure Conda to stop using the "defaults" channel and instead use community channels like "conda-forge" or "bioconda".

Example Commands (to switch an existing installation):

Show current channels: `$ conda config --show channels`.

Append “conda-forge” channel: `$ conda config --append channels conda-forge`.

Remove Anaconda Inc.’s “defaults” channel: `$ conda config --remove channels defaults`.

Q: What is Miniforge, and how does it help with compliance?
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Miniforge is an alternative, non-Anaconda installer that is pre-configured to only access the "conda-forge" channel. Installing Miniforge instead of the Anaconda distribution is recommended if you do not already have conda installed. Since community-provided packages (like those from conda-forge) do not fall under Anaconda's licensing terms, using Miniforge helps ensure compliance.

Q: Is Miniconda the same as Miniforge?
''''''''''''''''''''''''''''''''''''''

No. Miniconda is an Anaconda Inc.’s version of the installer that is pre-configured to use Anaconda Inc.’s channels (including “defaults”) and does fall under Anaconda's licensing terms.


Q: What other open-source alternatives are being explored?
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The working group is evaluating several alternative tools and approaches to manage software environments, including: Miniforge, Mamba, Pip, Pixi, and UV.

Q: How does Mamba relate to Conda?
''''''''''''''''''''''''''''''''''

Mamba is a package manager and command line tool created as a drop-in replacement for Conda (with an identical CLI). Mamba is written in C/C++ and has a faster dependency resolution than the original Conda implementation because it uses libsolv (a fast dependency solver also used by Linux package managers). Note that Conda now uses the conda-libmamba-solver plugin by default, allowing Conda to use the same libsolv solver as Mamba.


Q: Should I use Pip instead of Conda?
'''''''''''''''''''''''''''''''''''''

Pip is appropriate for pure Python projects and accessing the comprehensive PyPI repository. However, Pip's limitations compared to Conda include that it is typically only for Python packages, while Conda supports multiple languages (Python, R, C/C++, JavaScript/node, etc.). Also, Pip installs wheels or source packages (sometimes requiring compilers), while Conda installs binaries/compiled packages. Unlike Conda, Pip does not inherently perform dependency checks across non-Python system libraries.

Q: What non-package manager alternatives exist for managing research environments?
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Two major alternatives that alleviate the need for package managers like Anaconda are:

Spack: An HPC-centric package manager that allows users to compile the entire dependency tree (Python and non-Python), fulfilling the need for specific software versions for unprivileged users.

Containers: Technologies like Docker, Apptainer, and Podman allow researchers to bring their own Python and install both Python and non-Python dependencies into a self-contained, reproducible environment.

Academic Advocacy
-----------------

Q: What actions are academic institutions taking now?
'''''''''''''''''''''''''''''''''''''''''''''''''''''

The CaRCC working group encourages institutions to:
- Evaluate and Pilot Alternatives: Proactively explore and test alternative package management and distribution solutions (like Miniforge/Mamba) to reduce reliance on Anaconda.
- Leverage Collaboration: Share best practices for managing the transition within the CaRCC community.
Establish Contingency Plans: Develop strategies to ensure research continuity if access to Anaconda becomes restricted or unsustainable.

