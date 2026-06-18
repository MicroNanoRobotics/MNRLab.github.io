---
title: Tour
date: 2024-10-24
type: landing
translationKey: tour

sections:
  - block: hero
    content:
      title: |
       <br>
        Micro Nano Robotics Lab

      image:
        filename: wanghuaping2.jpg
      text: |
        <br>
          The lab is committed to magnetic soft robots, micro and nano robots, micro-scale automation, and related interdisciplinary research.

  - block: collection
    content:
      title: Latest News
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'

  - block: markdown
    content:
      title: Journal Covers
      subtitle: Selected research highlights
      text: |
        <div align="center">
          <img src="cover3.jpg" alt="" width="100%" height="auto">
        </div>
    design:
      columns: '1'
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

  - block: collection
    content:
      title: Latest Articles
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article-journal'
    design:
      view: citation
      columns: '5'

  - block: markdown
    content:
      text: |
        {{% cta cta_link="../people/" cta_text="Meet the team ->" %}}
    design:
      columns: '1'
---
