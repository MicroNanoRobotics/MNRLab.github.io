---
title: "IHVIN-GAT-Based Path Planning for Parallel and Independent Manipulation of Heterogeneous Microtargets via OETs in Unstructured Environments"
authors:
- Jiaxin Liu
- Huaping Wang
author_notes:
- "The first author"
- "Corresponding author"
date: "2024-09-06T00:00:00Z"
doi: "10.1109/TSMC.2024.3449132"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-09-06T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Transactions on Systems, Man and Cybernetics: System. "
publication_short: ""

abstract: Manipulating heterogeneous microtargets based on optoelectronic tweezers (OETs) to construct micropatterns with specific distribution and ordered arrangement enables recapitulating the spatial architecture of cells in native tissues, and has significant potential in tissue regeneration, medical diagnostics, and cell behavior research. However, the uncertain disturbances in liquid environment, collision risk, and electrokinetic interference in OETs system can cause microtargets to deviate from the safe and controlled state, especially for manipulation tasks with heterogeneous microtargets. Here, we propose an improved hierarchical value iteration network (IHVIN)-GAT-based path planning method for parallel manipulation of heterogeneous microtargets with independent control, integrating goal assignment, feature extraction, and decentralized decision-making. The Kuhn–Munkres-based goal assignment model periodically modifies the matching relationship between microtargets and goal positions to reduce the task complexity. High-order features involving path planning are extracted by an IHVIN model, and then selectively aggregated and convolved through GAT to yield real-time locomotion strategies for all microtargets. For the issues of constraint variability and system heterogeneity, discrete locomotion constraints are developed through analysis of escape mechanism, then embedded into modeling procedures and converted to heterogeneous edge weights in graph domain. The simulation and experimental results demonstrate the desired performance of the IHVIN-GAT model in high timeliness, high strategy quality, and compatibility for microtarget number, where up to 20 microtargets from three categories are parallel manipulated within 16 s to form arbitrary micropatterns recapitulating microscale architecture of cells in native tissues. We anticipate that our method will contribute to construct more biomimetic microstructures with heterogeneous cells for biomedical applications in the future.
# Summary. An optional shortened abstract.
summary: xxxxxx

tags:
- Article
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: ''
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://spj.science.org/doi/10.34133/research.0414#F1)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example

---

<!-- {{% callout note %}}
Click the *Cite* button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the *Slides* button to check out the example.
{{% /callout %}}

Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://docs.hugoblox.com/content/writing-markdown-latex/). -->
