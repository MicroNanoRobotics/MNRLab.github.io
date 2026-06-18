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
        微纳机器人实验室

      image:
        filename: wanghuaping2.jpg
      text: |
        <br>
          实验室聚焦磁驱软体机器人、微纳机器人、微尺度自动化及相关交叉方向研究。

  - block: collection
    content:
      title: 新闻动态
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
      title: 期刊封面
      subtitle: 代表性科研成果
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
      title: 最新论文
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
        {{% cta cta_link="../people/" cta_text="查看团队成员 ->" %}}
    design:
      columns: '1'
---
