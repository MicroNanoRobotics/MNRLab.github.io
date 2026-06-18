---
title: Tour
date: 2024-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
       <br>
        王化平教授课题组

      image:
        filename: wanghuaping2.jpg
      text: |
        <br>
          微纳机器人研究团队
        <br>
          The Lab is committed to magnetic drive software robots, micro and nano robots, micro-scale automation and other fields of research.

  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
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
      title: 期刊合辑
      subtitle: 'xxxxxxxx'
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
      title: Latest article
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
      title:
      subtitle:
      text: |
        {{% cta cta_link="../people/" cta_text="Meet the team ->" %}}
    design:
      columns: '1'
---
