#######################################
White paper to institutional leadership
#######################################

Addressing the Challenges Posed by Anaconda's New Licensing Model
#################################################################

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
=================

Recent revisions to Anaconda's Terms of Service (ToS) pose immediate
risks to our university's research and teaching infrastructure.
Anaconda's Python distribution and package-management platform has long
been available at no cost for academic use, underpinning – locally and
on our HPC clusters – the majority of scientific workflows across
departments. The newly proposed restrictions and license-fee
requirements could introduce significant financial burdens, disrupt
established computational environments, and undermine collaborative
projects – from individual lab pipelines to cross-campus consortium
efforts.

At a recent Campus Research Computing Consortium (CaRCC) meeting,
representatives from national laboratories, DoE facilities, and peer
institutions underscored shared concerns, such as, which institutions
(and which categories of users – scholarly vs. research, on-campus
vs. external collaborators) qualify for a free or reduced-fee academic
tier, or how would individual researchers submit proof of affiliation,
or can the university secure a blanket exemption, or how will site-wide
installations on shared systems be licensed, particularly when NSF- or
DoE-funded collaborators without formal university appointments also
require access.

At the time of this communication, Anaconda's team was drafting a
standalone academic policy and had invited institutions to coordinate
use-case details and a rollout timeline. The negotiation window has now
closed. Moving forward, we will need to adapt to the finalized terms
while exploring institutional solutions to ensure continued,
cost-effective access to the Anaconda ecosystem, preserve the integrity
of our teaching labs and research clusters, and sustain our science
leadership.



Introduction
============

Anaconda has long been a cornerstone of scientific and academic
computing, offering a robust package management system and an ecosystem
that simplifies the installation and maintenance of numerous open-source
libraries. It is one of the most popular methods of automatically
installing packages and interfacing with AI and other package-based
technologies. However, in early 2024, Anaconda Inc. updated its `terms
of service (ToS) <https://legal.anaconda.com/policies/en/>`__ to imply
that it would no longer support free access to their base distribution
or their *defaults* channel for non-commercial academic research
institutions with more than 200 employees. The
`reason <https://www.anaconda.com/pricing/terms-of-service-faqs>`__ for
updating their ToS was to offset the significant costs associated with
maintaining and hosting their platform and services. But, this update
caused tremendous confusion and anxiety across academic communities that
have historically relied upon Anaconda for their academic and research
work.

In September 2024, a few months after the widespread enforcement of
these changes began, a `blog
post <https://www.anaconda.com/blog/update-on-anacondas-terms-of-service-for-academia-and-research>`__
was published to clarify the intent of the update to the community. This
blog post seemed to suggest that Anaconda would remain free for
researchers at accredited universities, and that a revised update is
forthcoming by year-end. However, the academic community continued to
stay concerned, as blog posts are not legally binding (unlike ToS),
which led to the creation of `Anaconda Transition Working
Group <https://carcc.org/anaconda-transition-working-group/>`__ (ATWG).

ATWG comes under the umbrella of the nationwide Campus Research
Computing Consortium (`CaRCC <https://carcc.org/>`__). It is formed to
help the research computing and data (RCD) community ensure compliance
with the changes proposed by Anaconda Inc. and to come up with
alternatives for package management, if needed. ATWG has been meeting
weekly since October 2024 to discuss the implications of Anaconda Inc's
revised ToS and how to best communicate that to the academic community.
To that end, the group has met with the Anaconda Inc. leadership a
couple of times, in December 2024 and February 2025, to gain clarity on
their ToS and ensure compliance in the face of the changes proposed by
Anaconda Inc. The goals of the meetings included, but were not limited
to:

-  obtaining clarity on the `update to the
   ToS <https://legal.anaconda.com/policies/en/>`__
-  the current status of proposed changes
-  implications of the change on the larger community
-  thoughts and suggestions on how to proceed
-  specific compliance details for various types of institutions

Before proceeding further, it is important to make the distinction between
several terms used here. Anaconda, as a term, could refer to the
company, a package distribution channel, or a package management
software distribution, depending on the context. It could, sometimes,
also be used to refer to the environment management software "conda". On
the other hand, `Anaconda, Inc. <https://www.anaconda.com/>`__, strictly
refers to the privately owned, for-profit company responsible for the
well-known ecosystem for managing scientific software packages. Finally,
Anaconda distribution refers to the software bundle containing "conda",
Anaconda Navigator (desktop application with graphical interface for
managing packages, channels, and environments within the Anaconda,
Inc. ecosystem), a pre-configured "base" environment, and pre-configured
package distribution channels.

According to the updated ToS, downloading the distribution is covered by
the ToS. However, the Anaconda channel that is maintained by the company
is subject to ToS. Additionally, "conda" and its
`repository <https://github.com/conda/conda>`__ is a Free and
Open-Source Software (FOSS) with Berkley Source Distribution
(`BSD <https://www.techtarget.com/whatis/definition/BSD-licenses#:~:text=As%20a%20low%20restriction%20and,was%20first%20written%20in%201969.>`__)
license that is widely used in the Anaconda Distribution, Miniconda, and
Miniforge installers. The primary issues associated with these change(s)
include, but are not limited to:

-  Licensing Costs: Institutions with more than 200 employees must now
   pay for a commercial license to use Anaconda.
-  Compliance: Institutions are receiving notices from Anaconda about
   non-compliance with the new ToS. See `Anaconda puts the squeeze on
   data scientists • The
   Register <https://www.theregister.com/2024/08/08/anaconda_puts_the_squeeze_on/>`__.
-  Heavy Dependence: Academic institutions contribute significantly to
   open-source software used within Anaconda. Based on the above, any
   institution with more than 200 employees will now be required to pay
   for access.
-  Budget Constraints: Many institutions and researchers operate under
   tight budgets, even more so now than ever, that do not account for
   unexpected licensing costs.
-  Operational Challenges: The sudden implementation of these changes
   has disrupted workflows, requiring rapid reassessment of how
   institutions and research computing teams should manage software
   environments.

To address these challenges, ATWG has initiated several actions:

-  Communication with Anaconda Inc.: As noted above, we have had two
   meetings with Anaconda Inc. leadership and representatives. The main
   goals of those meetings were to understand their licensing model
   better and to advocate for equitable treatment of academic
   institutions.
-  Internal collaboration: Institutions within CaRCC are sharing their
   experiences and strategies for adapting to the new licensing model,
   including alternative solutions. ATWG has reached out to CaRCC
   community members in the form of a user survey to understand their
   usage and the level of dependence on Anaconda.
-  Exploring alternatives: Discussions are underway to evaluate
   alternative tools and approaches for managing software environments.
   This includes exploring open-source installers, such as Miniforge,
   and utilizing package managers like
   `Mamba <https://mamba.readthedocs.io/en/latest/>`__,
   `Pip <https://packaging.python.org/en/latest/key_projects/#pip>`__,
   `Pixi <https://pixi.sh/latest/>`__, and/or
   `UV <https://docs.astral.sh/uv/>`__. Additionally, looking into
   containerization platforms like
   `Singularity <https://docs.sylabs.io/guides/latest/user-guide/>`__ or
   `Docker <https://www.docker.com/>`__ could be a possible alternative
   as long as they employ open-source installers or installing packages
   from scratch.



Impact on Academic Institutions
===============================

Academic organizations now face a cascade of practical and financial
hurdles as a result of Anaconda's revised Terms of Service:

1. Escalating Licensing Costs

   Under the new model, any institution with more than 200 employees
   must purchase a commercial license. For a typical mid‐sized
   university—supporting dozens of departments, central IT-managed HPC
   clusters, and distributed lab installations—annual fees could reach
   tens of thousands of dollars. These unplanned expenses threaten to
   divert funding away from core research and teaching needs.

2. Compliance Ambiguity

   CaRCC members report receiving "non-compliance" notices for shared
   installations on central clusters. Key questions remain unanswered:

   -  Does an "academic tier" exemption cover external collaborators
      (NSF- or DoE-funded researchers without formal university
      appointments)?
   -  Can the institution provide a single "proof of affiliation" to
      Anaconda, or must every individual user register separately?

3. Transition Overhead

   Moving away from Anaconda-whether to conda-forge/Miniconda, Spack, or
   containers-requires substantial IT staff time, retraining of faculty
   and students, and revalidation of research pipelines. One peer
   university estimates that piloting a Spack migration consumed over
   200 staff-hours and delayed several high-priority simulation
   campaigns by weeks.

4. Disruption to Scientific Workflows

   Researchers rely on the ease of conda install and prebuilt binary
   packages for everything from molecular dynamics to machine-learning
   toolkits. Any interruption in Anaconda service risks halting active
   data analyses, reproducibility efforts, and deadline-driven
   computational experiments.

5. Complications for Collaboration

   In multi-institution projects — such as DoE lab partnerships or
   interdisciplinary centers — a fragmented licensing landscape could
   force collaborators onto different package ecosystems, undermining
   shared environment files, container images, and joint development
   workflows.

6. Strained Budgets and Sustainability

   Redirecting grant funds and departmental budgets toward license fees
   may force difficult trade-offs: hiring fewer graduate students,
   postponing hardware upgrades, or reducing support for other
   open-source tools critical to our teaching and research missions.



Licensing and Cost Implications
===============================

At the start of 2025, Anaconda
Inc. `released <https://www.anaconda.com/blog/anaconda-for-education-empowering-the-academic-community>`__
`Anaconda for
Education <https://www.anaconda.com/industries/education>`__ to
accelerate AI learning across the academic community for free of charge.
This includes access to free AI courses, storage, and tools at no cost
to users, such as researchers, students, and educators with an academic
access to the Anaconda Starter plan. The products and tools that are
included in this package are `Anaconda
Distribution <https://www.anaconda.com/download>`__, `Anaconda
Navigator <https://www.anaconda.com/products/ai-navigator>`__, `Anaconda
AI
Assistant <https://www.anaconda.com/capability/anaconda-assistant>`__,
`Public Package Repository <https://repo.anaconda.com/>`__, `Anaconda
Learning <https://www.anaconda.com/learning>`__, `Cloud
Notebooks <https://www.anaconda.com/products/notebooks>`__, and `App
publishing with
Panel <https://www.anaconda.com/blog/a-new-and-simple-way-to-publish-your-data-applications>`__.

In order to access the academic account one needs to be either actively
enrolled or employed at an accredited academic institution with a
verified academic email address. However, for an accredited academic
institution, the use of Anaconda package repository continues to be free
and they do not need to purchase any business or enterprise license
regardless of their size. The free-use policy for educational entities
continues to be in effect as long as Anaconda is used in the
institution's course curricula, teaching, learning, and research. In
addition to academia, Anaconda Inc. now offers AI-based solutions by
industry that include finance, healthcare, government, manufacturing,
and technology. All of the categories come with their own price packages
except for academia, where the use is free as long as no embedding,
mirroring, or access to a third party has been carried out for their
products. However, they urge institutions to contact their `partner
team <https://legal.anaconda.com/policies/en/>`__ at
partnerships@anaconda.com should the need to pursue an embedded use case
arises in academia. This is different when compared to their archival
FAQ from `August 13,
2024 <https://web.archive.org/web/20250506042444/https://www.anaconda.com/web/20250506042444/https://www.anaconda.com/pricing/terms-of-service-faqs>`__,
where no such requirement was stated for any kind of academic use
including embedding, mirroring, or third party access.

Given that the state of affairs is still evolving at Anaconda Inc. and
that there is a fair amount of ambiguity in what would constitute as an
out-of-compliance case and when would a license be required, the ATWG
has decided to come up with a number of recommendations for the academic
community that rely upon alternative methods to achieve what can be
accomplished with Anaconda distribution. Additionally, ATWG strongly
feels that the campus research computing teams should not be expected to
police the academic community, in how Anaconda Inc. products are being
utilized by an individual user, once the distribution has been installed
on academic and research clusters in full compliance with Anaconda
Inc.'s policies for academia. Hence, having an alternative would help
the RCD and academic community immensely.

The proposed solutions are all based on open-source software and
distribution that do not depend on any of the Anaconda Inc. products,
thereby allowing us to avoid any license or out-of-compliance issues
with Anaconda Inc. The ATWG has written another white paper,
:doc:`/PaperA_users-researchers/White-paper-to-users-researchers`, in
addition to this one, that explains the methodology of utilizing the
open-source solutions to our researchers and research facilitators. A
summarized version of this is mentioned in the `Alternative Solutions
and Recommendations`_ below.



Compliance Concerns
===================

.. attention:: Need info on notifications institutions have received…
               do we have any examples?
               [leftover comment that needs addressing]

The recent changes to Anaconda's licensing model, which limit the
previously free distribution and usage of its platform for
non-commercial purposes, have raised significant compliance concerns for
academic and research institutions. These concerns are especially
critical as institutions balance the need for cutting-edge research
tools with the strict legal and regulatory frameworks governing their
operations.

**1. Licensing Restrictions and Compliance Risks:**

Anaconda's previous licensing model allowed academic and research
institutions to use the distribution platform freely without incurring
licensing fees, provided the use was non-commercial in nature. This
model has allowed institutions to develop and deploy software
environments, often across large-scale high-performance computing (HPC)
systems, with minimal administrative burden.

However, the new licensing changes—particularly for non-commercial
users—could potentially introduce the risk of non-compliance in the
following areas:

*License/Agreement Enforcement:*
   Institutions must now ensure that any use of Anaconda's distribution
   within non-commercial research environments adheres to the new terms.

According to their current `Academic
Policy <https://www.anaconda.com/legal/terms/academic>`__, an
institution qualifying for an Eligible Academic Institution (EAI)
account should secure an institution-wide agreement for use of Anaconda.
The institution must reach out to their support team to initiate the
process of completing the EAI Agreement with Anaconda and set up an
academic account. However, the agreement prohibits researchers/users
from extending their scaled enterprise deployment to commercial,
non-educational use while using Anaconda at an EAI. This also includes
redistribution of system outputs, which is permitted only within the
scope of non-commercial, educational use under the Academic Policy.

Anaconda reserves the right to verify the institution's eligibility for
the Anaconda for Education Program and the access to this program's
benefits are valid for twelve months from the signing of the EAI
Agreement. Once the duration is expired, the agreement must be renewed
to continue accessing the benefits.

Additionally, Anaconda extends the participation in this program to
individuals as long as they are associated with an EAI. However,
according to their current `Terms of
Service <https://www.anaconda.com/legal/terms/terms-of-service>`__,
section 5, the institution would be responsible for ensuring that all
their users follow these Terms and for any violations of these Terms by
their users. In the case of any modification to the terms of their
Academic Policy, Anaconda will post them to `Anaconda's legal
page <https://www.anaconda.com/legal/terms>`__ with a ninety day notice.
The program participants will not be directly notified but it will be
their responsibility to review the terms of this Policy periodically to
ensure that no new updates have been released.

All of the above puts an additional responsibility on the institution's
representative to ensure that the institution-wide agreement remains
valid, is adhered to at all times, and policy changes are tracked
regularly to avoid any legal complications that might originate from
lack of thereof.

*Auditability:*
   Without clear mechanisms in place to track which users are operating
   under the free or paid licenses, research institutions risk running
   afoul of audit processes. Many institutions are subject to external
   audits, particularly when dealing with government-funded research or
   grants, and failing to demonstrate compliance with software licensing
   requirements can result in penalties or reputational damage.


**2. Potential Legal Implications:**

Academic institutions are often bound by stringent intellectual property
agreements, especially those that receive government or private funding.
The violation of software licensing agreements may have downstream legal
consequences, including:

*Loss of Funding:*
   Non-compliance with software licenses could lead to the forfeiture of
   funding, particularly when grantors specify that software tools and
   infrastructure must be licensed properly and legally.

*Legal Disputes:*
   Institutions that inadvertently breach Anaconda's new licensing terms
   may be subject to litigation. While legal action might be rare, even the
   risk of potential lawsuits can cause significant disruptions and
   reputational harm to an institution, which is particularly concerning
   for publicly-funded research.

**3. Institutional Governance and Policy Updates:**

Institutions must review and potentially update their governance and
policy frameworks to reflect these new licensing terms. Specific areas
for policy development and review may include:

*IT Policies:*
   Updating institutional IT policies to ensure that all research computing
   resources, including HPC clusters, are compliant with Anaconda's new
   licensing terms. This includes developing clear guidelines for faculty
   and researchers regarding which licenses are required for specific
   projects or environments.

*Procurement Processes:*
   Revising procurement processes to account for the financial and legal
   implications of new licensing models. This could involve negotiating
   blanket licenses for entire departments or campuses or deciding whether
   to migrate to alternative software solutions to mitigate compliance
   risk.



Alternative Solutions and Recommendations
=========================================

Given the compliance challenges raised by Anaconda's new licensing
model, academic and research institutions need to explore alternative
solutions to mitigate both financial and operational risks. Below are
several viable options that can help institutions maintain operational
efficiency and compliance while reducing dependency on Anaconda's paid
licensing structure.

**1. Open-Source Package Management Systems**

One of the most straightforward alternatives is to transition to fully
open-source package management systems that can replace Anaconda's
distribution platform, offering similar functionality without licensing
restrictions, such as conda-forge. For a full list of options, see
:doc:`/PaperA_users-researchers/White-paper-to-users-researchers`.
This allows institutions to create isolated environments without requiring a
paid license.

**2. Docker and Containerization**

Containerization platforms provide another viable alternative by
allowing research institutions to build and deploy reproducible research
environments in isolated containers. Containerization allows users to
create self-contained, portable images that can be deployed across other
computing platforms more easily. These containers can also be prebuilt
to include alternative open-source environments and the necessary
software packages, eliminating the need for the Anaconda distribution.

Anaconda Inc.'s `Terms of
Service <https://www.anaconda.com/legal/terms/terms-of-service>`__ (as
of August 29, 2025) prevent "embedding" ("incorporating Anaconda Content
into another product or service") and prevent "distribut[ing] the
Platform or any Offering to anyone other than your Users." Anaconda
Inc.'s `Academic
Policy <https://www.anaconda.com/legal/terms/academic>`__ (as of August
29, 2025) attempts to modify these restrictions slightly, allowing one
"to redistribute system outputs solely for academic purpose," though
it's not clear what they mean by "system outputs."

Our concern with these restrictions is a common use-case of a researcher
creating a Docker (or Singularity/Apptainer) Container to share their
code and/or workflows with other researchers, possibly at other academic
institutions. If that researcher includes Anaconda Inc. packages within
the container image, it could be considered "embedding," which is not
allowed; sharing that container with others outside their own
Institution would certainly seem to count as "distribution". It is
unclear if a Container image would be considered as "system outputs" so
sharing one might not be allowed outside the originating Institution.

The only solution we see in this case is to make sure that the
restricted Anaconda Inc. packages are not included in any Containers.
However, it would be quite difficult for any Institution to monitor the
behavior of all researchers at the level of creating and/or sharing
Container images. A given image could be potentially scanned for
Anaconda, Inc.'s packages, but it is not always clear where a Container
image has come from, or with whom it might have been shared.

**3. Virtual Machines (VMs) and Cloud-based Solutions**

For institutions that require greater flexibility and scalability,
moving to cloud-based research environments or using virtual machines
(VMs) can provide another way to sidestep licensing issues while
ensuring compliance. Institutions can also create custom virtual
machines with specific research environments, using open-source package
managers, to replace Anaconda environments. These VMs can be hosted on
local servers or on cloud platforms.

**4. Hybrid Solutions: Combining Multiple Tools**

In many cases, institutions may find it effective to combine multiple
alternative solutions based on specific needs.

Each of these alternative solutions offers different trade-offs in terms
of cost, compliance, and operational complexity. The best solution for
any given institution will depend on its specific needs, infrastructure,
and available resources.

As institutions move away from Anaconda's licensing model, they should
evaluate the potential of these solutions based on their current
research tools, budget constraints, and long-term goals. A hybrid
approach that incorporates multiple tools may provide the greatest
flexibility and minimize both the compliance risks and operational
burdens of the new licensing restrictions.



Conclusion
==========

While Anaconda's licensing changes pose significant challenges, they
also present an opportunity to reexamine our dependencies and develop
more resilient software ecosystems. Through collaboration and proactive
planning, we can ensure that academic research continues to thrive
without disruption. To that end, our recommendations and call to action
to the community are mentioned below.

Recommendations:
----------------

We propose the following actions to mitigate the impact:

1. **Continue Advocacy:** Strengthen dialogue with Anaconda to seek
   adjustments that better support academic institutions, such as
   discounted or waived fees for specific use cases.
2. **Leverage Community Collaboration:** Build on the efforts within
   CaRCC to document and share best practices for managing the
   transition.
3. **Evaluate and Pilot Alternatives:** Proactively explore and test
   alternative package management and distribution solutions to reduce
   reliance on Anaconda.
4. **Establish Contingency Plans:** Develop strategies to ensure
   research continuity if access to Anaconda becomes restricted or
   unsustainable.


Call to Action
--------------

We encourage institutional leaders to:

-  Engage in ongoing discussions within the CaRCC community.
-  Support the evaluation of alternative tools and approaches.
-  Collaborate with peer institutions to present a unified voice in
   advocating for equitable academic licensing.


.. attention:: Are we putting contacts here, or on the top page?
               I'd say, either on the top page (as the entire group's work)
               or make authors list fully-qualified with affiliations and emails.

| **Contact Information**
| A,B, C, D
