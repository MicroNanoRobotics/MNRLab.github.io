---
title: "Deep Reinforcement Learning-Based Collision-Free Navigation for Magnetic Helical Microrobots in Dynamic Environments"
authors:
- Huaping Wang
- Yaozhen Hou
author_notes:
- "The first author"
- "Corresponding author"
date: "2024-10-08T00:00:00Z"
doi: "10.1109/TASE.2024.3470810"

# Schedule page publish date (NOT publication's date).
publishDate: "2024-10-08T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "IEEE Transactions on Automation Science and Engineering"
publication_short: ""

abstract: Magnetic helical microrobots have great potential in biomedical applications due to their ability to access confined and enclosed environments via remote manipulation by magnetic fields. However, achieving collision-free navigation for microrobots in complex and unstructured environments, particularly in highly dynamic settings, remains a challenge. In this paper, we present a novel deep reinforcement learning-based control framework for magnetic helical microrobots, focusing on the tasks of goal-reaching and dynamic obstacle avoidance. To streamline data collection, a specialized training environment capturing essential aspects of navigation for magnetic helical microrobots is devised. The robustness and adaptability of the trained policy are supported using a randomization technique within the training environment. To facilitate seamless integration with real-world magnetic actuation systems, a visual processing algorithm based on OpenCV is devised and incorporated to collect policy observations. Simulations and experiments in various scenarios validate the high robustness and adaptability of the method. The performance assessment revealed a success rate of 99% in navigating the microrobot around 4 dynamic obstacles of comparable speeds and a success rate of 90% in environments with 14 dynamic obstacles. The results indicate the potential for future applications of our method in unstructured, confined, and dynamic living environments. Note to Practitioners —The motivation of this work is to develop a robust and effective control scheme for collision-free navigation of magnetic helical microrobots in dynamic environments. The conventional navigation strategies in dynamic environments mainly include global path planning and local path replanning; thus, highly dynamic environments require frequent updates to the planned path, making it difficult to apply in highly dynamic environments. In this work, a deep reinforcement learning-based control framework is proposed that can guide microrobots through many dynamic obstacles to a series of locations without collisions. The simulation and experimental results validate the efficacy of the proposed control framework and the robustness and adaptability of the trained policy. The proposed control scheme enables better understanding of advanced motion control methods for magnetic microrobots.
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
