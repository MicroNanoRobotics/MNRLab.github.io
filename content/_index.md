---
# Leave the homepage title empty to use the site title
title:
date: 2024-10-24
type: landing

sections:
  # - block: hero
  #     content:
  #       title: 欢迎访问王化平教授团队主页
  #       text: Welcome to the Official Site of Huaping Wang Research Team
  #     primary_action:
  #       text: Get Started
  #       url: https://example.org
  #       icon: rocket-launch
  #     design:
  #       spacing:
  #         padding: [0, 0, 0, 0]
  #         margin: [0, 0, 0, 0]
  #       # For full-screen, add `min-h-screen` below
  #       css_class: "dark"
  #       background:
  #         color: "navy"
  #         image:
  #           # Add your image background to `assets/media/`.
  #           filename: bg-triangles.svg
  #           filters:
  #             brightness: 0.5
  - block: hero
    content:
      title: |
        微纳机器人研究团队
      primary_action:
        text: Get Started
        url: https://example.org
        icon: rocket-launch
      design:
        spacing:
          padding: [0, 0, 0, 0]
          margin: [0, 0, 0, 0]
        # For full-screen, add `min-h-screen` below
        css_class: "dark"
        background:
          color: "navy"
          image:
            # Add your image background to `assets/media/`.
            filename: bg-triangles.svg
            filters:
              brightness: 0.5
      image:
        filename: wanghuaping2.jpg
      text: |
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
      title: 
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: cover3.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: contain
          text_color_light: true
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
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
        
    design:
      columns: '1'



---
