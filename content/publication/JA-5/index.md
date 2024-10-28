---
title: "Data-driven Parallel Adaptive Control for Magnetic Helical Microrobots with Derivative Structure in Uncertain Environments"
authors:
- Huaping Wang
- Zhiqiang Zheng
author_notes:
- "The first author"
- "Corresponding author"
date: "2024-07-01T00:00:00Z"
doi: "10.1109/TSMC.2024.3374071"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-07-01T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Transactions on Systems, Man and Cybernetics: System"
publication_short: ""

abstract: Micron-range untethered, magnetic helical robots have great potential for biomedical applications due to their desirable performance with high flexibility and accuracy in unstructured and confined environments. However, at the microscale, time-varying uncertain disturbances in the environment and electromagnetic system greatly hinder helical microrobot tracking control performance. When a microrobot is replaced or even a derivative version with a slight helical body structure change is used for different tasks, the performance of the original control scheme remarkably decreases or even becomes ineffective. Here, we propose a data-driven optimal integrated controller (D 2-OIC) that realizes precise tracking and transfer control among a series of helical microrobots with derived structures in different situations. The control approach has a parallel structure with nonlinear feedforward and linear feedback controllers. The nonlinear feedforward controller inversely maps the relationship between the electromagnetic field state and the helical microrobot motion state, allowing the helical microrobot to quickly approach the desired motion state. The linear feedback controller effectively adjusts the controller parameters using the virtual reference feedback tuning (VRFT) method, thus eliminating any residual motion errors arising from nonlinear control. By retraining on newly acquired and collected cumulative data with assigned weights, the nonlinear feedforward controller is updated to achieve transfer control among various helical microrobot types. In the experiment, two helical microrobot types performed arbitrary path tracking and obstacle avoidance tasks with tracking errors consistently less than 4% of the microrobot body length, demonstrating the feasibility of the proposed method.
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
